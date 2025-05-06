from similitud_ProcesoComunPrincipal import pipeline_evaluacion_con_equivalencias

ResultadoFinalTerminos="resultadoFinalNormal__70.json"
ResultadoFinalTerminosDocumento="resultadoFinalNormalDocNN__70.json"
csvGold = "20250430_9e5995.csv"
deepseek_r___b = "deepseek-r1:70b"
csvSalidaTabla = "resultadoTabla__70.csv"
mdSalidaResumen = "resultadoResumen__70.md"

pipeline_evaluacion_con_equivalencias(
    ResultadoFinalTerminos=ResultadoFinalTerminos,
    ResultadoFinalTerminosDocumento=ResultadoFinalTerminosDocumento,
    csvGold=csvGold,
    deepseek_r___b=deepseek_r___b,
    csvSalidaTabla=csvSalidaTabla,
    mdSalidaResumen=mdSalidaResumen
)