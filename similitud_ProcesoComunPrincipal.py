from similutud import (cargar_y_combinar_findings,
                       alingTerminology,
                       convertir_a_diccionario,
                       extraer_lineas_validas,
                       es_formato_valido)

from similitud_analisis import evaluar_resultado_con_equivalencias
import time
import pandas as pd


def pipeline_evaluacion_con_equivalencias(
    ResultadoFinalTerminos="resultadoFinalNormal__1.5.json",
    ResultadoFinalTerminosDocumento="resultadoFinalNormalDocNN__1_5.json",
    csvGold="20250430_9e5995.csv",
    deepseek_r___b="deepseek-r1:1.5b",
    csvSalidaTabla="resultadoTabla__1.5.csv",
    mdSalidaResumen="resultadoResumen__1.5.md"
):
    # === Paso 1: Cargar y comparar findings
    datos = cargar_y_combinar_findings(ResultadoFinalTerminos, ResultadoFinalTerminosDocumento)
    ordered_combined = datos["ordered_combined"]
    findings_1 = datos["findings_1"]
    findings_2 = datos["findings_2"]
    common_findings = datos["common"]
    only_in_1 = datos["only_in_1"]
    only_in_2 = datos["only_in_2"]

    # Crear contenido Markdown para este paso
    md_lines = ["# Evaluación de equivalencias\n"]

    md_lines.append("## Comparación de Findings entre JSONs\n")

    md_lines.append("### En ambos JSONs:")
    for f in sorted(common_findings):
        md_lines.append(f"- {f}")
    print("=== Findings en ambos JSON ===")
    for f in sorted(common_findings):
        print(f"- {f}")

    md_lines.append(f"\n### Solo en {ResultadoFinalTerminos}:")
    for f in sorted(only_in_1):
        md_lines.append(f"- {f}")
    print(f"\n=== Solo en {ResultadoFinalTerminos} ===")
    for f in sorted(only_in_1):
        print(f"- {f}")

    md_lines.append(f"\n### Solo en {ResultadoFinalTerminosDocumento}:")
    for f in sorted(only_in_2):
        md_lines.append(f"- {f}")
    print(f"\n=== Solo en {ResultadoFinalTerminosDocumento} ===")
    for f in sorted(only_in_2):
        print(f"- {f}")

    md_lines.append("\n### JSON combinado de findings únicos (ordenado):")
    md_lines.append("```json")
    print("\n=== JSON combinado de findings únicos (ordenado y comentado) ===")
    print("[")
    md_lines.append("[")
    for idx, finding in enumerate(ordered_combined):
        comma = "," if idx < len(ordered_combined) - 1 else ""
        comment = " // Añadido desde la segunda pasada de los documentos" if finding in only_in_2 else ""
        linea = f'    {{"finding": "{finding}"}}{comma}{comment}'
        print(linea)
        md_lines.append(linea)
    print("]")
    md_lines.append("]")
    md_lines.append("```")

    # Guardar encabezado del Markdown
    with open(mdSalidaResumen, "w") as f_md:
        for linea in md_lines:
            f_md.write(linea + "\n")

    # === Paso 2: Cargar Gold desde CSV ===
    try:
        df_csv = pd.read_csv(csvGold)
        BList = list(dict.fromkeys(df_csv.iloc[:, 1].dropna().astype(str).tolist()))
        if not BList:
            print("⚠️ Lista B está vacía.")
    except Exception as e:
        print(f"⚠️ Error al procesar el CSV: {e}")
        BList = []

    print("\n✅ Lista B cargada:", BList)

    # === Paso 3: Obtener equivalencias con reintento
    def obtener_equivalencias(listaA, listaB, label):
        while True:
            print(f"\n🧠 Llamando a Ollama para {label}...")
            respuesta = alingTerminology(listaA, listaB, model=deepseek_r___b)
            if respuesta and es_formato_valido(respuesta):
                lineas_utiles = extraer_lineas_validas(respuesta)
                contenido_filtrado = "\n".join(lineas_utiles)
                return convertir_a_diccionario(contenido_filtrado)
            print("🔁 Respuesta inválida. Reintentando en 2 segundos...")
            time.sleep(2)

    equiv_gold_to_test = obtener_equivalencias(ordered_combined, BList, "Gold -> Test")
    equiv_test_to_test = obtener_equivalencias(ordered_combined, ordered_combined, "Test -> Test")
    equiv_gold_to_gold = obtener_equivalencias(BList, BList, "Gold -> Gold")

    # === Paso 4: Mostrar resumen
    def imprimir_equivalencias(nombre, d):
        print(f"\n✅ Equivalencias {nombre}:")
        for k, v in d.items():
            print(f"{k} -> {v}")

    imprimir_equivalencias("Gold → Test", equiv_gold_to_test)
    imprimir_equivalencias("Test → Test", equiv_test_to_test)
    imprimir_equivalencias("Gold → Gold", equiv_gold_to_gold)

    # === Paso 5: Ejecutar análisis final
    evaluar_resultado_con_equivalencias(
        json_test_file=ResultadoFinalTerminosDocumento,
        csv_gold_file=csvGold,
        equiv_gold_to_test=equiv_gold_to_test,
        equiv_test_to_test=equiv_test_to_test,
        equiv_gold_to_gold=equiv_gold_to_gold,
        output_csv=csvSalidaTabla,
        output_md=mdSalidaResumen
    )