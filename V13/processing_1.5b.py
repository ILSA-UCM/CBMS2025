import json
from processing import salvarSalida, procesaResultado


# Leer el archivo JSON desanonimizado
archivo_salida = "resultados_desanonimizados.json"
with open(archivo_salida, "r", encoding="utf-8") as f:
    datos = json.load(f)

# Crear las listas de textOri y textDesa
# Crear los dos diccionarios
diccionario_textOri = {item["clave"]: item["textOri"] for item in datos}
diccionario_textDesa = {item["clave"]: item["textDesa"] for item in datos}

# Imprimir los resultados
# print("Lista de textOri:", lista_textOri)
# print("Lista de textDesa:", lista_textDesa)


# Ruta del archivo
file_path = "identificadores.txt"

# Leer los identificadores desde el archivo y guardarlos en una lista
with open(file_path, "r") as f:
    identificadores = [line.strip() for line in f.readlines()]

# Leer el archivo JSON etiquetas
archivo_salidaNormal = "resultadoFinalNormal.json"
with open(archivo_salidaNormal, "r", encoding="utf-8") as f:
    datos = json.load(f)

# Crear las listas de listaFindings
listaFindings = [objeto["finding"] for objeto in datos]

print("Recorriendo ORI:ORI:")

# Text ORIGINAL contra lista ORIGINAL
ResultadoSalidaNormalNormal, ResultadoErrores = (
    procesaResultado(diccionario_textOri, listaFindings, identificadores, "deepseek-r1:1.5b"))

# Nombre del archivo donde se guardará el JSON
archivo_salida = "resultadoFinalNormalDocNN__1_5.json"

# Nombre del archivo donde se guardará el JSON
archivo_salidaE = "resultadoFinalNormalDocENN__1_5.json "

salvarSalida(ResultadoSalidaNormalNormal, ResultadoErrores, archivo_salida, archivo_salidaE)


