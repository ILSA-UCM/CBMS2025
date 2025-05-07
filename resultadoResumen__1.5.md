# Evaluación de equivalencias

## Comparación de Findings entre JSONs

### En ambos JSONs:
- bronchiectasis
- fibrotic scarring
- flattened diaphragm
- hyperinflated lungs
- increased retrosternal airspace
- infiltrate in the right middle lobe
- lumbar degenerative disc disease
- pulmonary edema due to acute respiratory distress syndrome (ards)
- spine dextrocurvature

### Solo en V13/resultadoFinalNormal__1.5.json:

### Solo en V13/resultadoFinalNormalDocNN__1_5.json:
- advanced degenerative changes in the lumbar bilaterally
- air space/diffusion disease/opacity
- aortic calcifications
- ard
- ardis
- ards
- ards (acute respiratory distress syndrome)
- associated atelectatic collapse of the right middle lobe
- atelectasis in the left midlung
- breast prostheses
- calcified granuloma
- calcified granulomas
- calcified hilar
- cardiomegaly
- coping disease in right middle lobe
- dense consolidation within retrocardiac left lower lobe
- drainage catheter overlying the right upper quadrant
- elevation of right hemidiaphragm
- emphysema
- fibro scarring
- fibrosis in the right middle lobe
- fibrotic disc
- filtrate in the right middle lobe
- flatened diaphragm
- heart size and pulmonary vascular engorgement
- increased vascularity
- inflated lungs
- interstitial opacities
- interval enlargement in cardiac silhouette
- left lower lobe air space opacity
- low lung volumes without focal consolidation
- lucency in the right humeral head with geographic 1a margins
- lungscc
- mediastinal contour
- mediastinal contours stable
- mild cardiomegaly
- mildly enlarged heart
- no clinically significant finding or disease identified.
- no pneumothorax
- patchy airspace opacity in the right lung
- pleural effusion
- pleural effusion or airspace consolidation
- pneumothorax
- pneumothorax or large pleural effusion
- pulmonary edema due to ard
- pulmonary edema due to ardes
- pulmonary edema due to arthralys
- pulmonary edema due to fibrotic scarring
- pulmonary edema due toards
- pulmonary edema due toards respiratory distress syndrome (ards)
- pulmonary edema due toardsards
- pulmonary edema dueards
- pulmonary scarring
- question large pulmonary arteries
- right chest xxxx tip
- right lower lobe airspace opacity
- right-sided pleural effusion
- scarring on the left base
- small left pleural effusion
- spinal dextrocurvature
- stability of aorta
- stability of cardiomegaly
- stable left mid lung granuloma
- subsegmental atelectasis
- thoracic aorta
- thoracic aortic atherosclerotic calcifications
- thoracic spondylosis
- vague opacities in the right upper lobe

### JSON combinado de findings únicos (ordenado):
```json
[
    {"finding": "bronchiectasis"},
    {"finding": "fibrotic scarring"},
    {"finding": "flattened diaphragm"},
    {"finding": "hyperinflated lungs"},
    {"finding": "increased retrosternal airspace"},
    {"finding": "infiltrate in the right middle lobe"},
    {"finding": "lumbar degenerative disc disease"},
    {"finding": "pulmonary edema due to acute respiratory distress syndrome (ards)"},
    {"finding": "spine dextrocurvature"},
    {"finding": "advanced degenerative changes in the lumbar bilaterally"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "air space/diffusion disease/opacity"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "aortic calcifications"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "ard"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "ardis"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "ards"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "ards (acute respiratory distress syndrome)"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "associated atelectatic collapse of the right middle lobe"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "atelectasis in the left midlung"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "breast prostheses"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "calcified granuloma"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "calcified granulomas"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "calcified hilar"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "cardiomegaly"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "coping disease in right middle lobe"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "dense consolidation within retrocardiac left lower lobe"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "drainage catheter overlying the right upper quadrant"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "elevation of right hemidiaphragm"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "emphysema"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "fibro scarring"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "fibrosis in the right middle lobe"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "fibrotic disc"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "filtrate in the right middle lobe"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "flatened diaphragm"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "heart size and pulmonary vascular engorgement"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "increased vascularity"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "inflated lungs"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "interstitial opacities"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "interval enlargement in cardiac silhouette"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "left lower lobe air space opacity"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "low lung volumes without focal consolidation"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "lucency in the right humeral head with geographic 1a margins"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "lungscc"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "mediastinal contour"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "mediastinal contours stable"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "mild cardiomegaly"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "mildly enlarged heart"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "no clinically significant finding or disease identified."}, // Añadido desde la segunda pasada de los documentos
    {"finding": "no pneumothorax"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "patchy airspace opacity in the right lung"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pleural effusion"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pleural effusion or airspace consolidation"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pneumothorax"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pneumothorax or large pleural effusion"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema due to ard"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema due to ardes"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema due to arthralys"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema due to fibrotic scarring"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema due toards"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema due toards respiratory distress syndrome (ards)"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema due toardsards"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary edema dueards"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pulmonary scarring"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "question large pulmonary arteries"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "right chest xxxx tip"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "right lower lobe airspace opacity"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "right-sided pleural effusion"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "scarring on the left base"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "small left pleural effusion"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "spinal dextrocurvature"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "stability of aorta"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "stability of cardiomegaly"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "stable left mid lung granuloma"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "subsegmental atelectasis"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "thoracic aorta"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "thoracic aortic atherosclerotic calcifications"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "thoracic spondylosis"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "vague opacities in the right upper lobe"} // Añadido desde la segunda pasada de los documentos
]
```

## Lista Gold 

