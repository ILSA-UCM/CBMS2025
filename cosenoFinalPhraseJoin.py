import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Cargar archivo CSV procesado
file_path = "Resumen_GOLD_procesado_CHGPT.csv"
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

# Modelo semántico
model = SentenceTransformer('all-MiniLM-L6-v2')


# Convertir términos en texto formateado
def format_terms(terms):
    if not terms:
        return "Normal"
    elif len(terms) == 1:
        return terms[0]
    else:
        return ", ".join(terms[:-1]) + " and " + terms[-1]


# Crear tabla de similitud
similarity_results = []

for _, row in df.iterrows():
    gold_text = format_terms(row["Gold"].split('|'))
    gold_embedding = model.encode([gold_text])

    for hyp_col in ['NN', 'DN', 'ND', 'DD']:
        hypothesis_text = format_terms(row[hyp_col].split('|'))
        hypothesis_embedding = model.encode([hypothesis_text])

        similarity = cosine_similarity(hypothesis_embedding, gold_embedding)[0][0]

        similarity_results.append({
            'ID': row['ID'],
            'Hipótesis': hyp_col,
            'Texto Hipótesis': hypothesis_text,
            'Texto Gold': gold_text,
            'Similitud Coseno': similarity
        })

# Guardar la tabla de similitudes en CSV
similarity_df = pd.DataFrame(similarity_results)
similarity_df.to_csv("tabla_similitud_gold_vs_experimentales.csv", index=False, encoding='utf-8', sep=';')

# Mostrar resultados
print(similarity_df.head())
