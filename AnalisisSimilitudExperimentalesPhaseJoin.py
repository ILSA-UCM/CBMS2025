import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo de similitud
file_path = "tabla_similitud_gold_vs_experimentales.csv"
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

# Obtener estadísticas por hipótesis
stats_df = df.groupby("Hipótesis")["Similitud Coseno"].describe()

# Guardar estadísticas en CSV
stats_df.to_csv("estadisticas_similitud.csv", sep=';', encoding='utf-8')

# Generar gráficos de distribución en líneas sin efectos visuales de KDE fuera del rango
plt.figure(figsize=(10, 6))
for hypothesis in ['NN', 'DN', 'ND', 'DD']:
    subset = df[df["Hipótesis"] == hypothesis]["Similitud Coseno"]
    sns.kdeplot(subset, label=hypothesis, linewidth=2, clip=(0, 1))  # Limita la KDE al rango válido de similitud

plt.xlabel("Similitud de Coseno")
plt.ylabel("Densidad")
plt.title("Distribución de Similitud de Coseno por Hipótesis")
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()

# Mostrar estadísticas
print(stats_df)