```json
[
    {"finding": "Mild cardiomegaly"},
    {"finding": "Mild unfolding of the thoracic aorta"},
    {"finding": "No focal air space opacity"},
    {"finding": "No pleural effusion or pneumothorax"},
    {"finding": "Visualized osseous structures are unremarkable"},
    {"finding": "Normal heart size"},
    {"finding": "Unremarkable mediastinum"},
    {"finding": "Lingula scarring"},
    {"finding": "Clear lungs"},
    {"finding": "Angulate opacities"},
    {"finding": "No focal infiltrates"},
    {"finding": "No focal consolidation"},
    {"finding": "No suspicious pulmonary opacities"},
    {"finding": "No pleural effusions"},
    {"finding": "No pneumothorax"},
    {"finding": "Stable left mid lung granuloma"},
    {"finding": "Normal cardiac contours"},
    {"finding": "Thoracic spondylosis"},
    {"finding": "Mildly enlarged heart"},
    {"finding": "Elevated left hemidiaphragm"},
    {"finding": "No acute infiltrate or pleural effusion"},
    {"finding": "Central vascular prominence"},
    {"finding": "Diffuse bilateral interstitial and alveolar opacities"},
    {"finding": "Left basilar airspace opacities"},
    {"finding": "Large heart size"},
    {"finding": "Normal cardiomediastinal silhouette"},
    {"finding": "Mildly hyperinflated lungs"},
    {"finding": "Resolution of bibasilar infiltrates"},
    {"finding": "Minimal scarring or atelectasis right midlung"},
    {"finding": "No focal airspace disease"},
    {"finding": "No pneumothorax or pleural effusion"},
    {"finding": "Normal heart and pulmonary vasculature"},
    {"finding": "Normal mediastinal contours"},
    {"finding": "Mild degenerative changes of the thoracic spine"},
    {"finding": "Stable mediastinal contours"},
    {"finding": "Aortic calcifications"},
    {"finding": "Small calcified lymph nodes"},
    {"finding": "Emphysema"},
    {"finding": "Left perihilar upper lobe opacity"},
    {"finding": "Possible pleural extension"},
    {"finding": "Low lung volumes"},
    {"finding": "No focal airspace opacity"},
    {"finding": "Multilevel degenerative changes in the spine"},
    {"finding": "Chronic asymmetric elevation of the right hemidiaphragm"},
    {"finding": "Increased streaky airspace disease right lung base"},
    {"finding": "Stable hilar prominence"},
    {"finding": "No pneumothorax or large pleural effusion"},
    {"finding": "Grossly normal heart size"},
    {"finding": "No focal consolidation or pneumothorax"},
    {"finding": "Unremarkable cardio mediastinal silhouette"},
    {"finding": "Mild multilevel thoracolumbar degenerative disc disease"},
    {"finding": "Stable upper abdominal midline surgical sutures"},
    {"finding": "Postop changes of CABG"},
    {"finding": "Right lower lobe infiltrate"},
    {"finding": "Normal cardiac and mediastinal silhouettes"},
    {"finding": "Normal pulmonary vasculature"},
    {"finding": "Advanced degenerative changes"},
    {"finding": "Right humeral head lucency"},
    {"finding": "Mildly hyperlucent lungs"},
    {"finding": "Denser lumbar scoliosis"},
    {"finding": "Enlarged heart"},
    {"finding": "Thoracic aortic atherosclerotic calcifications"},
    {"finding": "Dense consolidation left lower lobe"},
    {"finding": "Patchy airspace opacity right lung"},
    {"finding": "No focal airspace consolidation"},
    {"finding": "Normal heart size and mediastinal contour"},
    {"finding": "Degenerative changes of the spine"},
    {"finding": "Stable mediastinum"},
    {"finding": "Right chest tip at cavoatrial junction"},
    {"finding": "Elevated right hemidiaphragm with right-sided pleural effusion"},
    {"finding": "Vague right upper lobe opacities"},
    {"finding": "Clear left lung"},
    {"finding": "Drainage catheter right upper quadrant"},
    {"finding": "Hyperinflated lungs"},
    {"finding": "Coarse interstitial markings"},
    {"finding": "Chronic pleural-parenchymal scarring"},
    {"finding": "No lobar consolidation"},
    {"finding": "Stable right chest wall pacemaker"},
    {"finding": "Stable cardiomegaly"},
    {"finding": "Calcified thoracic aorta"},
    {"finding": "Stable mild interstitial opacities"},
    {"finding": "Unchanged dense retrocardiac opacities"},
    {"finding": "No pneumothorax or large effusion"},
    {"finding": "No focal consolidation or large pleural effusion"},
    {"finding": "No acute bone abnormality"},
    {"finding": "Lobulated opacity anterior mediastinum"},
    {"finding": "Tortuous/calcified thoracic aorta"},
    {"finding": "Hyperexpanded lungs"},
    {"finding": "Severe degenerative changes of the thoracic spine"},
    {"finding": "Vascular calcification"},
    {"finding": "No pleural effusions or pneumothoraces"},
    {"finding": "Normal heart and mediastinum"},
    {"finding": "Degenerative changes in the spine"},
    {"finding": "Large hiatal hernia"},
    {"finding": "Diffuse right lower lobe airspace opacity"},
    {"finding": "Normal skeletal structures"},
    {"finding": "Calcified granulomas"},
    {"finding": "Calcified hilar lymph nodes"},
    {"finding": "Degenerative changes thoracic spine"},
    {"finding": "Tortuous thoracic aorta"},
    {"finding": "Tortuous aorta"},
    {"finding": "Extensive degenerative changes of the thoracic spine"},
    {"finding": "No pneumothorax or significant pulmonary edema"},
    {"finding": "Small left pleural effusion"},
    {"finding": "No focal lung consolidation"},
    {"finding": "Mildly low lung volumes"},
    {"finding": "No acute abnormality"},
    {"finding": "Mild tortuosity of the thoracic aorta"},
    {"finding": "Mildly hyperexpanded lungs"},
    {"finding": "No focal airspace consolidations"},
    {"finding": "No pleural effusion"},
    {"finding": "Degenerative changes of the midthoracic spine"},
    {"finding": "Stable coronary stent"},
    {"finding": "Sternotomy changes"},
    {"finding": "No mediastinal widening"},
    {"finding": "No large pleural effusion or pneumothorax"},
    {"finding": "Mild dextro curvature of the thoracic spine"},
    {"finding": "Postoperative sternotomy changes"},
    {"finding": "Cardiomegaly"},
    {"finding": "Prominent ascending aorta (aneurysm)"},
    {"finding": "Minimal degenerative changes of the spine"},
    {"finding": "Borderline enlarged heart"},
    {"finding": "Tortuous/ectatic thoracic aorta"},
    {"finding": "No focal pulmonary opacity"},
    {"finding": "Fracture of distal right clavicle"},
    {"finding": "Atherosclerosis of the aorta"},
    {"finding": "Minimal left lung base densities"},
    {"finding": "No acute bony abnormalities"},
    {"finding": "Hyperinflated lungs (emphysema)"},
    {"finding": "Biapical scarring"},
    {"finding": "No acute infiltrate"},
    {"finding": "No focal consolidation or pleural effusion"},
    {"finding": "Tortuous descending thoracic aorta"},
    {"finding": "Central venous catheter"},
    {"finding": "No focal airspace opacities"},
    {"finding": "Moderate cardiomegaly"},
    {"finding": "Bibasilar and perihilar interstitial opacities"},
    {"finding": "Large right pleural effusion with atelectasis"},
    {"finding": "Right lung opacities"},
    {"finding": "Stable cardio mediastinal silhouette"},
    {"finding": "Increased pulmonary vascularity"},
    {"finding": "Elevated right hemidiaphragm"},
    {"finding": "Right lung base airspace disease/atelectasis"},
    {"finding": "Left base streaky opacity"},
    {"finding": "Blunted costophrenic angles"},
    {"finding": "Calcified granuloma left upper lobe"},
    {"finding": "Normal heart size and pulmonary vascularity"},
    {"finding": "Unremarkable mediastinal contour"},
    {"finding": "No acute bony findings"},
    {"finding": "No cardiac enlargement"},
    {"finding": "No vascular congestion"},
    {"finding": "Small circular opacities right upper lung"},
    {"finding": "No bony abnormality"},
    {"finding": "Enlarged cardiac silhouette"},
    {"finding": "Status post sternotomy and CABG"},
    {"finding": "Left midlung atelectasis or scar"},
    {"finding": "Blunted left costophrenic angle"},
    {"finding": "Surgical clips at thoracic inlet"},
    {"finding": "Left base scarring"},
    {"finding": "Hyperinflation"},
    {"finding": "Anterior mediastinal calcification"},
    {"finding": "Normal heart"},
    {"finding": "Arthritic changes of the spine"},
    {"finding": "Atherosclerotic calcifications of the aorta"},
    {"finding": "Known large breast mass"},
    {"finding": "Upper normal heart size"},
    {"finding": "Minimal right middle lobe atelectasis"},
    {"finding": "Degenerative endplate changes of the spine"},
    {"finding": "Interval enlargement of the cardiac silhouette"},
    {"finding": "Normally inflated and clear lungs"},
    {"finding": "Normal osseous structures"},
    {"finding": "Streaky bibasilar airspace opacities"},
    {"finding": "No acute osseous findings"},
    {"finding": "Mild dextroscoliosis"},
    {"finding": "Prior anterior cervical fusion"},
    {"finding": "Stable small calcified granuloma left base"},
    {"finding": "No acute findings"},
    {"finding": "Unremarkable heart and mediastinum"},
    {"finding": "No effusion or pneumothorax"},
    {"finding": "Mild anterior deformities L1-L2"},
    {"finding": "Retropulsion of L1"},
    {"finding": "Bilateral interstitial opacities"},
    {"finding": "No pleural effusions or pneumothorax"},
    {"finding": "Moderate degenerative changes of the thoracic spine"},
    {"finding": "Bibasilar pleural scarring"},
    {"finding": "No pneumothorax or effusion"},
    {"finding": "Normal pulmonary vascularity"},
    {"finding": "Calcified hilar lymph nodes and granulomas"},
    {"finding": "Stable degenerative changes in the spine"},
    {"finding": "Relatively clear lungs"},
    {"finding": "Unfolded aorta"},
    {"finding": "Moderate hiatal hernia"},
    {"finding": "T-spine osteophytes and DISH"},
    {"finding": "No focal infiltrate or suspicious opacity"},
    {"finding": "Lucency right lung base (skin fold)"},
    {"finding": "Moderately enlarged heart"},
    {"finding": "Left midlung and basilar opacities (atelectasis)"},
    {"finding": "Improved right midlung opacity"},
    {"finding": "Mild degenerative changes of the spine"},
    {"finding": "Intact sternotomy wires"},
    {"finding": "Extensive atherosclerotic disease"},
    {"finding": "No alveolar consolidation or pleural effusion"},
    {"finding": "S-shaped spine curvature"},
    {"finding": "Retrocardiac soft tissue density (possible hiatal hernia)"},
    {"finding": "Calcified granuloma"},
    {"finding": "Left lung base bandlike opacity (atelectasis)"},
    {"finding": "Osteopenia"}
]
```
# Calculo de similitud


