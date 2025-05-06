from similitud_ProcesoComunPrincipal import pipeline_evaluacion_con_equivalencias

ResultadoFinalTerminos="resultadoFinalNormal__7.json"
ResultadoFinalTerminosDocumento="resultadoFinalNormalDocNN__7.json"
csvGold = "20250430_9e5995.csv"
deepseek_r___b = "deepseek-r1"
csvSalidaTabla = "resultadoTabla__7.csv"
mdSalidaResumen = "resultadoResumen__7.md"

pipeline_evaluacion_con_equivalencias(
    ResultadoFinalTerminos=ResultadoFinalTerminos,
    ResultadoFinalTerminosDocumento=ResultadoFinalTerminosDocumento,
    csvGold=csvGold,
    deepseek_r___b=deepseek_r___b,
    csvSalidaTabla=csvSalidaTabla,
    mdSalidaResumen=mdSalidaResumen
)