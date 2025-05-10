# Evaluación de equivalencias

## Comparación de Findings entre JSONs

### En ambos JSONs:
- aortic unfolding
- cardiomegaly
- fracture of distal right clavicle
- lumbar degenerative disc disease
- pleural effusion

### Solo en V13/resultadoFinalNormal__7.json:

### Solo en V13/resultadoFinalNormalDocNN__7.json:
- advanced degenerative changes
- aortic calcifications
- arthritic changes of the spine
- atelectasis
- atherosclerotic calcifications
- calcification over the anterior mediastinum
- degenerative changes of both xxxx joints
- degenerative endplate changes of the spine
- effusion
- emphysema
- focal airspace disease
- hiatal hernia
- large breast mass
- lucency in the right humeral head
- minimal right middle lobe atelectasis
- pleural_effusion
- pneumothorax
- subsegmental atelectasis
- thoracic aortic atherosclerotic calcifications
- thoracic spondylosis
- tortuous thoracic aorta
- unidentified calcified lymph node

### JSON combinado de findings únicos (ordenado):
```json
[
    {"finding": "aortic unfolding"},
    {"finding": "cardiomegaly"},
    {"finding": "fracture of distal right clavicle"},
    {"finding": "lumbar degenerative disc disease"},
    {"finding": "pleural effusion"},
    {"finding": "advanced degenerative changes"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "aortic calcifications"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "arthritic changes of the spine"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "atelectasis"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "atherosclerotic calcifications"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "calcification over the anterior mediastinum"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "degenerative changes of both xxxx joints"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "degenerative endplate changes of the spine"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "effusion"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "emphysema"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "focal airspace disease"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "hiatal hernia"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "large breast mass"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "lucency in the right humeral head"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "minimal right middle lobe atelectasis"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pleural_effusion"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "pneumothorax"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "subsegmental atelectasis"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "thoracic aortic atherosclerotic calcifications"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "thoracic spondylosis"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "tortuous thoracic aorta"}, // Añadido desde la segunda pasada de los documentos
    {"finding": "unidentified calcified lymph node"} // Añadido desde la segunda pasada de los documentos
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
- Advanced degenerative changes -> advanced degenerative changes
- Angulate opacities -> 
- Anterior mediastinal calcification -> calcification over the anterior mediastinum
- Aortic calcifications -> aortic calcifications, atherosclerotic calcifications, thoracic aortic atherosclerotic calcifications
- Arthritic changes of the spine -> arthritic changes of the spine
- Atherosclerosis of the aorta -> aortic calcifications, atherosclerotic calcifications
- Atherosclerotic calcifications of the aorta -> aortic calcifications, atherosclerotic calcifications
- Biapical scarring -> 
- Bibasilar and perihilar interstitial opacities -> 
- Bibasilar pleural scarring -> 
- Bilateral interstitial opacities -> 
- Blunted costophrenic angles -> pleural effusion, pleural_effusion
- Blunted left costophrenic angle -> pleural effusion, pleural_effusion
- Borderline enlarged heart -> cardiomegaly
- Calcified granuloma -> 
- Calcified granuloma left upper lobe -> 
- Calcified granulomas -> 
- Calcified hilar lymph nodes -> unidentified calcified lymph node
- Calcified hilar lymph nodes and granulomas -> unidentified calcified lymph node
- Calcified thoracic aorta -> aortic calcifications, thoracic aortic atherosclerotic calcifications
- Cardiomegaly -> cardiomegaly
- Central vascular prominence -> 
- Central venous catheter -> 
- Chronic asymmetric elevation of the right hemidiaphragm -> 
- Chronic pleural-parenchymal scarring -> 
- Clear left lung -> 
- Clear lungs -> 
- Coarse interstitial markings -> 
- Degenerative changes in the spine -> arthritic changes of the spine
- Degenerative changes of the midthoracic spine -> thoracic spondylosis
- Degenerative changes of the spine -> arthritic changes of the spine, degenerative changes of both xxxx joints, degenerative endplate changes of the spine
- Degenerative changes thoracic spine -> thoracic spondylosis
- Degenerative endplate changes of the spine -> degenerative endplate changes of the spine
- Dense consolidation left lower lobe -> 
- Denser lumbar scoliosis -> 
- Diffuse bilateral interstitial and alveolar opacities -> 
- Diffuse right lower lobe airspace opacity -> 
- Drainage catheter right upper quadrant -> 
- Elevated left hemidiaphragm -> 
- Elevated right hemidiaphragm -> 
- Elevated right hemidiaphragm with right-sided pleural effusion -> pleural effusion, pleural_effusion
- Emphysema -> emphysema
- Enlarged cardiac silhouette -> cardiomegaly
- Enlarged heart -> cardiomegaly
- Extensive atherosclerotic disease -> aortic calcifications, atherosclerotic calcifications
- Extensive degenerative changes of the thoracic spine -> advanced degenerative changes
- Fracture of distal right clavicle -> fracture of distal right clavicle
- Grossly normal heart size -> 
- Hyperexpanded lungs -> emphysema
- Hyperinflated lungs -> emphysema
- Hyperinflated lungs (emphysema) -> emphysema
- Hyperinflation -> emphysema
- Improved right midlung opacity -> 
- Increased pulmonary vascularity -> 
- Increased streaky airspace disease right lung base -> 
- Intact sternotomy wires -> 
- Interval enlargement of the cardiac silhouette -> cardiomegaly
- Known large breast mass -> large breast mass
- Large heart size -> cardiomegaly
- Large hiatal hernia -> hiatal hernia
- Large right pleural effusion with atelectasis -> atelectasis, pleural effusion, pleural_effusion
- Left base scarring -> 
- Left base streaky opacity -> 
- Left basilar airspace opacities -> 
- Left lung base bandlike opacity (atelectasis) -> at
- Left midlung and basilar opacities (atelectasis) -> atelectasis
- Left midlung atelectasis or scar -> atelectasis
- Left perihilar upper lobe opacity -> 
- Lingula scarring -> 
- Lobulated opacity anterior mediastinum -> calcification over the anterior mediastinum
- Low lung volumes -> 
- Lucency right lung base (skin fold) -> 
- Mild anterior deformities L1-L2 -> 
- Mild cardiomegaly -> cardiomegaly
- Mild degenerative changes of the spine -> 
- Mild degenerative changes of the thoracic spine -> thoracic spondylosis
- Mild dextro curvature of the thoracic spine -> 
- Mild dextroscoliosis -> 
- Mild multilevel thoracolumbar degenerative disc disease -> lumbar degenerative disc disease
- Mild tortuosity of the thoracic aorta -> tortuous thoracic aorta
- Mild unfolding of the thoracic aorta -> aortic unfolding
- Mildly enlarged heart -> cardiomegaly
- Mildly hyperexpanded lungs -> emphysema
- Mildly hyperinflated lungs -> emphysema
- Mildly hyperlucent lungs -> emphysema
- Mildly low lung volumes -> 
- Minimal degenerative changes of the spine -> 
- Minimal left lung base densities -> 
- Minimal right middle lobe atelectasis -> minimal right middle lobe atelectasis, subsegmental atelectasis
- Minimal scarring or atelectasis right midlung -> minimal right middle lobe atelectasis, subsegmental atelectasis
- Moderate cardiomegaly -> cardiomegaly
- Moderate degenerative changes of the thoracic spine -> thoracic spondylosis
- Moderate hiatal hernia -> hiatal hernia
- Moderately enlarged heart -> cardiomegaly
- Multilevel degenerative changes in the spine -> advanced degenerative changes, degenerative changes of both xxxx joints, degenerative endplate changes of the spine
- No acute abnormality -> 
- No acute bone abnormality -> 
- No acute bony abnormalities -> 
- No acute bony findings -> 
- No acute findings -> 
- No acute infiltrate -> 
- No acute infiltrate or pleural effusion -> no pleural_effusion
- No acute osseous findings -> 
- No alveolar consolidation or pleural effusion -> no pleural_effusion
- No bony abnormality -> 
- No cardiac enlargement -> 
- No effusion or pneumothorax -> no pleural_effusion, no pneumothorax
- No focal air space opacity -> 
- No focal airspace consolidation -> 
- No focal airspace consolidations -> 
- No focal airspace disease -> no focal airspace disease
- No focal airspace opacities -> 
- No focal airspace opacity -> no focal airspace disease
- No focal consolidation -> 
- No focal consolidation or large pleural effusion -> no pleural_effusion
- No focal consolidation or pleural effusion -> no pleural_effusion
- No focal consolidation or pneumothorax -> no pneumothorax
- No focal infiltrate or suspicious opacity -> 
- No focal infiltrates -> 
- No focal lung consolidation -> 
- No focal pulmonary opacity -> 
- No large pleural effusion or pneumothorax -> no pleural_effusion, no pneumothorax
- No lobar consolidation -> 
- No mediastinal widening -> 
- No pleural effusion -> no pleural_effusion
- No pleural effusion or pneumothorax -> no pleural_effusion, no pneumothorax
- No pleural effusions -> no pleural_effusion
- No pleural effusions or pneumothoraces -> no pleural_effusion, no pneumothorax
- No pleural effusions or pneumothorax -> no pleural_effusion, no pneumothorax
- No pneumothorax -> no pneumothorax
- No pneumothorax or effusion -> no pleural_effusion, no pneumothorax
- No pneumothorax or large effusion -> no pleural_effusion, no pneumothorax
- No pneumothorax or large pleural effusion -> no pleural_effusion, no pneumothorax
- No pneumothorax or pleural effusion -> no pleural_effusion, no pneumothorax
- No pneumothorax or significant pulmonary edema -> no pneumothorax
- No suspicious pulmonary opacities -> 
- No vascular congestion -> 
- Normal cardiac and mediastinal silhouettes -> 
- Normal cardiac contours -> 
- Normal cardiomediastinal silhouette -> 
- Normal heart -> 
- Normal heart and mediastinum -> 
- Normal heart and pulmonary vasculature -> 
- Normal heart size -> 
- Normal heart size and mediastinal contour -> 
- Normal heart size and pulmonary vascularity -> 
- Normal mediastinal contours -> 
- Normal osseous structures -> 
- Normal pulmonary vascularity -> 
- Normal pulmonary vasculature -> 
- Normal skeletal structures -> 
- Normally inflated and clear lungs -> 
- Patchy airspace opacity right lung -> 
- Possible pleural extension -> pleural effusion, pleural_effusion
- Postop changes of CABG -> 
- Postoperative sternotomy changes -> 
- Prior anterior cervical fusion -> 
- Prominent ascending aorta (aneurysm) -> 
- Relatively clear lungs -> 
- Resolution of bibasilar infiltrates -> 
- Retrocardiac soft tissue density (possible hiatal hernia) -> hiatal hernia
- Retropulsion of L1 -> 
- Right chest tip at cavoatrial junction -> 
- Right humeral head lucency -> lucency in the right humeral head
- Right lower lobe infiltrate -> 
- Right lung base airspace disease/atelectasis -> atelectasis
- Right lung opacities -> 
- S-shaped spine curvature -> 
- Severe degenerative changes of the thoracic spine -> advanced degenerative changes
- Small calcified lymph nodes -> unidentified calcified lymph node
- Small circular opacities right upper lung -> 
- Small left pleural effusion -> pleural effusion, pleural_effusion
- Stable cardio mediastinal silhouette -> 
- Stable cardiomegaly -> cardiomegaly
- Stable coronary stent -> 
- Stable degenerative changes in the spine -> 
- Stable hilar prominence -> 
- Stable left mid lung granuloma -> 
- Stable mediastinal contours -> 
- Stable mediastinum -> 
- Stable mild interstitial opacities -> 
- Stable right chest wall pacemaker -> 
- Stable small calcified granuloma left base -> 
- Stable upper abdominal midline surgical sutures -> 
- Status post sternotomy and CABG -> 
- Sternotomy changes -> 
- Streaky bibasilar airspace opacities -> 
- Surgical clips at thoracic inlet -> 
- T-spine osteophytes and DISH -> 
- Thoracic aortic atherosclerotic calcifications -> aortic calcifications, atherosclerotic calcifications, thoracic aortic atherosclerotic calcifications
- Thoracic spondylosis -> thoracic spondylosis
- Tortuous aorta -> tortuous thoracic aorta
- Tortuous descending thoracic aorta -> tortuous thoracic aorta
- Tortuous thoracic aorta -> tortuous thoracic aorta
- Tortuous/calcified thoracic aorta -> tortuous thoracic aorta
- Tortuous/ectatic thoracic aorta -> tortuous thoracic aorta
- Unchanged dense retrocardiac opacities -> 
- Unfolded aorta -> aortic unfolding
- Unremarkable cardio mediastinal silhouette -> 
- Unremarkable heart and mediastinum -> 
- Unremarkable mediastinal contour -> 
- Unremarkable mediastinum -> 
- Upper normal heart size -> 
- Vague right upper lobe opacities -> 
- Vascular calcification -> aortic calcifications
- Visualized osseous structures are unremarkable -> 

## Equivalencias: Test → Test
- advanced degenerative changes -> degenerative changes of both xxxx joints, degenerative endplate changes of the spine
- aortic calcifications -> atherosclerotic calcifications, thoracic aortic atherosclerotic calcifications
- aortic unfolding -> tortuous thoracic aorta
- arthritic changes of the spine -> lumbar degenerative disc disease, thoracic spondylosis
- atelectasis -> minimal right middle lobe atelectasis, subsegmental atelectasis
- atherosclerotic calcifications -> aortic calcifications, thoracic aortic atherosclerotic calcifications
- calcification over the anterior mediastinum -> 
- cardiomegaly -> 
- degenerative changes of both xxxx joints -> degenerative endplate changes of the spine, lumbar degenerative disc disease
- degenerative endplate changes of the spine -> degenerative changes of both xxxx joints, lumbar degenerative disc disease
- effusion -> pleural effusion, pleural_effusion
- emphysema -> 
- focal airspace disease -> 
- fracture of distal right clavicle -> lucency in the right humeral head
- hiatal hernia -> 
- large breast mass -> 
- lucency in the right humeral head -> fracture of distal right clavicle
- lumbar degenerative disc disease -> degenerative changes of both xxxx joints, degenerative endplate changes of the spine
- minimal right middle lobe atelectasis -> atelectasis, subsegmental atelectasis
- pleural effusion -> effusion, pleural_effusion
- pleural_effusion -> effusion, pleural effusion
- pneumothorax -> 
- subsegmental atelectasis -> atelectasis, minimal right middle lobe atelectasis
- thoracic aortic atherosclerotic calcifications -> aortic calcifications, atherosclerotic calcifications
- thoracic spondylosis -> arthritic changes of the spine
- tortuous thoracic aorta -> aortic unfolding
- unidentified calcified lymph node -> 

## Equivalencias: Gold → Gold
- Advanced degenerative changes -> Severe degenerative changes of the thoracic spine
- Angulate opacities -> Bibasilar and perihilar interstitial opacities, Left basilar airspace opacities, Patchy airspace opacity right lung, Streaky bibasilar airspace opacities
- Anterior mediastinal calcification -> Lobulated opacity anterior mediastinum
- Aortic calcifications -> Atherosclerosis of the aorta, Atherosclerotic calcifications of the aorta, Thoracic aortic atherosclerotic calcifications
- Arthritic changes of the spine -> Degenerative changes of the spine
- Atherosclerosis of the aorta -> Aortic calcifications
- Atherosclerotic calcifications of the aorta -> Aortic calcifications
- Biapical scarring -> Lingula scarring
- Bibasilar and perihilar interstitial opacities -> Angulate opacities
- Bibasilar pleural scarring -> Lingula scarring
- Bilateral interstitial opacities -> Diffuse bilateral interstitial and alveolar opacities
- Blunted costophrenic angles -> Possible pleural extension
- Blunted left costophrenic angle -> Possible pleural extension
- Borderline enlarged heart -> Mild cardiomegaly
- Calcified granuloma -> Calcified granulomas
- Calcified granuloma left upper lobe -> Calcified granuloma
- Calcified granulomas -> Calcified granuloma
- Calcified hilar lymph nodes -> Small calcified lymph nodes
- Calcified hilar lymph nodes and granulomas -> Calcified hilar lymph nodes
- Calcified thoracic aorta -> Aortic calcifications
- Cardiomegaly -> Enlarged heart
- Central vascular prominence -> Increased pulmonary vascularity, Prominent ascending aorta (aneurysm)
- Central venous catheter -> Drainage catheter right upper quadrant
- Chronic asymmetric elevation of the right hemidiaphragm -> Elevated right hemidiaphragm
- Chronic pleural-parenchymal scarring -> Lingula scarring
- Clear left lung -> Clear lungs
- Clear lungs -> Clear left lung, No acute infiltrate, Normally inflated and clear lungs, Relatively clear lungs
- Coarse interstitial markings -> Diffuse bilateral interstitial and alveolar opacities
- Degenerative changes in the spine -> Thoracic spondylosis
- Degenerative changes of the midthoracic spine -> Thoracic spondylosis
- Degenerative changes of the spine -> Thoracic spondylosis
- Degenerative changes thoracic spine -> Thoracic spondylosis
- Degenerative endplate changes of the spine -> Degenerative changes of the spine
- Dense consolidation left lower lobe -> 
- Denser lumbar scoliosis -> Mild dextroscoliosis, S-shaped spine curvature
- Diffuse bilateral interstitial and alveolar opacities -> Bilateral interstitial opacities, Coarse interstitial markings, Stable mild interstitial opacities
- Diffuse right lower lobe airspace opacity -> Right lower lobe infiltrate
- Drainage catheter right upper quadrant -> Central venous catheter
- Elevated left hemidiaphragm -> Chronic asymmetric elevation of the right hemidiaphragm, Elevated right hemidiaphragm
- Elevated right hemidiaphragm -> Chronic asymmetric elevation of the right hemidiaphragm
- Elevated right hemidiaphragm with right-sided pleural effusion -> Large right pleural effusion with atelectasis
- Emphysema -> Hyperinflated lungs (emphysema)
- Enlarged cardiac silhouette -> Large heart size
- Enlarged heart -> Cardiomegaly, Mildly enlarged heart
- Extensive atherosclerotic disease -> Aortic calcifications
- Extensive degenerative changes of the thoracic spine -> Severe degenerative changes of the thoracic spine
- Fracture of distal right clavicle -> 
- Grossly normal heart size -> Normal heart size
- Hyperexpanded lungs -> Hyperinflated lungs
- Hyperinflated lungs -> Mildly hyperinflated lungs
- Hyperinflated lungs (emphysema) -> Hyperinflated lungs
- Hyperinflation -> Hyperinflated lungs
- Improved right midlung opacity -> Resolution of bibasilar infiltrates
- Increased pulmonary vascularity -> Central vascular prominence
- Increased streaky airspace disease right lung base -> Right lung base airspace disease/atelectasis
- Intact sternotomy wires -> Sternotomy changes
- Interval enlargement of the cardiac silhouette -> Enlarged cardiac silhouette
- Known large breast mass -> 
- Large heart size -> Cardiomegaly, Enlarged cardiac silhouette, Enlarged heart
- Large hiatal hernia -> Moderate hiatal hernia
- Large right pleural effusion with atelectasis -> Elevated right hemidiaphragm with right-sided pleural effusion
- Left base scarring -> Lingula scarring
- Left base streaky opacity -> Minimal left lung base densities
- Left basilar airspace opacities -> Left base streaky opacity, Left midlung and basilar opacities (atelectasis)
- Left lung base bandlike opacity (atelectasis) -> Left basilar airspace opacities
- Left midlung and basilar opacities (atelectasis) -> Left basilar airspace opacities
- Left midlung atelectasis or scar -> Minimal scarring or atelectasis right midlung
- Left perihilar upper lobe opacity -> Vague right upper lobe opacities
- Lingula scarring -> Biapical scarring, Bibasilar pleural scarring, Chronic pleural-parenchymal scarring, Left base scarring, Minimal scarring or atelectasis right midlung
- Lobulated opacity anterior mediastinum -> Anterior mediastinal calcification
- Low lung volumes -> Mildly low lung volumes
- Lucency right lung base (skin fold) -> 
- Mild anterior deformities L1-L2 -> 
- Mild cardiomegaly -> Borderline enlarged heart, Cardiomegaly, Enlarged cardiac silhouette, Enlarged heart, Mildly enlarged heart, Moderate cardiomegaly
- Mild degenerative changes of the spine -> Thoracic spondylosis
- Mild degenerative changes of the thoracic spine -> Degenerative changes thoracic spine, Thoracic spondylosis
- Mild dextro curvature of the thoracic spine -> Mild dextroscoliosis
- Mild dextroscoliosis -> Mild dextro curvature of the thoracic spine
- Mild multilevel thoracolumbar degenerative disc disease -> Degenerative changes of the spine
- Mild tortuosity of the thoracic aorta -> Tortuous thoracic aorta
- Mild unfolding of the thoracic aorta -> Mild tortuosity of the thoracic aorta, Tortuous aorta, Tortuous thoracic aorta, Tortuous/calcified thoracic aorta, Tortuous/ectatic thoracic aorta, Unfolded aorta
- Mildly enlarged heart -> Borderline enlarged heart, Cardiomegaly, Enlarged heart, Mild cardiomegaly
- Mildly hyperexpanded lungs -> Mildly hyperinflated lungs
- Mildly hyperinflated lungs -> Hyperexpanded lungs, Hyperinflated lungs, Hyperinflated lungs (emphysema), Mildly hyperexpanded lungs
- Mildly hyperlucent lungs -> Mildly hyperinflated lungs
- Mildly low lung volumes -> Low lung volumes
- Minimal degenerative changes of the spine -> Mild degenerative changes of the thoracic spine
- Minimal left lung base densities -> Left base streaky opacity
- Minimal right middle lobe atelectasis -> Minimal scarring or atelectasis right midlung
- Minimal scarring or atelectasis right midlung -> Left midlung atelectasis or scar, Minimal right middle lobe atelectasis
- Moderate cardiomegaly -> Cardiomegaly
- Moderate degenerative changes of the thoracic spine -> Thoracic spondylosis
- Moderate hiatal hernia -> Large hiatal hernia
- Moderately enlarged heart -> Cardiomegaly
- Multilevel degenerative changes in the spine -> Advanced degenerative changes, Severe degenerative changes of the thoracic spine
- No acute abnormality -> No acute findings
- No acute bone abnormality -> No acute bony findings
- No acute bony abnormalities -> No acute bone abnormality
- No acute bony findings -> No acute bone abnormality
- No acute findings -> No acute abnormality
- No acute infiltrate -> No acute infiltrate or pleural effusion
- No acute infiltrate or pleural effusion -> No acute findings, No acute infiltrate
- No acute osseous findings -> No acute bone abnormality
- No alveolar consolidation or pleural effusion -> No focal consolidation
- No bony abnormality -> No acute bone abnormality
- No cardiac enlargement -> Normal heart size
- No effusion or pneumothorax -> No pleural effusion or pneumothorax
- No focal air space opacity -> No focal airspace consolidations, No focal airspace disease, No focal airspace opacities, No focal airspace opacity, No focal lung consolidation, No focal pulmonary opacity
- No focal airspace consolidation -> No focal consolidation
- No focal airspace consolidations -> No focal consolidation
- No focal airspace disease -> No focal air space opacity
- No focal airspace opacities -> No focal air space opacity
- No focal airspace opacity -> No focal air space opacity
- No focal consolidation -> No alveolar consolidation, No focal airspace consolidation, No focal consolidation or pleural effusion, No lobar consolidation
- No focal consolidation or large pleural effusion -> No focal consolidation
- No focal consolidation or pleural effusion -> No focal consolidation
- No focal consolidation or pneumothorax -> No focal consolidation
- No focal infiltrate or suspicious opacity -> No suspicious pulmonary opacities
- No focal infiltrates -> No acute infiltrate, No focal infiltrate or suspicious opacity, No suspicious pulmonary opacities
- No focal lung consolidation -> No focal consolidation
- No focal pulmonary opacity -> No focal air space opacity
- No large pleural effusion or pneumothorax -> No pneumothorax or large pleural effusion
- No lobar consolidation -> No focal consolidation
- No mediastinal widening -> 
- No pleural effusion -> No pleural effusions
- No pleural effusion or pneumothorax -> No effusion or pneumothorax, No pleural effusions, No pleural effusions or pneumothoraces, No pneumothorax, No pneumothorax or effusion, No pneumothorax or pleural effusion
- No pleural effusions -> No pleural effusion, No small left pleural effusion
- No pleural effusions or pneumothoraces -> No pleural effusion or pneumothorax
- No pleural effusions or pneumothorax -> No pleural effusion or pneumothorax
- No pneumothorax -> No pneumothorax or effusion, No pneumothorax or large pleural effusion
- No pneumothorax or effusion -> No pleural effusion or pneumothorax
- No pneumothorax or large effusion -> No pneumothorax or large pleural effusion
- No pneumothorax or large pleural effusion -> No pneumothorax or large effusion
- No pneumothorax or pleural effusion -> No pneumothorax or large effusion
- No pneumothorax or significant pulmonary edema -> No pneumothorax
- No suspicious pulmonary opacities -> No acute infiltrate, No focal infiltrate or suspicious opacity
- No vascular congestion -> Normal pulmonary vascularity
- Normal cardiac and mediastinal silhouettes -> Normal cardiomediastinal silhouette
- Normal cardiac contours -> Normal cardiac and mediastinal silhouettes, Normal cardiomediastinal silhouette, Normal heart size
- Normal cardiomediastinal silhouette -> Stable cardio mediastinal silhouette, Unremarkable cardio mediastinal silhouette
- Normal heart -> Normal heart size
- Normal heart and mediastinum -> Unremarkable heart and mediastinum
- Normal heart and pulmonary vasculature -> No vascular congestion, Normal pulmonary vascularity
- Normal heart size -> Grossly normal heart size, No cardiac enlargement, Normal cardiac contours, Normal heart, Normal heart size and mediastinal contour, Normal heart size and pulmonary vascularity
- Normal heart size and mediastinal contour -> Normal cardiomediastinal silhouette
- Normal heart size and pulmonary vascularity -> Normal heart and pulmonary vasculature
- Normal mediastinal contours -> Unremarkable mediastinum
- Normal osseous structures -> Visualized osseous structures are unremarkable
- Normal pulmonary vascularity -> Normal heart and pulmonary vasculature
- Normal pulmonary vasculature -> Normal heart and pulmonary vasculature
- Normal skeletal structures -> Visualized osseous structures are unremarkable
- Normally inflated and clear lungs -> Clear lungs
- Osteopenia -> 
- Patchy airspace opacity right lung -> Right lung opacities
- Possible pleural extension -> Blunted costophrenic angles, Small left pleural effusion
- Postop changes of CABG -> Status post sternotomy and CABG
- Postoperative sternotomy changes -> Sternotomy changes
- Prior anterior cervical fusion -> 
- Prominent ascending aorta (aneurysm) -> 
- Relatively clear lungs -> Clear lungs
- Resolution of bibasilar infiltrates -> Improved right midlung opacity
- Retrocardiac soft tissue density (possible hiatal hernia) -> 
- Retropulsion of L1 -> 
- Right chest tip at cavoatrial junction -> Surgical clips at thoracic inlet
- Right humeral head lucency -> 
- Right lower lobe infiltrate -> Diffuse right lower lobe airspace opacity
- Right lung base airspace disease/atelectasis -> Increased streaky airspace disease right lung base
- Right lung opacities -> Patchy airspace opacity right lung
- S-shaped spine curvature -> Denser lumbar scoliosis
- Severe degenerative changes of the thoracic spine -> Advanced degenerative changes
- Small calcified lymph nodes -> Calcified hilar lymph nodes, Calcified hilar lymph nodes and granulomas
- Small circular opacities right upper lung -> Vague right upper lobe opacities
- Small left pleural effusion -> Possible pleural extension
- Stable cardio mediastinal silhouette -> Normal cardiomediastinal silhouette
- Stable cardiomegaly -> Cardiomegaly
- Stable coronary stent -> 
- Stable degenerative changes in the spine -> Degenerative changes of the spine
- Stable hilar prominence -> 
- Stable left mid lung granuloma -> Calcified granuloma, Calcified granuloma left upper lobe, Calcified granulomas, Stable small calcified granuloma left base
- Stable mediastinal contours -> Stable mediastinum
- Stable mediastinum -> Unremarkable mediastinum
- Stable mild interstitial opacities -> Diffuse bilateral interstitial and alveolar opacities
- Stable right chest wall pacemaker -> 
- Stable small calcified granuloma left base -> Calcified granuloma
- Stable upper abdominal midline surgical sutures -> 
- Status post sternotomy and CABG -> Postop changes of CABG
- Sternotomy changes -> Postoperative sternotomy changes
- Streaky bibasilar airspace opacities -> Angulate opacities
- Surgical clips at thoracic inlet -> Right chest tip at cavoatrial junction
- T-spine osteophytes and DISH -> 
- Thoracic aortic atherosclerotic calcifications -> Aortic calcifications
- Thoracic spondylosis -> Degenerative changes of the thoracic spine, Degenerative changes thoracic spine, Mild degenerative changes of the thoracic spine
- Tortuous aorta -> Tortuous thoracic aorta
- Tortuous descending thoracic aorta -> Tortuous thoracic aorta
- Tortuous thoracic aorta -> Tortuous aorta
- Tortuous/calcified thoracic aorta -> Tortuous thoracic aorta
- Tortuous/ectatic thoracic aorta -> Tortuous thoracic aorta
- Unchanged dense retrocardiac opacities -> 
- Unfolded aorta -> Mild unfolding of the thoracic aorta
- Unremarkable cardio mediastinal silhouette -> Normal cardiomediastinal silhouette
- Unremarkable heart and mediastinum -> Normal heart and mediastinum
- Unremarkable mediastinal contour -> Unremarkable mediastinum
- Unremarkable mediastinum -> No mediastinal widening, Normal mediastinal contours, Stable mediastinal contours, Stable mediastinum, Unremarkable mediastinal contour
- Upper normal heart size -> Borderline enlarged heart
- Vague right upper lobe opacities -> Left perihilar upper lobe opacity
- Vascular calcification -> Aortic calcifications
- Visualized osseous structures are unremarkable -> No acute bone abnormality, No acute bony abnormalities, No acute bony findings, No bony abnormality, Normal osseous structures, Normal skeletal structures
### Métricas de evaluación (solo términos originales)

- **Total recuperados (Test)**: 91
- **Relevantes recuperados (Gold→Test, sin duplicados)**: 44
- **Relevantes totales (Gold)**: 328
- **Precisión**: 48.35%
- **Recall**: 13.41%
- **F Score**: 21.00%

### Métricas de evaluación (con expandidos, solo para referencia)

- **Total recuperados (Test expandido)**: 208
- **Relevantes totales (Gold expandido)**: 1023
- **Precisión**: 21.15%
- **Recall**: 4.30%
- **F Score**: 7.15%