## Equivalencias: Gold → Test
- Advanced degenerative changes -> advanced degenerative changes in the lumbar bilaterally
- Angulate opacities -> interstitial opacities
- Anterior mediastinal calcification -> 
- Aortic calcifications -> aortic calcifications, thoracic aortic atherosclerotic calcifications
- Arthritic changes of the spine -> lumbar degenerative disc disease
- Atherosclerosis of the aorta -> aortic calcifications
- Atherosclerotic calcifications of the aorta -> aortic calcifications
- Biapical scarring -> fibrotic scarring, pulmonary scarring
- Bibasilar and perihilar interstitial opacities -> interstitial opacities
- Bibasilar pleural scarring -> fibrotic scarring, pulmonary scarring
- Bilateral interstitial opacities -> interstitial opacities
- Blunted costophrenic angles -> pleural effusion
- Blunted left costophrenic angle -> pleural effusion
- Borderline enlarged heart -> mildly enlarged heart
- Calcified granuloma -> calcified granuloma, calcified granulomas
- Calcified granuloma left upper lobe -> calcified granuloma, calcified granulomas
- Calcified granulomas -> calcified granuloma, calcified granulomas
- Calcified hilar lymph nodes -> calcified hilar
- Calcified hilar lymph nodes and granulomas -> calcified granulomas, calcified hilar
- Calcified thoracic aorta -> aortic calcifications, thoracic aortic atherosclerotic calcifications
- Cardiomegaly -> cardiomegaly, mildly enlarged heart
- Central vascular prominence -> heart size and pulmonary vascular engorgement, increased vascularity
- Central venous catheter -> drainage catheter overlying the right upper quadrant
- Chronic asymmetric elevation of the right hemidiaphragm -> elevation of right hemidiaphragm
- Chronic pleural-parenchymal scarring -> fibrotic scarring, pulmonary scarring
- Clear left lung -> 
- Clear lungs -> 
- Coarse interstitial markings -> interstitial opacities
- Degenerative changes in the spine -> lumbar degenerative disc disease, thoracic spondylosis
- Degenerative changes of the midthoracic spine -> thoracic spondylosis
- Degenerative changes of the spine -> lumbar degenerative disc disease, thoracic spondylosis
- Degenerative changes thoracic spine -> thoracic spondylosis
- Degenerative endplate changes of the spine -> lumbar degenerative disc disease
- Dense consolidation left lower lobe -> dense consolidation within retrocardiac left lower lobe
- Denser lumbar scoliosis -> spinal dextrocurvature, spine dextrocurvature
- Diffuse bilateral interstitial and alveolar opacities -> air space/diffusion disease/opacity, interstitial opacities
- Diffuse right lower lobe airspace opacity -> right lower lobe airspace opacity
- Drainage catheter right upper quadrant -> drainage catheter overlying the right upper quadrant
- Elevated left hemidiaphragm -> elevation of right hemidiaphragm
- Elevated right hemidiaphragm -> elevation of right hemidiaphragm
- Elevated right hemidiaphragm with right-sided pleural effusion -> elevation of right hemidiaphragm, right-sided pleural effusion
- Emphysema -> emphysema
- Enlarged cardiac silhouette -> cardiomegaly
- Enlarged heart -> cardiomegaly, mildly enlarged heart
- Extensive atherosclerotic disease -> aortic calcifications
- Extensive degenerative changes of the thoracic spine -> advanced degenerative changes in the lumbar bilaterally
- Fracture of distal right clavicle -> 
- Grossly normal heart size -> no cardiac enlargement
- Hyperexpanded lungs -> hyperinflated lungs
- Hyperinflated lungs -> hyperinflated lungs, inflated lungs
- Hyperinflated lungs (emphysema) -> emphysema, hyperinflated lungs
- Hyperinflation -> hyperinflated lungs
- Improved right midlung opacity -> resolution of bibasilar infiltrates
- Increased pulmonary vascularity -> increased vascularity
- Increased streaky airspace disease right lung base -> filtrate in the right middle lobe, infiltrate in the right middle lobe
- Intact sternotomy wires -> 
- Interval enlargement of the cardiac silhouette -> interval enlargement in cardiac silhouette
- Known large breast mass -> breast prostheses
- Large heart size -> cardiomegaly, interval enlargement in cardiac silhouette, mildly enlarged heart
- Large hiatal hernia -> 
- Large right pleural effusion with atelectasis -> right-sided pleural effusion
- Left base scarring -> scarring on the left base
- Left base streaky opacity -> scarring on the left base
- Left basilar airspace opacities -> left lower lobe air space opacity
- Left lung base bandlike opacity (atelectasis) -> atelectasis in the left midlung
- Left midlung and basilar opacities (atelectasis) -> atelectasis in the left midlung
- Left midlung atelectasis or scar -> atelectasis in the left midlung
- Left perihilar upper lobe opacity -> vague opacities in the right upper lobe
- Lingula scarring -> fibrotic scarring, pulmonary scarring, scarring on the left base
- Lobulated opacity anterior mediastinum -> 
- Low lung volumes -> low lung volumes without focal consolidation
- Lucency right lung base (skin fold) -> 
- Mild anterior deformities L1-L2 -> 
- Mild cardiomegaly -> cardiomegaly, mild cardiomegaly, mildly enlarged heart, stability of cardiomegaly
- Mild degenerative changes of the spine -> lumbar degenerative disc disease
- Mild degenerative changes of the thoracic spine -> thoracic spondylosis
- Mild dextro curvature of the thoracic spine -> spinal dextrocurvature, spine dextrocurvature
- Mild dextroscoliosis -> spinal dextrocurvature, spine dextrocurvature
- Mild multilevel thoracolumbar degenerative disc disease -> lumbar degenerative disc disease
- Mild tortuosity of the thoracic aorta -> thoracic aorta
- Mild unfolding of the thoracic aorta -> stability of aorta, thoracic aorta
- Mildly enlarged heart -> cardiomegaly, mild cardiomegaly, mildly enlarged heart
- Mildly hyperexpanded lungs -> hyperinflated lungs
- Mildly hyperinflated lungs -> hyperinflated lungs, inflated lungs
- Mildly hyperlucent lungs -> hyperinflated lungs
- Mildly low lung volumes -> low lung volumes without focal consolidation
- Minimal degenerative changes of the spine -> lumbar degenerative disc disease
- Minimal left lung base densities -> 
- Minimal right middle lobe atelectasis -> infiltrate in the right middle lobe
- Minimal scarring or atelectasis right midlung -> atelectasis in the left midlung, fibrosis in the right middle lobe, subsegmental atelectasis
- Moderate cardiomegaly -> cardiomegaly, mildly enlarged heart
- Moderate degenerative changes of the thoracic spine -> thoracic spondylosis
- Moderate hiatal hernia -> 
- Moderately enlarged heart -> cardiomegaly, mildly enlarged heart
- Multilevel degenerative changes in the spine -> advanced degenerative changes in the lumbar bilaterally, lumbar degenerative disc disease
- No acute abnormality -> no clinically significant finding or disease identified.
- No acute bone abnormality -> 
- No acute bony abnormalities -> 
- No acute bony findings -> 
- No acute findings -> no clinically significant finding or disease identified.
- No acute infiltrate -> no clinically significant finding or disease identified.
- No acute infiltrate or pleural effusion -> no clinically significant finding or disease identified.
- No acute osseous findings -> 
- No alveolar consolidation or pleural effusion -> no clinically significant finding or disease identified.
- No bony abnormality -> 
- No cardiac enlargement -> 
- No effusion or pneumothorax -> no pneumothorax
- No focal air space opacity -> no clinically significant finding or disease identified.
- No focal airspace consolidation -> no clinically significant finding or disease identified.
- No focal airspace consolidations -> no clinically significant finding or disease identified.
- No focal airspace disease -> no clinically significant finding or disease identified.
- No focal airspace opacities -> no clinically significant finding or disease identified.
- No focal airspace opacity -> no clinically significant finding or disease identified.
- No focal consolidation -> no focal airspace consolidation, no lobar consolidation
- No focal consolidation or large pleural effusion -> no clinically significant finding or disease identified.
- No focal consolidation or pleural effusion -> no clinically significant finding or disease identified.
- No focal consolidation or pneumothorax -> no focal airspace consolidation, no pneumothorax
- No focal infiltrate or suspicious opacity -> no clinically significant finding or disease identified.
- No focal infiltrates -> no clinically significant finding or disease identified.
- No focal lung consolidation -> no clinically significant finding or disease identified.
- No focal pulmonary opacity -> no clinically significant finding or disease identified.
- No large pleural effusion or pneumothorax -> no pneumothorax or large pleural effusion
- No lobar consolidation -> no clinically significant finding or disease identified.
- No mediastinal widening -> 
- No pleural effusion -> no pleural effusion or airspace consolidation
- No pleural effusion or pneumothorax -> no pleural effusion or airspace consolidation, no pneumothorax, no pneumothorax or large pleural effusion
- No pleural effusions -> no pleural effusion or airspace consolidation
- No pleural effusions or pneumothoraces -> no pleural effusion or airspace consolidation, no pneumothorax
- No pleural effusions or pneumothorax -> no pneumothorax
- No pneumothorax -> no pneumothorax or large pleural effusion
- No pneumothorax or effusion -> no pneumothorax
- No pneumothorax or large effusion -> no pneumothorax, no pneumothorax or large pleural effusion
- No pneumothorax or large pleural effusion -> no pneumothorax, no pneumothorax or large pleural effusion
- No pneumothorax or pleural effusion -> no pleural effusion or airspace consolidation, no pneumothorax
- No pneumothorax or significant pulmonary edema -> no pneumothorax
- No suspicious pulmonary opacities -> no clinically significant finding or disease identified.
- No vascular congestion -> 
- Normal cardiac and mediastinal silhouettes -> 
- Normal cardiac contours -> 
- Normal cardiomediastinal silhouette -> 
- Normal heart -> 
- Normal heart and mediastinum -> 
- Normal heart and pulmonary vasculature -> 
- Normal heart size -> no cardiac enlargement
- Normal heart size and mediastinal contour -> 
- Normal heart size and pulmonary vascularity -> 
- Normal mediastinal contours -> mediastinal contour, mediastinal contours stable
- Normal osseous structures -> 
- Normal pulmonary vascularity -> 
- Normal pulmonary vasculature -> 
- Normal skeletal structures -> 
- Normally inflated and clear lungs -> 
- Osteopenia -> 
- Patchy airspace opacity right lung -> patchy airspace opacity in the right lung
- Possible pleural extension -> pleural effusion, right-sided pleural effusion, small left pleural effusion
- Postop changes of CABG -> 
- Postoperative sternotomy changes -> 
- Prior anterior cervical fusion -> 
- Prominent ascending aorta (aneurysm) -> 
- Relatively clear lungs -> 
- Resolution of bibasilar infiltrates -> improved right midlung opacity
- Retrocardiac soft tissue density (possible hiatal hernia) -> 
- Retropulsion of L1 -> 
- Right chest tip at cavoatrial junction -> right chest xxxx tip
- Right humeral head lucency -> lucency in the right humeral head with geographic 1a margins
- Right lower lobe infiltrate -> infiltrate in the right middle lobe, right lower lobe airspace opacity
- Right lung base airspace disease/atelectasis -> infiltrate in the right middle lobe
- Right lung opacities -> right lower lobe airspace opacity
- S-shaped spine curvature -> spinal dextrocurvature, spine dextrocurvature
- Severe degenerative changes of the thoracic spine -> advanced degenerative changes in the lumbar bilaterally
- Small calcified lymph nodes -> calcified hilar
- Small circular opacities right upper lung -> vague opacities in the right upper lobe
- Small left pleural effusion -> pleural effusion, small left pleural effusion
- Stable cardio mediastinal silhouette -> 
- Stable cardiomegaly -> cardiomegaly, stability of cardiomegaly
- Stable coronary stent -> 
- Stable degenerative changes in the spine -> lumbar degenerative disc disease
- Stable hilar prominence -> 
- Stable left mid lung granuloma -> calcified granuloma, calcified granulomas, stable left mid lung granuloma
- Stable mediastinal contours -> mediastinal contour, mediastinal contours stable
- Stable mediastinum -> mediastinal contour, mediastinal contours stable
- Stable mild interstitial opacities -> interstitial opacities
- Stable right chest wall pacemaker -> 
- Stable small calcified granuloma left base -> calcified granuloma, calcified granulomas
- Stable upper abdominal midline surgical sutures -> 
- Status post sternotomy and CABG -> 
- Sternotomy changes -> 
- Streaky bibasilar airspace opacities -> interstitial opacities
- Surgical clips at thoracic inlet -> 
- T-spine osteophytes and DISH -> 
- Thoracic aortic atherosclerotic calcifications -> aortic calcifications, thoracic aortic atherosclerotic calcifications
- Thoracic spondylosis -> thoracic spondylosis
- Tortuous aorta -> thoracic aorta
- Tortuous descending thoracic aorta -> thoracic aorta
- Tortuous thoracic aorta -> thoracic aorta
- Tortuous/calcified thoracic aorta -> thoracic aorta
- Tortuous/ectatic thoracic aorta -> thoracic aorta
- Unchanged dense retrocardiac opacities -> 
- Unfolded aorta -> thoracic aorta
- Unremarkable cardio mediastinal silhouette -> 
- Unremarkable heart and mediastinum -> 
- Unremarkable mediastinal contour -> mediastinal contour, mediastinal contours stable
- Unremarkable mediastinum -> mediastinal contour, mediastinal contours stable
- Upper normal heart size -> 
- Vague right upper lobe opacities -> vague opacities in the right upper lobe
- Vascular calcification -> aortic calcifications
- Visualized osseous structures are unremarkable -> 

