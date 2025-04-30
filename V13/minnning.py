from ollama import Client
import re
import json


# Lista para almacenar el historial de conversación


def obtener_respuesta(valor_texto,model,
                      historial_mensajes=[], jsonIni={}, error="",
                      host= 'http://localhost:11434'):
    try:
        client = Client(host=host)
    except Exception as e:
        print(f"Error conectarse a la API de OLLAAMA: {e}")
        return None

    content_text = (
        f"""Extract all **clinically relevant findings and diseases** from the following medical text.

Return **only** a valid JSON array, merging the findings with the existing list in `jsonIni`, ensuring that:
- **No duplicate terms** are included.
- **Only medically relevant findings and diseases** are extracted.
- **Irrelevant terms, normal findings, and anatomical descriptions are excluded**.

### Input:
1. `jsonIni`: {jsonIni}  # Initial list of findings and diseases.
2. Text to analyze:
   {valor_texto}

### Output format:
- Each object in the JSON array must include:
  - `"finding"`: the **clinically significant finding or disease** identified in the text.

### Expected Output Format:
    [
        {{"finding": "hyperinflated lungs"}},
        {{"finding": "flattened diaphragm"}},
        {{"finding": "increased retrosternal airspace"}},
        {{"finding": "pulmonary edema due to acute respiratory distress syndrome (ARDS)"}},
        {{"finding": "spine dextrocurvature"}},
        {{"finding": "bronchiectasis"}},
        {{"finding": "fibrotic scarring"}},
        {{"finding": "infiltrate in the right middle lobe"}},
        {{"finding": "lumbar degenerative disc disease"}}
    ]

### Important:
- **Ensure all values are clinically relevant.**
- **Exclude** general observations, normal findings, and anatomical descriptions such as:
  - "Unremarkable structures"
  - "Normal appearance"
  - "No abnormalities detected"
  - "Mild age-related changes"
  - "Typical anatomy"
  - "No significant pathology"
- Maintain lowercase `"true"` for boolean values.
- **DO NOT** include any explanations, code, or additional text—return **only** the JSON array.
- **DO NOT** include any explanations, code, or additional text—return **only** the JSON array.
- **DO NOT** include any explanations, code, or additional text—return **only** the JSON array."""
    )

    if len(error)>0:
        content_text = error +". "+content_text
    #print(content_text)

    response = client.chat(model=model, messages=historial_mensajes+
    [
        {
            'role': 'user',
            'content': content_text,
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
            #print("jsonfound->",json_text)
            # Intenta cargarlo como un objeto JSON
            parsed_json = json.loads(json_text)

            if isinstance(parsed_json, list) and all(
                    isinstance(item, dict) and "finding" in item for item in parsed_json
            ):
                return parsed_json

        else:
            # print("No se encontró un JSON en el texto.")
            return None
    except json.JSONDecodeError as e:
        # print(f"Error al decodificar JSON: {e}")
        return fix_json_with_ollama(json_text)


import subprocess


def fix_json_with_ollama(json_text,
                      host= 'http://localhost:11434'):
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
    The following text is supposed to be a JSON array containing only clinically relevant findings.

    ### Expected Output Format:
    [
        {{"finding": "hyperinflated lungs"}},
        {{"finding": "flattened diaphragm"}},
        {{"finding": "increased retrosternal airspace"}},
        {{"finding": "pulmonary edema due to acute respiratory distress syndrome (ARDS)"}},
        {{"finding": "spine dextrocurvature"}},
        {{"finding": "bronchiectasis"}},
        {{"finding": "fibrotic scarring"}},
        {{"finding": "infiltrate in the right middle lobe"}},
        {{"finding": "lumbar degenerative disc disease"}}
    ]

    ### Instructions:
    - **Return only a JSON array of objects**, where each object contains a **single key**: `"finding"`.
    - **Remove extra keys such as `"description"`, `"category"`, or any other unwanted attributes.**
    - **Ensure the JSON is valid and properly formatted.**
    - **If the input JSON is invalid or contains unnecessary data, correct it while maintaining only the `"finding"` structure.**
    - **Do not include explanations, code, or formatting outside of the JSON array.**

    ### Input JSON:
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

def intentoBase(textOri,model,historial_mensajes,resultadoJSONAnnon,error=""):
    if resultadoJSONAnnon is not None:
        historial_mensajes, resultadoAnon = obtener_respuesta(textOri, model,
                                                              historial_mensajes, resultadoJSONAnnon, error)
    else :
        historial_mensajes, resultadoAnon = obtener_respuesta(textOri,model,
                                                              historial_mensajes, error=error)

   # print(f"Historial_mensajes: {historial_mensajes}")
   # print(f"Texto resultadoAnon: {resultadoAnon['message']['content']}")
    resultadoJSONAnnon2 = extract_json(resultadoAnon['message']['content'])
    return resultadoJSONAnnon2, resultadoAnon['message']['content']


def produceResultado(archivo_salida,lista,model):
    historial_mensajes = []
    resultadoJSONAnnon = []
    errorAgregado = f"""El JSON No esta bien formado o no contiene al menos la lista inicial."""
    print(lista)
    for item,value in lista.items():

            clave = item
            textOri =value
            print(f"DocX: {clave}")

            resultadoJSONAnnonUni = None
            errorAgregadoA = ""

            while resultadoJSONAnnonUni is None:
                resultadoJSONAnnonUni, resultadoContent = intentoBase(textOri,model,
                                                                      historial_mensajes, resultadoJSONAnnon,errorAgregadoA)

                if resultadoJSONAnnonUni is not None and contiene_todos_los_tags(resultadoJSONAnnon,
                                                                                 resultadoJSONAnnonUni):
                    resultadoJSONAnnon = resultadoJSONAnnonUni

                if resultadoJSONAnnonUni is None:
                    errorAgregadoA = errorAgregado



            # print(f"Texto Original: {textOri}")
            print(f"Texto JSON: {resultadoJSONAnnon}")
            print("---")

    print(f"Texto JSON Final: {resultadoJSONAnnon}")


    # Guardar el JSON en el archivo
    with open(archivo_salida, "w", encoding="utf-8") as f:
        json.dump(resultadoJSONAnnon, f, indent=4, ensure_ascii=False)

    print(f"JSON guardado en {archivo_salida}")

def contiene_todos_los_tags(previo, nuevo):
    if not previo:
        return True  # Si la lista previa está vacía, acepta cualquier nueva lista válida
    set_previos = {item["finding"] for item in previo}
    set_nuevos = {item["finding"] for item in nuevo}
    return set_previos.issubset(set_nuevos)
