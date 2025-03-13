import json
from ollama import Client

def desanonimizar_informe_medico(AList, BList, filename):
    try:
        client = Client(host='http://localhost:11434')
    except Exception as e:
        print(f"Error al conectarse a la API de OLLAMA: {e}")
        return None

    # Formatear las listas en el contenido del texto
    first_terminology = '\n'.join(AList)
    second_terminology = '\n'.join(BList)

    # Instrucción ajustada
    content_text = (
        f"""You must align two medical terminologies, which use different terms. 

First terminology:
{first_terminology}


Second terminology:
{second_terminology}


For each term X in the second terminology, you must provide those terms Y in the first terminology such that X and Y have similar meanings. The output should consist of lines of the form X -> Y,Z,K,.... where X is a term in the second terminology, and Y,Z,K are terms in the first terminology with similar meanings to X. If there is no term in the first terminology similar to X, X -> (with the right part empty) will appear. In the answer, there will be one line for each term in the second terminology. Generate only the requested output, omitting any other additional text (i.e., explanations, examples, etc.).
"""
    )

    # Guardar el contenido en el archivo especificado
    with open(filename, 'w') as f:
        f.write(content_text)

    # Enviar la solicitud al modelo
    response = client.chat(model='deepseek-r1:70b', messages=[
        {
            'role': 'user',
            'content': content_text,
        },
    ])

    if response:
        return response['message']['content']
    else:
        print("Error al obtener respuesta del modelo.")
        return None




# Cargar los datos del archivo resultadoFinalNormal.json
with open('/mnt/data/resultadoFinalNormal.json', 'r') as file:
    findings_data = json.load(file)

# Cargar los datos del archivo reports.json
with open('/mnt/data/reports.json', 'r') as file:
    reports_data = json.load(file)


# Primer término: GOLD del archivo reports.json
first_terminology = set()
for report in reports_data:
    gold = report["Gold"]
    if isinstance(gold, list):
        first_terminology.update(gold)
    else:
        first_terminology.add(gold)

# Segundo término: findings del archivo resultadoFinalNormal.json
second_terminology = [item["finding"] for item in findings_data]

desanonimizar_informe_medico(first_terminology,first_terminology, "gold_gold.py")

desanonimizar_informe_medico(second_terminology,second_terminology, "ds_ds.py")

desanonimizar_informe_medico(first_terminology,second_terminology, "gold_ds.py")


