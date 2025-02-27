import pandas as pd
import json
import matplotlib.pyplot as plt
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

# Compute cosine similarities and check inclusion for multiple thresholds
thresholds = [0.7, 0.5]
inclusion_percentages = {}
similarity_results = []

for idx_s, s_emb in enumerate(smaller_embeddings):
    similarities = cosine_similarity([s_emb], larger_embeddings).flatten()
    best_match_idx = similarities.argmax()
    max_similarity = similarities[best_match_idx]

    # Save all cosine similarities in the table
    for idx_l, similarity in enumerate(similarities):
        similarity_results.append({
            'Smaller Term': smaller_list[idx_s],
            'Larger Term': larger_list[idx_l],
            'Cosine Similarity': similarity,
            'Passes 0.7': similarity >= 0.7,
            'Passes 0.5': similarity >= 0.5
        })

    # Count inclusion for each threshold
    for threshold in thresholds:
        if max_similarity >= threshold:
            inclusion_percentages.setdefault(threshold, 0)
            inclusion_percentages[threshold] += 1

# Calculate final inclusion percentages
for threshold in thresholds:
    inclusion_percentages[threshold] = (inclusion_percentages[threshold] / len(smaller_list)) * 100

# Save similarity table to CSV
similarity_df = pd.DataFrame(similarity_results)
similarity_df.to_csv("similarity_comparison.csv", index=False, encoding='utf-8', sep=';')

# Generate similarity distribution plot
plt.figure(figsize=(8, 6))
plt.hist(similarity_df["Cosine Similarity"], bins=30, edgecolor='black', alpha=0.7)
plt.axvline(0.7, color='r', linestyle='dashed', linewidth=1, label="Threshold 0.7")
plt.axvline(0.5, color='b', linestyle='dashed', linewidth=1, label="Threshold 0.5")
plt.xlabel("Cosine Similarity")
plt.ylabel("Frequency")
plt.title("Distribution of Cosine Similarities")
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()

# Print results for different thresholds
for threshold, percentage in inclusion_percentages.items():
    print(
        f"{percentage:.2f}% of the smaller list is included in the larger list based on a similarity threshold of {threshold}.")
