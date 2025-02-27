import pandas as pd
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load JSON files
with open("resultadoFinalAnnon.json", "r", encoding="utf-8") as f:
    annon_findings = [item["finding"] for item in json.load(f)]

with open("resultadoFinalNormal.json", "r", encoding="utf-8") as f:
    normal_findings = [item["finding"] for item in json.load(f)]

# Determine the smaller and larger list
if len(annon_findings) < len(normal_findings):
    smaller_list = annon_findings
    larger_list = normal_findings
else:
    smaller_list = normal_findings
    larger_list = annon_findings

# Load semantic model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode findings
smaller_embeddings = model.encode(smaller_list)
larger_embeddings = model.encode(larger_list)

# Compute cosine similarities
similarity_results = []
for idx_s, s_emb in enumerate(smaller_embeddings):
    similarities = cosine_similarity([s_emb], larger_embeddings).flatten()
    for idx_l, similarity in enumerate(similarities):
        similarity_results.append({
            'Smaller Term': smaller_list[idx_s],
            'Larger Term': larger_list[idx_l],
            'Cosine Similarity': similarity
        })

# Save similarity table to CSV
similarity_df = pd.DataFrame(similarity_results)
similarity_df.to_csv("similarity_comparison.csv", index=False, encoding='utf-8', sep=';')

# Print first few rows
print(similarity_df.head())
