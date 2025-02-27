import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
file_path_05 = "metricas_precision_recall_f1_completas_0.5.csv"
file_path_07 = "metricas_precision_recall_f1_completas_0.7.csv"

df_05 = pd.read_csv(file_path_05, delimiter=';', encoding='utf-8')
df_07 = pd.read_csv(file_path_07, delimiter=';', encoding='utf-8')

# Function to plot a table with Matplotlib
def plot_table(df, title):
    fig, ax = plt.subplots(figsize=(8, 1.5))  # Reduce height to minimize space
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width([i for i in range(len(df.columns))])  # Adjust column width automatically
    plt.subplots_adjust(top=0.85, bottom=0.15)  # Reduce space between title and table
    plt.title(title, fontsize=10, pad=0)  # Title as close as possible to the table
    plt.show()

# Plot the tables with English labels
plot_table(df_05, "Metrics for Threshold 0.5")
plot_table(df_07, "Metrics for Threshold 0.7")
