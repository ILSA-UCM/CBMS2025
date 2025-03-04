import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "estadisticas_similitud.csv"
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

# Remove the 'count' column if it exists
df = df.drop(columns=['count','max'], errors='ignore')

# Round numerical values to 3 decimal places
df = df.round(3)

# Function to plot a table with Matplotlib
def plot_table(df, title):
    fig, ax = plt.subplots(figsize=(8, 2))  # Adjust size for better readability
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width([i for i in range(len(df.columns))])  # Adjust column width automatically
    plt.subplots_adjust(top=0.85, bottom=0.15)  # Reduce space between title and table
    plt.title(title, fontsize=10, pad=0)  # Title as close as possible to the table
    plt.show()

# Plot the statistics table
plot_table(df, "Statistics of Cosine Similarity")
