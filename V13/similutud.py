import json
import re
from ollama import Client


# === Función para cargar y combinar findings de dos archivos JSON ===
def cargar_y_combinar_findings(archivo_json1, archivo_json2):
    with open(archivo_json1, "r") as f1:
        json1 = json.load(f1)

    with open(archivo_json2, "r") as f2:
        json2 = json.load(f2)

    findings_1 = set(entry["finding"].strip().lower() for entry in json1)

    findings_2 = set()
    for entry in json2:
        for anotado in entry.get("anotado", []):
            finding = anotado.get("finding")
            if finding:
                findings_2.add(finding.strip().lower())

    common = findings_1 & findings_2
    only_1 = findings_1 - findings_2
    only_2 = findings_2 - findings_1
    combinados = sorted(findings_1) + sorted(only_2)

    return {
        "ordered_combined": combinados,
        "findings_1": findings_1,
        "findings_2": findings_2,
        "common": common,
        "only_in_1": only_1,
        "only_in_2": only_2,
    }

def extraer_lineas_validas(respuesta):
    patron = re.compile(r"^.+\s*->(\s*.+)?$")
    lineas_validas = []
    for linea in respuesta.strip().split('\n'):
        linea = linea.strip()
        if patron.match(linea):
            lineas_validas.append(linea)
    return lineas_validas

# Valida si hay al menos una línea válida
def es_formato_valido(respuesta):
    lineas = extraer_lineas_validas(respuesta)
    return len(lineas) > 0

# === Alinea Terminologias ===
def alingTerminology(AList, BList, model, host="http://localhost:11434"):
    try:
        client = Client(host=host)
    except Exception as e:
        print(f"❌ Error al conectarse a Ollama: {e}")
        return None

    if AList != BList:
        first_terminology = '\n'.join(AList)
        second_terminology = '\n'.join(BList)
        content_text = f"""
You must align two medical terminologies, which use different terms.

First terminology:
{first_terminology}

Second terminology:
{second_terminology}

For each term X in the second terminology, you must provide those terms Y in the first terminology such that X and Y have similar meanings. The output should consist of lines of the form X -> Y,Z,K,.... If no similar terms exist, use X ->. Only generate the output.
"""
    else:
        first_terminology = '\n'.join(AList)
        content_text = f"""
You must determine terms with similar meanings in the following terminology:

{first_terminology}

For each term X, generate X -> Y,Z,K,... for related terms, or X -> if none. Only generate the output.
"""

    try:
        response = client.chat(model=model, messages=[
            {'role': 'user', 'content': content_text},
        ])
        return response['message']['content'].strip()
    except Exception as e:
        print(f"❌ Error en llamada a Ollama: {e}")
        return None

def limpiar_termino(texto):
    """
    Limpia un término eliminando numeraciones, guiones, asteriscos y espacios.
    """
    texto = texto.replace("*", "")
    texto = re.sub(r"^\s*[\d]+\.\s*", "", texto)  # elimina "1. "
    texto = re.sub(r"^\s*-\s*", "", texto)        # elimina "- "
    return texto.strip()

def convertir_a_diccionario(texto):
    dic = {}
    for linea in texto.strip().split('\n'):
        if '->' in linea:
            origen_raw, destino_raw = linea.split('->', 1)
            origen = limpiar_termino(origen_raw)
            destino = [limpiar_termino(x) for x in destino_raw.strip().split(',') if x.strip()]
            dic[origen] = destino
    return dic

