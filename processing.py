import re
from ollama import Client
import json


def obtener_respuesta(valor_texto, model, historial_mensajes=[], jsonIni={}, resultadoAgregado="",
                      host="http://localhost:11434"):
    try:
        client = Client(host=host)
    except Exception as e:
        print(f"Error conectarse a la API de OLLAAMA: {e}")
        return None

    content_text = (
        f"""Extract all **clinically relevant findings and diseases** from the following medical text.

        Return **only** a valid JSON array, ensuring that only **clinically significant findings and diseases** are included, while excluding general observations, normal findings, and anatomical descriptions.

        ### Input:
        1. `jsonIni`: {jsonIni}  # List of findings and diseases to find.
        2. Text to analyze:
           {valor_texto}

        ### Output format:
        - Each object in the JSON array must include:
          - `"finding"`: the **clinically significant finding or disease** identified in the text.

        ### Important:
        - Ensure all values are **clinically relevant**.
        - Exclude **normal findings**, general descriptions, and anatomical observations such as:
          - "Unremarkable structures"
          - "Normal appearance"
          - "No abnormalities detected"
          - "Mild age-related changes"
          - "Typical anatomy"
          - "Absent Findings"
        - Maintain lowercase `"true"` for boolean values.
        - **DO NOT** include any explanations, code, or additional text—return **only** the JSON array."""
    )

    # print(content_text)

    response = client.chat(model=model, messages=[
        {
            'role': 'user',
            'content': content_text + " " + resultadoAgregado,
        },
    ])

    if response:
        historial_mensajes.append({
            'role': 'assistant',
            'content': response['message']['content']
        })
        # print(response)
        return historial_mensajes, response
    else:
        #  print("No se recibió respuesta")
        return None


def extract_json(text):
    try:
        # Busca cualquier bloque de texto que parezca un JSON (entre corchetes o llaves)
        json_match = re.search(r'(\[.*?\]|\{.*?\})', text, re.DOTALL)
        if json_match:
            json_text = json_match.group(0)
            # print("jsonfound->",json_text)
            # Intenta cargarlo como un objeto JSON
            parsed_json = json.loads(json_text)
            return parsed_json
        else:
            # print("No se encontró un JSON en el texto.")
            return None
    except json.JSONDecodeError as e:
        # print(f"Error al decodificar JSON: {e}")
        return fix_json_with_ollama(json_text)

def fix_json_with_ollama(json_text,host="http://localhost:11434"):
    """
    Función para verificar y reparar un JSON usando Ollama.
    """
    try:
        # Primero, intenta cargar el JSON directamente
        return json.loads(json_text)
    except json.JSONDecodeError:
        # print("JSON no válido. Usando Ollama para repararlo...")
        pass

    client = Client(host=host)

    # Formatear el prompt para Ollama
    prompt = f"""
        The following text is supposed to be a JSON, but it may have issues. 
        Please validate, fix it, and return the corrected JSON only:

        {json_text}
    """

    # Ejecutar el modelo de Ollama
    response = client.chat(model='qwen2.5-coder:0.5b', messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])

    # Procesar la salida
    json_response = response['message']['content'].strip()
    try:
        # Intentar decodificar el JSON reparado
        return json.loads(json_response)
    except json.JSONDecodeError:
        #  print("No se pudo reparar el JSON con Ollama.")
        #  print(json_text)
        return None


def intentoBase(textOri,model, historial_mensajes, resultadoJSONAnnon, resultadoA):
    historial_mensajes, resultadoAnon = obtener_respuesta(textOri,model,
                                                          historial_mensajes,
                                                          resultadoJSONAnnon, resultadoA)
    # print(f"Historial_mensajes: {historial_mensajes}")
    # print(f"Texto resultadoAnon: {resultadoAnon['message']['content']}")
    resultadoJSONAnnon2 = extract_json(resultadoAnon['message']['content'])
    return resultadoJSONAnnon2, resultadoAnon['message']['content']

def es_formato_valido(clave, texto, resultado):
    if not isinstance(resultado, list):
        return False
    for entry in resultado:
        if not isinstance(entry, dict):
            return False
        if 'finding' not in entry:
            return False
    return True

def procesaResultado(diccionario_textOri, jsonInitialFindings, identificadores, model):
    ResultadoSalida = []
    ResultadoErrores = []
    historial_mensajes = []
    errorAgregado = f"""El JSON No esta bien formado o no contiene al menos la lista inicial."""
    for clave, textOri in diccionario_textOri.items():

        if clave in identificadores:

            resultadoJSONAnnonUni = None
            errorAgregadoA = ""

            while resultadoJSONAnnonUni is None:

                resultadoJSONAnnonUni, resultadoContent = intentoBase(textOri,model, historial_mensajes,
                                                                      jsonInitialFindings, errorAgregadoA)

                if resultadoJSONAnnonUni is None or not es_formato_valido(clave, textOri, resultadoJSONAnnonUni):
                    errorAgregadoA = errorAgregado
                    resultadoJSONAnnonUni = None


            if resultadoJSONAnnonUni is not None:
                dictvalor = dict();
                dictvalor["clave"] = clave
                dictvalor["texto"] = textOri
                dictvalor["anotado"] = resultadoJSONAnnonUni
                ResultadoSalida.append(dictvalor)
                print("Case", clave, "Result", resultadoJSONAnnonUni)

    return ResultadoSalida, ResultadoErrores


def salvarSalida(ResultadoSalida, ResultadoErrores, archivo_salida, archivo_salidaE):
    # Guardar el JSON en el archivo
    with open(archivo_salida, "w", encoding="utf-8") as f:
        json.dump(ResultadoSalida, f, indent=4, ensure_ascii=False)

    print(f"JSON guardado en {archivo_salida}")

    # Guardar el JSON en el archivo
    with open(archivo_salidaE, "w", encoding="utf-8") as f:
        json.dump(ResultadoErrores, f, indent=4, ensure_ascii=False)

    print(f"JSON guardado en {archivo_salidaE}")
