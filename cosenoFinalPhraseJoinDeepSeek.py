import pandas as pd
from ollama import Client
import json
import re


def verificar_similitud_deepseek(gold_text, hypothesis_text):
    client = Client(host='http://localhost:11434')
    intento = 1
    while intento <= 10:  # Limitar intentos a 10
        prompt = f"""
            Compare the following two phrases and determine if they express the same medical findings or deseases.
            Respond only with "SI" or "NO".

            ### Phrase 1:
            "{gold_text}"

            ### Phrase 2:
            "{hypothesis_text}"

            ### Output format:
            - Only "SI" if they have the same meaning.
            - Only "NO" if they do not have the same meaning.
        """

        response = client.chat(model='deepseek-r1', messages=[{'role': 'user', 'content': prompt}])
        if response:
            result = response['message']['content']
            result = re.sub(r'<think>.*?</think>', '', result,
                            flags=re.DOTALL).strip().upper()  # Quitar <think> y limpiar espacios
            print(f"G:{gold_text}  H:{hypothesis_text} " + result)
            if result in ["SI", "NO"]:
                return result

        prompt += "\n The response was not valid. Please answer strictly with 'SI' or 'NO'."
        intento += 1

    return "ERROR: No valid response after 10 attempts."


def format_terms(terms):
    if not terms:
        return "Normal"
    elif len(terms) == 1:
        return terms[0]
    else:
        return ", ".join(terms[:-1]) + " and " + terms[-1]


# Cargar archivo CSV procesado
file_path = "Resumen_GOLD_procesado_CHGPT.csv"
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

# Crear tabla de comparación
comparison_results = []

for _, row in df.iterrows():
    gold_text = format_terms(row["Gold"].split('|'))

    for hyp_col in ['NN', 'DN', 'ND', 'DD']:
        hypothesis_text = format_terms(row[hyp_col].split('|'))
        result = verificar_similitud_deepseek(gold_text, hypothesis_text)

        comparison_results.append({
            'ID': row['ID'],
            'Hipótesis': hyp_col,
            'Texto Hipótesis': hypothesis_text,
            'Texto Gold': gold_text,
            'Similitud': result
        })

# Guardar la tabla de comparaciones en CSV
comparison_df = pd.DataFrame(comparison_results)
comparison_df.to_csv("tabla_comparacion_gold_vs_experimentales_ds.csv", index=False, encoding='utf-8', sep=';')

# Mostrar resultados
print(comparison_df.head())