## Equivalencias: Test → Test
- advanced degenerative changes in the lumbar bilaterally -> lumbar degenerative disc disease
- air space/diffusion disease/opacity -> left lower lobe air space opacity, patchy airspace opacity in the right lung
- aortic calcifications -> thoracic aortic atherosclerotic calcifications
- ard -> ardis, ards, ards (acute respiratory distress syndrome)
- ardis -> ard, ards, ards (acute respiratory distress syndrome)
- ards -> ard, ardis, ards (acute respiratory distress syndrome)
- ards (acute respiratory distress syndrome) -> ard, ardis, ards
- associated atelectatic collapse of the right middle lobe -> subsegmental atelectasis
- atelectasis in the left midlung -> subsegmental atelectasis
- breast prostheses -> 
- bronchiectasis -> 
- calcified granuloma -> calcified granulomas, stable left mid lung granuloma
- calcified granulomas -> calcified granuloma, stable left mid lung granuloma
- calcified hilar -> 
- cardiomegaly -> mild cardiomegaly, mildly enlarged heart, stability of cardiomegaly
- coping disease in right middle lobe -> fibrosis in the right middle lobe, infiltrate in the right middle lobe
- dense consolidation within retrocardiac left lower lobe -> 
- drainage catheter overlying the right upper quadrant -> 
- elevation of right hemidiaphragm -> 
- emphysema -> hyperinflated lungs
- fibro scarring -> fibrotic scarring, pulmonary scarring, scarring on the left base
- fibrosis in the right middle lobe -> coping disease in right middle lobe, infiltrate in the right middle lobe
- fibrotic disc -> lumbar degenerative disc disease
- fibrotic scarring -> fibro scarring, pulmonary scarring, scarring on the left base
- filtrate in the right middle lobe -> coping disease in right middle lobe, infiltrate in the right middle lobe
- flatened diaphragm -> flattened diaphragm
- flattened diaphragm -> flatened diaphragm
- heart size and pulmonary vascular engorgement -> increased vascularity
- hyperinflated lungs -> emphysema, inflated lungs
- increased retrosternal airspace -> 
- increased vascularity -> heart size and pulmonary vascular engorgement
- infiltrate in the right middle lobe -> coping disease in right middle lobe, fibrosis in the right middle lobe, filtrate in the right middle lobe
- inflated lungs -> emphysema, hyperinflated lungs
- interstitial opacities -> 
- interval enlargement in cardiac silhouette -> cardiomegaly
- left lower lobe air space opacity -> air space/diffusion disease/opacity
- low lung volumes without focal consolidation -> 
- lucency in the right humeral head with geographic 1a margins -> 
- lumbar degenerative disc disease -> advanced degenerative changes in the lumbar bilaterally, fibrotic disc
- lungscc -> 
- mediastinal contour -> mediastinal contours stable
- mediastinal contours stable -> mediastinal contour
- mild cardiomegaly -> cardiomegaly, mildly enlarged heart
- mildly enlarged heart -> cardiomegaly, mild cardiomegaly
- no clinically significant finding or disease identified. -> 
- no pneumothorax -> pneumothorax or large pleural effusion
- patchy airspace opacity in the right lung -> air space/diffusion disease/opacity
- pleural effusion -> pleural effusion or airspace consolidation, right-sided pleural effusion, small left pleural effusion
- pleural effusion or airspace consolidation -> pleural effusion
- pneumothorax -> no pneumothorax, pneumothorax or large pleural effusion
- pneumothorax or large pleural effusion -> no pneumothorax, pneumothorax
- pulmonary edema due to acute respiratory distress syndrome (ards) -> pulmonary edema due to ard, pulmonary edema due to ardes, pulmonary edema due to arthralys, pulmonary edema due toards, pulmonary edema due toards respiratory distress syndrome (ards), pulmonary edema due toardsards, pulmonary edema dueards
- pulmonary edema due to ard -> pulmonary edema due to acute respiratory distress syndrome (ards)
- pulmonary edema due to ardes -> pulmonary edema due to acute respiratory distress syndrome (ards)
- pulmonary edema due to arthralys -> pulmonary edema due to acute respiratory distress syndrome (ards)
- pulmonary edema due to fibrotic scarring -> 
- pulmonary edema due toards -> pulmonary edema due to acute respiratory distress syndrome (ards)
- pulmonary edema due toards respiratory distress syndrome (ards) -> pulmonary edema due to acute respiratory distress syndrome (ards)
- pulmonary edema due toardsards -> pulmonary edema due to acute respiratory distress syndrome (ards)
- pulmonary edema dueards -> pulmonary edema due to acute respiratory distress syndrome (ards)
- pulmonary scarring -> fibro scarring, fibrotic scarring, scarring on the left base
- question large pulmonary arteries -> 
- right chest xxxx tip -> 
- right lower lobe airspace opacity -> 
- right-sided pleural effusion -> pleural effusion, small left pleural effusion
- scarring on the left base -> fibro scarring, fibrotic scarring, pulmonary scarring
- small left pleural effusion -> pleural effusion, right-sided pleural effusion
- spinal dextrocurvature -> spine dextrocurvature
- spine dextrocurvature -> spinal dextrocurvature
- stability of aorta -> thoracic aorta
- stability of cardiomegaly -> cardiomegaly
- stable left mid lung granuloma -> calcified granuloma, calcified granulomas
- subsegmental atelectasis -> associated atelectatic collapse of the right middle lobe, atelectasis in the left midlung
- thoracic aorta -> stability of aorta, thoracic aortic atherosclerotic calcifications
- thoracic aortic atherosclerotic calcifications -> aortic calcifications, thoracic aorta
- thoracic spondylosis -> 
- vague opacities in the right upper lobe -> 

