import pandas as pd
import matplotlib.pyplot as plt

# Load the cosine similarity file
file_path = "tabla_similitud_coseno.csv"
df_similitud = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

# Plot the distribution of similarities to evaluate the best threshold
plt.figure(figsize=(8, 6))
plt.hist(df_similitud["Similitud Coseno"], bins=30, edgecolor='black', alpha=0.7)
plt.axvline(0.7, color='r', linestyle='dashed', linewidth=1, label="Threshold 0.7")
plt.axvline(0.5, color='b', linestyle='dashed', linewidth=1, label="Threshold 0.5")
plt.axvline(0.4, color='g', linestyle='dashed', linewidth=1, label="Threshold 0.4")

plt.xlabel("Cosine Similarity")
plt.ylabel("Frequency")
plt.title("Cosine Similarity Distribution")
plt.legend()
plt.grid(axis='y', alpha=0.75)

# Show the plot
plt.show()
