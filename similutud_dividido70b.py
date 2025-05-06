from similitud_ProcesoComunPrincipal_dividido import (
        generar_equivalencias_y_guardar,
        evaluar_desde_archivos)


ResultadoFinalTerminos="resultadoFinalNormal__70.json"
ResultadoFinalTerminosDocumento="resultadoFinalNormalDocNN__70.json"
csvGold = "20250430_9e5995.csv"
deepseek_r___b = "deepseek-r1:70b"
csvSalidaTabla = "resultadoTabla__70.csv"
mdSalidaResumen = "resultadoResumen__70.md"
equiv_gold_to_test = "salida_gold_to_test__70.json"
equiv_test_to_test = "salida_test_to_test__70.json"
equiv_gold_to_gold = "salida_gold_to_gold__70.json"



generar_equivalencias_y_guardar(
    ResultadoFinalTerminos=ResultadoFinalTerminos,
    ResultadoFinalTerminosDocumento=ResultadoFinalTerminosDocumento,
    csvGold=csvGold,
    deepseek_r___b=deepseek_r___b,
    mdSalidaResumen=mdSalidaResumen,
    salida_gold_to_test=equiv_gold_to_test,
    salida_test_to_test=equiv_test_to_test,
    salida_gold_to_gold=equiv_gold_to_gold
)

evaluar_desde_archivos(
        ResultadoFinalTerminosDocumento=ResultadoFinalTerminosDocumento,
        csvGold=csvGold,
        archivo_equiv_gold_to_test=equiv_gold_to_test,
        archivo_equiv_test_to_test=equiv_test_to_test,
        archivo_equiv_gold_to_gold=equiv_gold_to_gold,
        csvSalidaTabla=csvSalidaTabla,
        mdSalidaResumen=mdSalidaResumen
    )