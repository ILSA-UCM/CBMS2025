import json
from minnning import produceResultado

# Leer el archivo JSON desanonimizado
archivo_salida = "resultados_desanonimizados.json"
with open(archivo_salida, "r", encoding="utf-8") as f:
    datos = json.load(f)

# Crear las listas de textOri y textDesa
lista_textOri = {item["clave"]: item["textOri"] for item in datos}
lista_textDesa = {item["clave"]: item["textDesa"] for item in datos}

# Imprimir los resultados
#print("Lista de textOri:", lista_textOri)
#print("Lista de textDesa:", lista_textDesa)


ResultadoErrores=[]
ResultadoErroresRaros=[]


# Ruta del archivo
file_path = "identificadores.txt"

# Leer los identificadores desde el archivo y guardarlos en una lista
with open(file_path, "r") as f:
    identificadores = [line.strip() for line in f.readlines()]


# Suponiendo que ya tienes lista_textOri, lista_textDesa e identificadores definidos

# Filtrar lista_textOri para conservar solo las claves en identificadores
lista_textOri_filtrada = {clave: lista_textOri[clave] for clave in identificadores if clave in lista_textOri}

# Filtrar lista_textDesa para conservar solo las claves en identificadores
lista_textDesa_filtrada = {clave: lista_textDesa[clave] for clave in identificadores if clave in lista_textDesa}

#print("Lista de textOri:", lista_textOri_filtrada)
#print("Lista de textDesa:", lista_textDesa_filtrada)


# Recorrer la lista de textOri con un bucle
print("Recorriendo textOri:")

produceResultado("resultadoFinalNormal__7.json", lista_textOri_filtrada,"deepseek-r1")



# Nombre del archivo donde se guardará el JSON
archivo_salida = "resultadoErrores__7.json"

# Guardar el JSON en el archivo
with open(archivo_salida, "w", encoding="utf-8") as f:
    json.dump(ResultadoErrores, f, indent=4, ensure_ascii=False)

print(f"Errores guardados en {archivo_salida}")

# Nombre del archivo donde se guardará el JSON
archivo_salida = "resultadoErroresRaros__7.json"

# Guardar el JSON en el archivo
with open(archivo_salida, "w", encoding="utf-8") as f:
    json.dump(ResultadoErroresRaros, f, indent=4, ensure_ascii=False)

print(f"Errores guardados en {archivo_salida}")
