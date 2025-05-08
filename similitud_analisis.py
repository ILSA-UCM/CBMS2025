import json
import pandas as pd

def limpiar_lista_terminos(lista):
    return [
        t.strip()
        for t in lista
        if isinstance(t, str) and t.strip().lower() != 'nan' and t.strip() != ''
    ]

def evaluar_resultado_con_equivalencias(
    json_test_file,
    csv_gold_file,
    equiv_gold_to_test,
    equiv_test_to_test,
    equiv_gold_to_gold,
    output_csv="evaluacion_resultados.csv",
    output_md="evaluacion.md"
):
    equiv_gold_to_test = {k.lower(): v for k, v in equiv_gold_to_test.items()}
    equiv_test_to_test = {k.lower(): v for k, v in equiv_test_to_test.items()}
    equiv_gold_to_gold = {k.lower(): v for k, v in equiv_gold_to_gold.items()}

    with open(json_test_file, "r") as f:
        test_data = json.load(f)

    df_gold = pd.read_csv(csv_gold_file)
    gold_dict = {
        str(row[0]).strip(): [str(x).strip().lower() for x in str(row[1]).split(',') if x.strip()]
        for _, row in df_gold.iterrows()
    }

    rows = []
    total_recuperados = 0
    relevantes_recuperados = 0
    total_relevantes = 0
    total_recuperados_exp = 0
    total_relevantes_exp = 0

    for doc in test_data:
        doc_id = doc["clave"]
        texto = doc["texto"]
        test_terms = [a["finding"].strip().lower() for a in doc.get("anotado", []) if a.get("finding")]
        gold_terms = gold_dict.get(doc_id, [])
        gold_terms = limpiar_lista_terminos(gold_terms)

        # Mapear gold_terms con Gold → Test
        gold_to_test_mapped = set()
        for g in gold_terms:
            gold_to_test_mapped.update(equiv_gold_to_test.get(g, []))

        # Expandir test_terms con Test → Test (solo para comparación)
        test_expanded = set(test_terms)
        for t in test_terms:
            test_expanded.update(equiv_test_to_test.get(t, []))

        # Expandir gold_terms con Gold → Gold (solo para referencia)
        gold_expanded = set(gold_terms)
        for g in gold_terms:
            gold_expanded.update(equiv_gold_to_gold.get(g, []))

        # Evitar sobrecontar equivalencias duplicadas
        encontrados = set()
        for g in gold_terms:
            posibles = set(equiv_gold_to_test.get(g, []))
            if posibles & test_expanded:
                encontrados.add(g)

        total_recuperados += len(test_terms)
        total_relevantes += len(gold_terms)
        relevantes_recuperados += len(encontrados)

        total_recuperados_exp += len(test_expanded)
        total_relevantes_exp += len(gold_expanded)

        rows.append({
            "numeroID": doc_id,
            "Texto": texto,
            "Test": ", ".join(sorted(test_terms)),
            "Gold": ", ".join(sorted(gold_terms)),
            "Test expandido": ", ".join(sorted(test_expanded)),
            "Gold expandido": ", ".join(sorted(gold_expanded)),
            "Mapeado Gold→Test": ", ".join(sorted(gold_to_test_mapped)),
            "Coincidencias (Gold original)": ", ".join(sorted(encontrados)),
        })

    df_resultados = pd.DataFrame(rows)
    df_resultados.to_csv(output_csv, index=False)

    precision = relevantes_recuperados / total_recuperados if total_recuperados else 0
    recall = relevantes_recuperados / total_relevantes if total_relevantes else 0
    f_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0

    precision_exp = relevantes_recuperados / total_recuperados_exp if total_recuperados_exp else 0
    recall_exp = relevantes_recuperados / total_relevantes_exp if total_relevantes_exp else 0
    f_score_exp = 2 * (precision_exp * recall_exp) / (precision_exp + recall_exp) if (precision_exp + recall_exp) else 0

    with open(output_md, "a", encoding='utf-8') as md:
        md.write("### Métricas de evaluación (solo términos originales)\n\n")
        md.write(f"- **Total recuperados (Test)**: {total_recuperados}\n")
        md.write(f"- **Relevantes recuperados (Gold→Test, sin duplicados)**: {relevantes_recuperados}\n")
        md.write(f"- **Relevantes totales (Gold)**: {total_relevantes}\n")
        md.write(f"- **Precisión**: {precision:.2%}\n")
        md.write(f"- **Recall**: {recall:.2%}\n")
        md.write(f"- **F Score**: {f_score:.2%}\n\n")

        md.write("### Métricas de evaluación (con expandidos, solo para referencia)\n\n")
        md.write(f"- **Total recuperados (Test expandido)**: {total_recuperados_exp}\n")
        md.write(f"- **Relevantes totales (Gold expandido)**: {total_relevantes_exp}\n")
        md.write(f"- **Precisión**: {precision_exp:.2%}\n")
        md.write(f"- **Recall**: {recall_exp:.2%}\n")
        md.write(f"- **F Score**: {f_score_exp:.2%}\n")

    print(f"\n✅ CSV guardado en: {output_csv}")
    print(f"📝 Markdown generado en: {output_md}")
