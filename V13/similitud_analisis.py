import json
import pandas as pd

def evaluar_resultado_con_equivalencias(
    json_test_file,
    csv_gold_file,
    equiv_gold_to_test,
    equiv_test_to_test,
    equiv_gold_to_gold,
    output_csv="evaluacion_resultados.csv",
    output_md="evaluacion.md"
):
    # === Cargar archivo JSON de test
    with open(json_test_file, "r") as f:
        test_data = json.load(f)

    # === Cargar archivo CSV de gold
    df_gold = pd.read_csv(csv_gold_file)
    gold_dict = {
        str(row[0]).strip(): [str(x).strip().lower() for x in str(row[1]).split(',') if x.strip()]
        for _, row in df_gold.iterrows()
    }

    # === Evaluación documento a documento
    rows = []
    total_recuperados = 0
    relevantes_recuperados = 0
    total_relevantes = 0

    for doc in test_data:
        doc_id = doc["clave"]
        texto = doc["texto"]
        test_terms = [a["finding"].strip().lower() for a in doc.get("anotado", []) if a.get("finding")]
        gold_terms = gold_dict.get(doc_id, [])

        # Expandir test_terms con Test → Test
        test_expanded = set(test_terms)
        for t in test_terms:
            test_expanded.update(equiv_test_to_test.get(t, []))

        # Expandir gold_terms con Gold → Gold
        gold_expanded = set(gold_terms)
        for g in gold_terms:
            gold_expanded.update(equiv_gold_to_gold.get(g, []))

        # Mapear gold_terms con Gold → Test
        gold_to_test_mapped = set()
        for g in gold_terms:
            gold_to_test_mapped.update(equiv_gold_to_test.get(g, []))

        # Intersección entre test_expanded y gold_to_test_mapped
        encontrados = test_expanded & gold_to_test_mapped

        total_recuperados += len(test_expanded)
        total_relevantes += len(gold_expanded)
        relevantes_recuperados += len(encontrados)

        rows.append({
            "numeroID": doc_id,
            "Texto": texto,
            "Test": ", ".join(sorted(test_terms)),
            "Gold": ", ".join(sorted(gold_terms)),
            "Test expandido": ", ".join(sorted(test_expanded)),
            "Gold expandido": ", ".join(sorted(gold_expanded)),
            "Mapeado Gold→Test": ", ".join(sorted(gold_to_test_mapped)),
            "Coincidencias": ", ".join(sorted(encontrados)),
        })

    # === Calcular métricas
    precision = relevantes_recuperados / total_recuperados if total_recuperados else 0
    recall = relevantes_recuperados / total_relevantes if total_relevantes else 0
    f_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0

    # === Crear CSV con los resultados
    df_resultados = pd.DataFrame(rows)
    df_resultados.to_csv(output_csv, index=False)

    # === Crear archivo Markdown con equivalencias y métricas
    with open(output_md, "a") as md:
        def dump_dict(title, d):
            md.write(f"### {title}\n\n")
            for k in sorted(d):
                v = ", ".join(sorted(d[k]))
                md.write(f"- `{k}` -> {v}\n")
            md.write("\n")



        # Métricas
        md.write("### Métricas de evaluación\n\n")
        md.write(f"- **Total recuperados (Test expandido)**: {total_recuperados}\n")
        md.write(f"- **Relevantes recuperados (Gold→Test)**: {relevantes_recuperados}\n")
        md.write(f"- **Relevantes totales (Gold expandido)**: {total_relevantes}\n")
        md.write(f"- **Precisión**: {precision:.2%}\n")
        md.write(f"- **Recall**: {recall:.2%}\n")
        md.write(f"- **F Score**: {f_score:.2%}\n")

    print(f"\n✅ CSV guardado en: {output_csv}")
    print(f"📝 Markdown generado en: {output_md}")
