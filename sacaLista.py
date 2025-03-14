import json
# Cargar los datos del archivo resultadoFinalNormal.json
with open('resultadoFinalNormal.json', 'r') as file:
    findings_data = json.load(file)

# Segundo término: findings del archivo resultadoFinalNormal.json
second_terminology = [item["finding"] for item in findings_data]

print('\n'.join(second_terminology))