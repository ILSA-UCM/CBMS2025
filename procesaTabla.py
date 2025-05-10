import pandas as pd

def procesar_archivo_csv(file_path):
    # Leer el archivo CSV
    df = pd.read_csv(file_path)

    # Columnas que sí queremos procesar separando términos
    columnas_a_procesar = [
        'Test', 'Gold', 'Test expandido', 'Gold expandido',
        'Mapeado Gold→Test', 'Coincidencias (Gold original)'
    ]

    # Iterar fila por fila
    for index, row in df.iterrows():
        print(f"\n--- Fila {index + 1} ---")
        print(f"ID: {row['numeroID']}")
        print(f"Texto: {row['Texto']}\n")

        # Procesar solo las columnas indicadas
        for col in columnas_a_procesar:
            if col in df.columns:
                valor = row[col]
                if pd.notna(valor):
                    # Separar términos, limpiar espacios, ordenar alfabéticamente
                    terminos = [term.strip() for term in str(valor).split(',') if term.strip()]
                    terminos_ordenados = sorted(terminos, key=lambda x: x.lower())

                    print(f"Columna: {col}")
                    for termino in terminos_ordenados:
                        print(f" - {termino}")

        input("\nPulsa ENTER para continuar...")

if __name__ == "__main__":
 #   archivo = input("Introduce la ruta del archivo CSV: ").strip()
    archivo="resultadoTabla__70.csv"
    procesar_archivo_csv(archivo)