## Equivalencias: Gold → Gold
- Advanced degenerative changes -> Severe degenerative changes of the thoracic spine
- Angulate opacities -> Bibasilar and perihilar interstitial opacities, Increased streaky airspace disease right lung base, Left base streaky opacity, Left basilar airspace opacities, Left midlung and basilar opacities (atelectasis), Patchy airspace opacity right lung, Streaky bibasilar airspace opacities
- Anterior mediastinal calcification -> Lobulated opacity anterior mediastinum
- Aortic calcifications -> Atherosclerosis of the aorta, Atherosclerotic calcifications of the aorta, Calcified thoracic aorta, Extensive atherosclerotic disease, Tortuous/calcified thoracic aorta, Vascular calcification
- Atherosclerosis of the aorta -> Aortic calcifications
- Biapical scarring -> Lingula scarring
- Bibasilar and perihilar interstitial opacities -> Angulate opacities
- Bibasilar pleural scarring -> Lingula scarring
- Blunted costophrenic angles -> Possible pleural extension
- Borderline enlarged heart -> Mild cardiomegaly
- Calcified granulomas -> Stable small calcified granuloma left base
- Calcified hilar lymph nodes and granulomas -> Small calcified lymph nodes
- Calcified thoracic aorta -> Aortic calcifications
- Central vascular prominence -> Increased pulmonary vascularity, Normal pulmonary vasculature, Prominent ascending aorta (aneurysm)
- Chronic pleural-parenchymal scarring -> Lingula scarring
- Clear left lung -> Clear lungs
- Clear lungs -> Clear left lung, No acute findings, No acute infiltrate, No acute infiltrate or pleural effusion, Normally inflated and clear lungs, Relatively clear lungs
- Coarse interstitial markings -> Diffuse bilateral interstitial and alveolar opacities
- Degenerative changes of the spine -> Thoracic spondylosis
- Dense consolidation left lower lobe -> Left basilar airspace opacities
- Diffuse bilateral interstitial and alveolar opacities -> Bilateral interstitial opacities, Coarse interstitial markings, Stable mild interstitial opacities
- Drainage catheter right upper quadrant -> Central venous catheter
- Elevated left hemidiaphragm -> Chronic asymmetric elevation of the right hemidiaphragm, Elevated right hemidiaphragm
- Emphysema -> Hyperinflated lungs (emphysema)
- Enlarged cardiac silhouette -> Large heart size
- Extensive degenerative changes of the thoracic spine -> Severe degenerative changes of the thoracic spine
- Hyperinflation -> Mildly hyperinflated lungs
- Improved right midlung opacity -> Resolution of bibasilar infiltrates
- Increased pulmonary vascularity -> Central vascular prominence
- Intact sternotomy wires -> Sternotomy changes
- Known large breast mass -> 
- Large heart size -> Cardiomegaly, Enlarged cardiac silhouette, Enlarged heart, Mild cardiomegaly, Mildly enlarged heart, Moderate cardiomegaly
- Large hiatal hernia -> Moderate hiatal hernia, Retrocardiac soft tissue density (possible hiatal hernia)
- Left midlung atelectasis or scar -> Minimal scarring or atelectasis right midlung
- Left perihilar upper lobe opacity -> Small circular opacities right upper lung, Vague right upper lobe opacities
- Lingula scarring -> Biapical scarring, Calcified granuloma left upper lobe, Calcified granulomas, Chronic pleural-parenchymal scarring, Left base scarring, Minimal scarring or atelectasis right midlung, Stable small calcified granuloma left base
- Lobulated opacity anterior mediastinum -> Anterior mediastinal calcification
- Low lung volumes -> Mildly low lung volumes
- Lucency right lung base (skin fold) -> 
- Mild anterior deformities L1-L2 -> 
- Mild cardiomegaly -> Borderline enlarged heart, Cardiomegaly, Enlarged cardiac silhouette, Enlarged heart, Interval enlargement of the cardiac silhouette, Large heart size, Mildly enlarged heart, Moderate cardiomegaly, Upper normal heart size
- Mild unfolding of the thoracic aorta -> Mild tortuosity of the thoracic aorta, Tortuous aorta, Tortuous descending thoracic aorta, Tortuous thoracic aorta, Tortuous/ectatic thoracic aorta, Unfolded aorta
- Mildly hyperinflated lungs -> Hyperexpanded lungs, Hyperinflated lungs, Hyperinflated lungs (emphysema), Hyperinflation, Mildly hyperexpanded lungs
- Minimal left lung base densities -> Left base streaky opacity
- Minimal right middle lobe atelectasis -> Minimal scarring or atelectasis right midlung
- Minimal scarring or atelectasis right midlung -> Left base streaky opacity, Left lung base bandlike opacity (atelectasis), Left midlung atelectasis or scar, Minimal right middle lobe atelectasis, Right lung base airspace disease/atelectasis
- Moderate cardiomegaly -> Mild cardiomegaly
- Moderate hiatal hernia -> Large hiatal hernia
- Moderately enlarged heart -> Moderate cardiomegaly
- No cardiac enlargement -> Normal heart size
- No focal air space opacity -> No alveolar consolidation, No focal airspace consolidations, No focal airspace disease, No focal airspace opacities, No focal airspace opacity, No focal consolidation, No focal lung consolidation, No focal pulmonary opacity, No lobar consolidation
- No focal consolidation -> No focal consolidation or large pleural effusion, No focal consolidation or pleural effusion, No focal consolidation or pneumothorax
- No focal infiltrate or suspicious opacity -> No focal infiltrates
- No focal infiltrates -> No acute infiltrate, No focal infiltrate or suspicious opacity, No suspicious pulmonary opacities
- No pleural effusion or pneumothorax -> No effusion or pneumothorax, No large pleural effusion or pneumothorax, No pleural effusions, No pleural effusions or pneumothorax, No pneumothoraces, No pneumothorax, No pneumothorax or effusion, No pneumothorax or large effusion, No pneumothorax or pleural effusion, No pneumothorax or significant pulmonary edema
- No pneumothorax or significant pulmonary edema -> No pleural effusion or pneumothorax
- No vascular congestion -> Normal pulmonary vasculature
- Normal cardiac contours -> Normal cardiac and mediastinal silhouettes, Normal cardiomediastinal silhouette, Normal heart size
- Normal heart and mediastinum -> Unremarkable heart and mediastinum
- Normal heart size -> Grossly normal heart size, No cardiac enlargement, Normal cardiac contours, Normal heart, Normal heart and mediastinum, Normal heart and pulmonary vasculature, Normal heart size and mediastinal contour, Normal heart size and pulmonary vascularity, Unremarkable heart and mediastinum
- Normal heart size and mediastinal contour -> Normal cardiomediastinal silhouette
- Normal heart size and pulmonary vascularity -> Normal heart and pulmonary vasculature
- Normally inflated and clear lungs -> Clear lungs
- Osteopenia -> 
- Possible pleural extension -> Blunted costophrenic angles, Blunted left costophrenic angle, Elevated right hemidiaphragm with right-sided pleural effusion, Large right pleural effusion with atelectasis, Small left pleural effusion
- Postop changes of CABG -> Intact sternotomy wires, Postoperative sternotomy changes, Status post sternotomy and CABG, Sternotomy changes
- Prior anterior cervical fusion -> 
- Relatively clear lungs -> Clear lungs
- Resolution of bibasilar infiltrates -> Improved right midlung opacity
- Retropulsion of L1 -> 
- Right chest tip at cavoatrial junction -> Central venous catheter, Surgical clips at thoracic inlet
- Right humeral head lucency -> Fracture of distal right clavicle
- Right lower lobe infiltrate -> Diffuse right lower lobe airspace opacity
- Right lung opacities -> Right lower lobe infiltrate
- S-shaped spine curvature -> Mild dextroscoliosis
- Small calcified lymph nodes -> Calcified hilar lymph nodes, Calcified hilar lymph nodes and granulomas
- Stable cardio mediastinal silhouette -> Normal cardiomediastinal silhouette
- Stable cardiomegaly -> Mild cardiomegaly
- Stable left mid lung granuloma -> Calcified granuloma, Calcified granuloma left upper lobe, Calcified granulomas, Stable small calcified granuloma left base
- Stable mediastinum -> Unremarkable mediastinum
- Stable mild interstitial opacities -> Diffuse bilateral interstitial and alveolar opacities
- Stable right chest wall pacemaker -> Stable coronary stent
- Stable small calcified granuloma left base -> Calcified granulomas
- Streaky bibasilar airspace opacities -> Angulate opacities
- Thoracic spondylosis -> Advanced degenerative changes, Arthritic changes of the spine, Degenerative changes in the spine, Degenerative changes of the midthoracic spine, Degenerative changes of the thoracic spine, Degenerative changes thoracic spine, Degenerative endplate changes of the spine, Denser lumbar scoliosis, Mild dextro curvature of the thoracic spine, Mild dextroscoliosis, Mild multilevel thoracolumbar degenerative disc disease, Minimal degenerative changes of the spine, Moderate degenerative changes of the thoracic spine, Multilevel degenerative changes in the spine, S-shaped spine curvature, Severe degenerative changes of the thoracic spine, Stable degenerative changes in the spine, T-spine osteophytes and DISH
- Tortuous descending thoracic aorta -> Tortuous thoracic aorta
- Tortuous thoracic aorta -> Mild unfolding of the thoracic aorta
- Tortuous/ectatic thoracic aorta -> Tortuous thoracic aorta
- Unchanged dense retrocardiac opacities -> Retrocardiac soft tissue density (possible hiatal hernia)
- Unremarkable mediastinal contour -> Unremarkable mediastinum
- Unremarkable mediastinum -> No mediastinal widening, Normal cardiac and mediastinal silhouettes, Normal cardiomediastinal silhouette, Normal mediastinal contours, Stable cardio mediastinal silhouette, Stable mediastinal contours, Stable mediastinum, Unremarkable cardio mediastinal silhouette
- Upper normal heart size -> Borderline enlarged heart
- Visualized osseous structures are unremarkable -> No acute bone abnormality, No acute bony abnormalities, No acute bony findings, No acute osseous findings, No bony abnormality, Normal osseous structures, Normal skeletal structures
### Métricas de evaluación

- **Total recuperados (Test expandido)**: 790
- **Relevantes recuperados (Gold→Test)**: 0
- **Relevantes totales (Gold expandido)**: 328
- **Precisión**: 0.00%
- **Recall**: 0.00%
- **F Score**: 0.00%
