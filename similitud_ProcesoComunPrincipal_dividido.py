from similutud import (cargar_y_combinar_findings,
                       alingTerminology,
                       convertir_a_diccionario,
                       extraer_lineas_validas,
                       es_formato_valido)
from similitud_analisis import evaluar_resultado_con_equivalencias


import time
import pandas as pd
import json
import os


def guardar_si_no_existe(diccionario, ruta):
    if os.path.exists(ruta):
        print(f"📁 Archivo '{ruta}' ya existe. Se conserva sin sobrescribir.")
    else:
        with open(ruta, "w") as f:
            json.dump(diccionario, f, indent=2)
        print(f"✅ Archivo '{ruta}' guardado correctamente.")

def generar_equivalencias_y_guardar(
    ResultadoFinalTerminos,
    ResultadoFinalTerminosDocumento,
    csvGold,
    deepseek_r___b,
    mdSalidaResumen,
    salida_gold_to_test,
    salida_test_to_test,
    salida_gold_to_gold
):
    # Paso 1: cargar findings y generar markdown de comparación
    datos = cargar_y_combinar_findings(ResultadoFinalTerminos, ResultadoFinalTerminosDocumento)
    ordered_combined = datos["ordered_combined"]
    findings_1 = datos["findings_1"]
    findings_2 = datos["findings_2"]
    common_findings = datos["common"]
    only_in_1 = datos["only_in_1"]
    only_in_2 = datos["only_in_2"]

    md_lines = ["# Evaluación de equivalencias\n", "## Comparación de Findings entre JSONs\n"]

    md_lines.append("### En ambos JSONs:")
    for f in sorted(common_findings):
        md_lines.append(f"- {f}")

    md_lines.append(f"\n### Solo en {ResultadoFinalTerminos}:")
    for f in sorted(only_in_1):
        md_lines.append(f"- {f}")

    md_lines.append(f"\n### Solo en {ResultadoFinalTerminosDocumento}:")
    for f in sorted(only_in_2):
        md_lines.append(f"- {f}")

    md_lines.append("\n### JSON combinado de findings únicos (ordenado):")
    md_lines.append("```json")
    md_lines.append("[")
    for idx, finding in enumerate(ordered_combined):
        comma = "," if idx < len(ordered_combined) - 1 else ""
        comment = " // Añadido desde la segunda pasada de los documentos" if finding in only_in_2 else ""
        md_lines.append(f'    {{"finding": "{finding}"}}{comma}{comment}')
    md_lines.append("]")
    md_lines.append("```")


    # Paso 2: cargar CSV Gold
    df_csv = pd.read_csv(csvGold)
    BList = list(dict.fromkeys(df_csv.iloc[:, 1].dropna().astype(str).tolist()))

    # === Agregar impresión y markdown de BList con anotaciones ===
    md_lines.append("\n## Lista Gold \n")
    md_lines.append("```json")
    md_lines.append("[")

    for idx, finding in enumerate(BList):
        comma = "," if idx < len(BList) - 1 else ""
        linea = f'    {{"finding": "{finding}"}}{comma}'
        print(linea)
        md_lines.append(linea)

    md_lines.append("]")
    md_lines.append("```")

    # Paso 3: función con reintento (solo si archivo no existe)
    def obtener_equivalencias_si_no_existe(listaA, listaB, label, ruta_json):
        if os.path.exists(ruta_json):
            print(f"📁 Equivalencia '{label}' ya existe en {ruta_json}, no se regenera.")
            with open(ruta_json, "r") as f:
                return json.load(f)
        else:
            while True:
                print(f"\n🧠 Llamando a Ollama para {label}...")
                respuesta = alingTerminology(listaA, listaB, model=deepseek_r___b)
                if respuesta and es_formato_valido(respuesta):
                    lineas_utiles = extraer_lineas_validas(respuesta)
                    contenido_filtrado = "\n".join(lineas_utiles)
                    dic = convertir_a_diccionario(contenido_filtrado)
                    guardar_si_no_existe(dic, ruta_json)
                    return dic
                print("🔁 Respuesta inválida. Reintentando en 2 segundos...")
                time.sleep(2)

    md_lines.append("# Calculo de similitud\n")
    # Paso 4: obtener los 3 equivalentes
    equiv_gold_to_test = obtener_equivalencias_si_no_existe(
        ordered_combined, BList, "Gold -> Test", salida_gold_to_test
    )

    equiv_test_to_test = obtener_equivalencias_si_no_existe(
        ordered_combined, ordered_combined, "Test -> Test", salida_test_to_test
    )

    equiv_gold_to_gold = obtener_equivalencias_si_no_existe(
        BList, BList, "Gold -> Gold", salida_gold_to_gold
    )

    # Añadir equivalencias al markdown
    def dump_dict_md(title, d):
        md_lines.append(f"\n## Equivalencias: {title}")
        for k in sorted(d):
            v = ", ".join(sorted(d[k]))
            md_lines.append(f"- {k} -> {v}")

    dump_dict_md("Gold → Test", equiv_gold_to_test)
    dump_dict_md("Test → Test", equiv_test_to_test)
    dump_dict_md("Gold → Gold", equiv_gold_to_gold)

    # Vuelve a guardar el markdown actualizado
    with open(mdSalidaResumen, "w", encoding='utf-8') as f_md:
        for line in md_lines:
            f_md.write(line + "\n")

    print("✅ Equivalencias generadas o cargadas correctamente.")


def evaluar_desde_archivos(
    ResultadoFinalTerminosDocumento,
    csvGold,
    archivo_equiv_gold_to_test,
    archivo_equiv_test_to_test,
    archivo_equiv_gold_to_gold,
    csvSalidaTabla,
    mdSalidaResumen
):
    # Cargar diccionarios desde JSON
    with open(archivo_equiv_gold_to_test, "r") as f:
        equiv_gold_to_test = json.load(f)
    with open(archivo_equiv_test_to_test, "r") as f:
        equiv_test_to_test = json.load(f)
    with open(archivo_equiv_gold_to_gold, "r") as f:
        equiv_gold_to_gold = json.load(f)

    # Ejecutar evaluación
    evaluar_resultado_con_equivalencias(
        json_test_file=ResultadoFinalTerminosDocumento,
        csv_gold_file=csvGold,
        equiv_gold_to_test=equiv_gold_to_test,
        equiv_test_to_test=equiv_test_to_test,
        equiv_gold_to_gold=equiv_gold_to_gold,
        output_csv=csvSalidaTabla,
        output_md=mdSalidaResumen
    )
