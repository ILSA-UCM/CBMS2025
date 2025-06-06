from similitud_ProcesoComunPrincipal_dividido import (
        generar_equivalencias_y_guardar,
        evaluar_desde_archivos)

ResultadoFinalTerminos="V13/resultadoFinalNormal__7.json"
ResultadoFinalTerminosDocumento="V13/resultadoFinalNormalDocNN__7.json"
csvGold = "20250430_9e5995.csv"
deepseek_r___b = "deepseek-r1"
csvSalidaTabla = "resultadoTabla__7.csv"
mdSalidaResumen = "resultadoResumen__7.md"
equiv_gold_to_test = "salida_gold_to_test__7.json"
equiv_test_to_test = "salida_test_to_test__7.json"
equiv_gold_to_gold = "salida_gold_to_gold__7.json"
entrada_equiv_gold_to_test = "entrada_gold_to_test__7.txt"
entrada_equiv_test_to_test = "entrada_test_to_test__7.txt"
entrada_equiv_gold_to_gold = "entrada_gold_to_gold__7.txt"


if generar_equivalencias_y_guardar(
    ResultadoFinalTerminos=ResultadoFinalTerminos,
    ResultadoFinalTerminosDocumento=ResultadoFinalTerminosDocumento,
    csvGold=csvGold,
    mdSalidaResumen=mdSalidaResumen,
    salida_gold_to_test=equiv_gold_to_test,
    salida_test_to_test=equiv_test_to_test,
    salida_gold_to_gold=equiv_gold_to_gold,
    entrada_gold_to_test=entrada_equiv_gold_to_test,
    entrada_test_to_test=entrada_equiv_test_to_test,
    entrada_gold_to_gold=entrada_equiv_gold_to_gold
) :

    evaluar_desde_archivos(
            ResultadoFinalTerminosDocumento=ResultadoFinalTerminosDocumento,
            csvGold=csvGold,
            archivo_equiv_gold_to_test=equiv_gold_to_test,
            archivo_equiv_test_to_test=equiv_test_to_test,
            archivo_equiv_gold_to_gold=equiv_gold_to_gold,
            csvSalidaTabla=csvSalidaTabla,
            mdSalidaResumen=mdSalidaResumen
        )