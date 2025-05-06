
from similitud_ProcesoComunPrincipal import pipeline_evaluacion_con_equivalencias

ResultadoFinalTerminos="V13/resultadoFinalNormal__1.5.json"
ResultadoFinalTerminosDocumento="V13/resultadoFinalNormalDocNN__1_5.json"
csvGold = "20250430_9e5995.csv"
deepseek_r___b = "deepseek-r1:1.5b"
csvSalidaTabla = "resultadoTabla__1.5.csv"
mdSalidaResumen = "resultadoResumen__1.5.md"


evaluar_resultado_con_equivalencias()

pipeline_evaluacion_con_equivalencias(
    ResultadoFinalTerminos=ResultadoFinalTerminos,
    ResultadoFinalTerminosDocumento=ResultadoFinalTerminosDocumento,
    csvGold=csvGold,
    deepseek_r___b=deepseek_r___b,
    csvSalidaTabla=csvSalidaTabla,
    mdSalidaResumen=mdSalidaResumen
)