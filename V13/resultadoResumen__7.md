# Evaluación de equivalencias

## Comparación de Findings entre JSONs

### En ambos JSONs:
- aortic unfolding
- cardiomegaly
- fracture of distal right clavicle
- lumbar degenerative disc disease
- pleural effusion

### Solo en resultadoFinalNormal__7.json:

### Solo en resultadoFinalNormalDocNN__7.json:
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
    {"finding": "Mild cardiomegaly, Mild unfolding of the thoracic aorta, No focal air space opacity, No pleural effusion or pneumothorax, Visualized osseous structures are unremarkable"},
    {"finding": "Normal heart size, Unremarkable mediastinum, Lingula scarring, Clear lungs"},
    {"finding": "Normal heart size, Angulate opacities, No focal infiltrates"},
    {"finding": "No focal consolidation, No suspicious pulmonary opacities, Normal heart size, No pleural effusions, No pneumothorax, Stable left mid lung granuloma"},
    {"finding": "Normal cardiac contours, Clear lungs, Thoracic spondylosis"},
    {"finding": "Mildly enlarged heart, Elevated left hemidiaphragm, No acute infiltrate or pleural effusion, Unremarkable mediastinum"},
    {"finding": "Central vascular prominence, Diffuse bilateral interstitial and alveolar opacities, Left basilar airspace opacities, No pneumothorax, Large heart size"},
    {"finding": "Normal cardiomediastinal silhouette, Mildly hyperinflated lungs, Resolution of bibasilar infiltrates, Minimal scarring or atelectasis right midlung, No focal airspace disease, No pneumothorax or pleural effusion"},
    {"finding": "Clear lungs, Normal heart and pulmonary vasculature, Normal mediastinal contours, Mild degenerative changes of the thoracic spine"},
    {"finding": "Normal heart size, Stable mediastinal contours, Aortic calcifications, Small calcified lymph nodes, Emphysema, Left perihilar upper lobe opacity, Possible pleural extension, No pleural effusion or pneumothorax"},
    {"finding": "Normal heart size, Low lung volumes, No focal airspace opacity, No pleural effusion or pneumothorax, Multilevel degenerative changes in the spine"},
    {"finding": "Chronic asymmetric elevation of the right hemidiaphragm, Increased streaky airspace disease right lung base, Stable hilar prominence, No pneumothorax or large pleural effusion, Grossly normal heart size"},
    {"finding": "Clear lungs, No focal consolidation or pneumothorax, Unremarkable cardio mediastinal silhouette, Mild multilevel thoracolumbar degenerative disc disease, Stable upper abdominal midline surgical sutures"},
    {"finding": "Postop changes of CABG, Mild cardiomegaly, Right lower lobe infiltrate, Thoracic spondylosis"},
    {"finding": "Clear lungs, Normal cardiac and mediastinal silhouettes, Normal pulmonary vasculature, No pneumothorax or pleural effusion, Advanced degenerative changes, Right humeral head lucency"},
    {"finding": "Normal heart size, Unremarkable mediastinum, Mildly hyperlucent lungs, Denser lumbar scoliosis"},
    {"finding": "Enlarged heart, Thoracic aortic atherosclerotic calcifications, Dense consolidation left lower lobe, Patchy airspace opacity right lung, No pleural effusion or pneumothorax"},
    {"finding": "Clear lungs, No focal airspace consolidation, No pleural effusion or pneumothorax, Normal heart size and mediastinal contour, Degenerative changes of the spine"},
    {"finding": "Normal heart size, Stable mediastinum, Right chest tip at cavoatrial junction, No pneumothorax, Elevated right hemidiaphragm with right-sided pleural effusion, Vague right upper lobe opacities, Clear left lung, Drainage catheter right upper quadrant"},
    {"finding": "Hyperinflated lungs, Coarse interstitial markings, Chronic pleural-parenchymal scarring, No lobar consolidation, No pleural effusion or pneumothorax, Normal heart size"},
    {"finding": "Stable right chest wall pacemaker, Stable cardiomegaly, Calcified thoracic aorta, Stable mild interstitial opacities, Unchanged dense retrocardiac opacities, No pneumothorax or large effusion"},
    {"finding": "Mild cardiomegaly, Low lung volumes, No focal consolidation or large pleural effusion, No acute bone abnormality"},
    {"finding": "Mildly enlarged heart, Lobulated opacity anterior mediastinum, Tortuous/calcified thoracic aorta, Hyperexpanded lungs, No pneumothorax or pleural effusion, Severe degenerative changes of the thoracic spine"},
    {"finding": "Normal heart size, No focal airspace disease, No pleural effusion or pneumothorax, Vascular calcification"},
    {"finding": "Hyperexpanded lungs, No pleural effusions or pneumothoraces, Normal heart and mediastinum, Degenerative changes in the spine"},
    {"finding": "Normal cardiomediastinal silhouette, No focal airspace disease, No pleural effusion or pneumothorax, Large hiatal hernia"},
    {"finding": "Diffuse right lower lobe airspace opacity, No pleural effusion or pneumothorax, Normal heart and mediastinum, Normal skeletal structures"},
    {"finding": "Calcified granulomas, Calcified hilar lymph nodes, No focal consolidation, Normal heart size, No pleural effusions, No pneumothorax, Hyperexpanded lungs, Aortic calcifications, Degenerative changes thoracic spine"},
    {"finding": "Normal cardiomediastinal silhouette, Tortuous thoracic aorta, No focal consolidation, No pneumothorax or large pleural effusion, Mild degenerative changes of the thoracic spine"},
    {"finding": "Mildly enlarged heart, Tortuous aorta, Aortic calcifications, No focal consolidation, No pleural effusion or pneumothorax, Extensive degenerative changes of the thoracic spine"},
    {"finding": "Normal heart size, No focal airspace consolidation, No pneumothorax or large pleural effusion, Mild degenerative changes of the thoracic spine"},
    {"finding": "Mild cardiomegaly, No pneumothorax or significant pulmonary edema, Small left pleural effusion, No focal lung consolidation, Mildly low lung volumes"},
    {"finding": "No acute abnormality, Normal heart size, Mild tortuosity of the thoracic aorta"},
    {"finding": "Mildly hyperexpanded lungs, No focal airspace consolidation, No pleural effusion or pneumothorax, Normal heart size and mediastinal contour"},
    {"finding": "Normal heart size, No focal airspace consolidations, No pleural effusion, Degenerative changes of the midthoracic spine"},
    {"finding": "Normal heart size, Stable coronary stent, Sternotomy changes, No focal consolidation or pneumothorax, Mild degenerative changes of the thoracic spine"},
    {"finding": "Normal heart size, No mediastinal widening, Clear lungs, No large pleural effusion or pneumothorax, Mild dextro curvature of the thoracic spine"},
    {"finding": "Postoperative sternotomy changes, Cardiomegaly, Prominent ascending aorta (aneurysm), Clear lungs, No focal consolidation, No pleural effusion or pneumothorax, Minimal degenerative changes of the spine"},
    {"finding": "Borderline enlarged heart, Tortuous/ectatic thoracic aorta, No focal pulmonary opacity, No pleural effusion or pneumothorax, Degenerative changes of the spine, Fracture of distal right clavicle"},
    {"finding": "Normal cardiomediastinal silhouette, Atherosclerosis of the aorta, Minimal left lung base densities, Hyperexpanded lungs, No focal consolidation or large pleural effusion, No acute bone abnormality"},
    {"finding": "Mildly enlarged heart, Low lung volumes, No focal consolidation or large pleural effusion, No acute bony abnormalities"},
    {"finding": "Normal heart size, Hyperinflated lungs (emphysema), Biapical scarring, No acute infiltrate"},
    {"finding": "Normal cardiomediastinal silhouette, Clear lungs, No focal consolidation or pleural effusion, Mild degenerative changes of the thoracic spine"},
    {"finding": "Normal heart size, Tortuous descending thoracic aorta, Central venous catheter, Elevated left hemidiaphragm, No pneumothorax or pleural effusion"},
    {"finding": "Stable cardiomegaly, Tortuous aorta, No focal airspace opacities, No pleural effusion or pneumothorax, Mild degenerative changes of the thoracic spine"},
    {"finding": "Moderate cardiomegaly, Bibasilar and perihilar interstitial opacities, No pneumothorax, No pleural effusions"},
    {"finding": "Clear left lung, Large right pleural effusion with atelectasis, Right lung opacities, No focal consolidation or pneumothorax, Stable cardio mediastinal silhouette"},
    {"finding": "Mildly enlarged heart, Increased pulmonary vascularity, Elevated right hemidiaphragm, Right lung base airspace disease/atelectasis, Left base streaky opacity, Blunted costophrenic angles"},
    {"finding": "Calcified granuloma left upper lobe, Normal heart size and pulmonary vascularity, Unremarkable mediastinal contour, No focal consolidation or pleural effusion, No acute bony findings"},
    {"finding": "No cardiac enlargement, No vascular congestion, Small circular opacities right upper lung, No bony abnormality"},
    {"finding": "Enlarged cardiac silhouette, Thoracic aortic atherosclerotic calcifications, Status post sternotomy and CABG, Left midlung atelectasis or scar, Blunted left costophrenic angle, No pneumothorax"},
    {"finding": "Surgical clips at thoracic inlet, Left base scarring, Clear lungs, No pleural effusion or pneumothorax, Normal heart and mediastinum, Normal skeletal structures"},
    {"finding": "Clear lungs, Hyperinflation, Anterior mediastinal calcification, Normal heart, Arthritic changes of the spine"},
    {"finding": "Normal heart size, Atherosclerotic calcifications of the aorta, Stable mediastinum, Known large breast mass, No pleural effusion"},
    {"finding": "Upper normal heart size, Minimal right middle lobe atelectasis, No focal consolidation or pleural effusion, Degenerative endplate changes of the spine"},
    {"finding": "Interval enlargement of the cardiac silhouette, Normally inflated and clear lungs, Normal osseous structures"},
    {"finding": "Low lung volumes, Normal cardiomediastinal silhouette, Streaky bibasilar airspace opacities, No pleural effusion or pneumothorax, No acute osseous findings"},
    {"finding": "Normal cardiac contours, Hyperinflated lungs, No focal consolidation, Thoracic spondylosis, Mild dextroscoliosis, Prior anterior cervical fusion"},
    {"finding": "Mildly enlarged heart, Stable mediastinal contours, Clear lungs"},
    {"finding": "Stable small calcified granuloma left base, No acute findings"},
    {"finding": "Unremarkable heart and mediastinum, Calcified granuloma left upper lobe, Clear lungs, No effusion or pneumothorax, Mild anterior deformities L1-L2, Retropulsion of L1"},
    {"finding": "Moderate cardiomegaly, Bilateral interstitial opacities, No focal airspace consolidation, No pleural effusions or pneumothorax, No acute bony abnormalities"},
    {"finding": "Normal cardiomediastinal silhouette, Tortuous thoracic aorta, No focal consolidation, No pneumothorax or pleural effusion, Moderate degenerative changes of the thoracic spine"},
    {"finding": "Normal heart size, No focal airspace disease, Emphysema, Bibasilar pleural scarring, No pneumothorax or effusion"},
    {"finding": "Normal heart size, Normal pulmonary vascularity, No pneumothorax or pleural effusion, No focal airspace opacities, Mild degenerative changes of the thoracic spine"},
    {"finding": "Normal cardiomediastinal silhouette, No focal consolidation or pleural effusion, Calcified hilar lymph nodes and granulomas, Stable degenerative changes in the spine"},
    {"finding": "Relatively clear lungs, Normal heart size, Unfolded aorta, Moderate hiatal hernia, T-spine osteophytes and DISH"},
    {"finding": "Upper normal heart size, No focal infiltrate or suspicious opacity, No pneumothorax or pleural effusion, Lucency right lung base (skin fold), No acute bony findings"},
    {"finding": "Moderately enlarged heart, No pleural effusion or pneumothorax, Left midlung and basilar opacities (atelectasis), Improved right midlung opacity, Mild degenerative changes of the spine, Intact sternotomy wires, Extensive atherosclerotic disease"},
    {"finding": "Mildly enlarged heart, No alveolar consolidation or pleural effusion, No pneumothorax, S-shaped spine curvature"},
    {"finding": "Normal heart size, Retrocardiac soft tissue density (possible hiatal hernia), Vascular calcification, Calcified granuloma, Left lung base bandlike opacity (atelectasis), No pneumothorax or pleural effusion, Osteopenia"}
]
```
# Calculo de similitud


## Equivalencias: Gold → Test
- Aortic regurgitation (transcatheter) -> Moderate calcified granuloma left base
- Aortic regurgitation (tricuspid) -> No mention in Set A
- Aortic stenosis (right) -> Calculated narrowing of the right aorta
- Atrial septal defects (cardiac) -> Unremarkable heart size
- Atrial septal defects (cerebral) -> Unremarkable heart and mediastinum
- Atrial septal defects (lower cardinal) -> Unremarkable heart size
- BIPH -> No mention in Set A
- Bi papillary interstitial opacities -> No mention in Set A
- Bicuspid aortic valve -> Increased pulmonary vascularity, Moderate cardiomegaly
- Bicuspid aortic valve disease -> No mention in Set A
- Bipolar interstitial opacities -> No mention in Set A
- Calcification (interstitial) -> No mention in Set A
- Calcification (right base) -> Left base streaky opacity, Right lung opacities
- Calcification (right upper lobe) -> Calcified granuloma left upper lobe
- Calcification (serrations) -> No mention in Set A
- Calcified granuloma left upper lobe -> Calcified granuloma left base
- Calcified hilar lymph nodes and granulomas -> Calcified hilar lymph nodes and granulomas
- Calcified mediastinal contour -> Normal mediastinum
- Calcified mediastinoscopy -> No mention in Set A
- Calcified subcutaneous -> No mention in Set A
- Calcified truncal -> No mention in Set A
- Cardiomegality (moderate) -> Increased pulmonary vascularity, Moderate cardiomegaly
- Cardiomegality (superficial) -> No mention in Set A
- Cardiomegaly (moderate) -> Mild cardiomegaly, Moderate cardiomegality
- Cardiomegaly (right) -> Right midlung atelectasis or scar
- Cardiomegaly (sub-Q) -> No mention in Set A
- Cardiomegaly (superficial) -> No mention in Set A
- Catecholase (low) -> No mention in Set A
- Central aortic stenosis (right proximal) -> No mention in Set A
- Central aortic stenosis (right) -> Elevated right hemidiaphragm, Increased pulmonary vascularity
- Cervical costophrenic angle (blunted) -> Blunted costophrenic angles
- Cholangiocarcinoma (mucinous, slow-growing) -> No mention in Set A
- Cholecystitis (mild) -> Unremarkable heart size
- Collateral circulation (distal right) -> No mention in Set A
- Collateral circulation (proximal right) -> No mention in Set A
- Collusion (right) -> No mention in Set A
- Congenital heart disease (trisomy 18,6,13) -> No mention in Set A
- Congestive cardiomyopathy (right-sided) -> No mention in Set A
- Congestive heart failure (right-sided) -> No mention in Set A
- Continuing this process for each term, ensuring that I don't miss any similar terms and noting if a term from Set B doesn't have an equivalent in Set A by leaving it blank or marking it with "X -> ".
- Costophrenic angle (blunted) -> Blunted costophrenic angles
- Costophrenic angle (deformity) -> No mention in Set A
- Costophrenic angle (distended) -> No mention in Set A
- Cysticercas (malignant) -> No mention in Set A
- Dacryogastrectomy (left) -> No mention in Set A
- Diabetic cardiomyopathy -> No mention in Set A
- Diabetic cardiomyopathy, concentric pattern -> No mention in Set A
- Digitalis toxicity (high) -> No mention in Set A
- Echocardiogram -> No mention in Set A
- Echocardiographic findings -> No mention in Set A
- Ectopic atrial contraction -> No mention in Set A
- Ectopic second heart sound (right) -> No mention in Set A
- Erythromycin (40 mg orally, qd for 5 days) -> No mention in Set A
- Esophageal varices (right) -> No mention in Set A
- Fibroathermal degeneration (right) -> No mention in Set A
- Fibromatosis (right) -> No mention in Set A
- Focal intralesional septal defects (FISS) (right) -> No mention in Set A
- Fructose 6-phosphate dehydrogenase deficiency (mild) -> No mention in Set A
- Functional right-sidedness (mild) -> No mention in Set A
- G protein-coupled receptor kinase 9 (GSK3β) inhibition (10 µg orally twice daily) -> No mention in Set A
- Gait issues (waist-related) -> No mention in Set A
- Gastroesophageal reflux disease (GERD) -> No mention in Set A
- Glucocorticoid (dexamethasone, 25 mcg IV qam) -> No mention in Set A
- Gouty arthritis (right hip) -> No mention in Set A
- Heart failure (right-sided, pulmonary) -> Elevated right hemidiaphragm, elevated pulmonary artery pressure
- Heart failure (right-sided, pulmonary, variable degree) -> Elevated right hemidiaphragm, elevated pulmonary artery pressure
- Heart-to-heart fistula (right) -> No mention in Set A
- Histone deacetylase (HDAC) inhibitors (1 µg orally twice daily) -> No mention in Set A
- Hydroxyurea (25 mg orally twice daily) -> No mention in Set A
- Incidence of adenocarcinoma (right lung) -> No mention in Set A
- Incidence of bronchiectasis -> No mention in Set A
- Incidence of interstitial fibrosis (right) -> No mention in Set A
- Incidence of macrophages (right lung, effusion) -> No mention in Set A
- Incidence of multinucleoplasmic inclusion bodies (MIPs) (right) -> No mention in Set A
- Incidence of pseudoglandular (mucosal-like) hyperplasia (MGH) (right) -> No mention in Set A
- Incidence of small-intestinal metaplasia (right) -> No mention in Set A
- Incidence of smooth muscle variant adenocarcinoma (right lung) -> No mention in Set A
- Incidence of solid tumors (right) -> No mention in Set A
- Incidence of squamous cell carcinoma (right lung) -> No mention in Set A
- Incidence of undifferentiated serous SqC (right) -> No mention in Set A
- Incisional hernias, inguinal (left) -> No mention in Set A
- Incisional hernias, inguvalobular (left) -> No mention in Set A
- Infiltrative neurolysis (right) -> No mention in Set A
- Inflammation-related adenocarcinoma (right lung) -> No mention in Set A
- Initial presentation of adenocarcinoma (right lung) -> No mention in Set A
- Ischemia and infarction (right-sided) -> Elevated right hemidiaphragm, elevated pulmonary artery pressure
- Ischemic heart disease (right-sided) -> Elevated right hemidiaphragm, elevated pulmonary artery pressure
- Ischemic right-sidedness (moderate) -> No mention in Set A
- Ischemic right-sidedness (severe) -> No mention in Set A
- It's important to ensure that the matching is accurate and not based on incomplete information. If a term from Set B isn't found in Set A, I should note that as "X -> ".
- Iterative therapy with epoxygenase (right) -> No mention in Set A
- Lantibiotics (methylprednisolone, 50 mg IV qam every 8 hours) -> No mention in Set A
- Lymphocytes (right arm) -> No mention in Set A
- Lymphocytes, cytotoxic T-cell (right arm) -> No mention in Set A
- Lymphocytosis (broadly reactive, right arm) -> No mention in Set A
- Lymphocytosis, non-specific (right arm) -> No mention in Set A
- Mapping of left ventricular Epicardial MyoMap -> No mention in Set A
- Mapping of right ventricular Epicardial MyoMap -> No mention in Set A
- Methotrexate (5-FU, 100 mg orally every 8 hours) -> No mention in Set A
- Minimal residual disease (MRD) (low) -> No mention in Set A
- Modifludin (60 mcg IV once) -> No mention in Set A
- Molecular imaging (PET/CT with FDG-PET) (right) -> No mention in Set A
- Mutations (right, 47,13T inversion; +58 insertions, +29 deletions, +6 translocations and 47,12q33; -20 inversions) -> No mention in Set A
- Mutations (right, 47,13T inversion; +58 insertions, +29 deletions, +6 translocations) -> No mention in Set A
- Mutations, right-sided adenocarcinoma, 47,13T inversion; +58 insertions ... -> No mention in Set A
- Mutations, right-sided undifferentiated serous SqC, 47,12q33; -20 inversions -> No mention in Set A
- Nodal metastases (right) -> No mention in Set A
- Nomogram for survival prediction (right lung adenocarcinoma) -> No mention in Set A
- Non-invasive test (right-sidedness evaluation, DAS-Esopharynx) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Abdomen) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Breast) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Cervix) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Kidney) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Lung) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Malegen) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Salivary) -> No mention in Set A
- Non-invasive test, right-sidedness evaluation (DAS-Vaginal) -> No mention in Set A
- Normal karyotype (right) -> No mention in Set A
- Okay, so I'm looking at this user query where they've provided two sets of medical terms related to heart and lung conditions. They want me to match each term from the second set (X) with similar terms from the first set (Y, Z, etc.). The output should be lines like "X -> K" for each X., Y, Z
- Ovarian hyperplasia (left-sided) -> No mention in Set A
- Ovarian hyperplasia (right-sided) -> No mention in Set A
- Pancytopenia (mild) -> No mention in Set A
- Pancytopenia, mild, right arm -> No mention in Set A
- Paroxysmal nocturnal dyspnea (left-sided) -> No mention in Set A
- Pathology findings of MIPs (right) -> No mention in Set A
- Pathology findings of adenocarcinoma (right lung) -> No mention in Set A
- Pathology findings of bronchiectasis -> No mention in Set A
- Pathology findings of interstitial fibrosis (right) -> No mention in Set A
- Pathology findings of non-specific lymphocytes (right arm) -> No mention in Set A
- Pathology findings of undifferentiated serous SqC (right arm) -> No mention in Set A
- Physical examination findings of left-sidedness assessment (DAS-Esopharynx) -> No mention in Set A
- Physical examination findings, left-sidedness evaluation (DAS-Breast) -> No mention in Set A
- Physical examination findings, left-sidedness evaluation (DAS-Cervix) -> No mention in Set A
- Physical examination findings, left-sidedness evaluation (DAS-Kidney) -> No mention in Set A
- Physical examination findings, left-sidedness evaluation (DAS-Lung) -> No mention in Set A
- Physical examination findings, left-sidedness evaluation (DAS-Malegen) -> No mention in Set A
- Physical examination findings, left-sidedness evaluation (DAS-Salivary) -> No mention in Set A
- Physical examination findings, left-sidedness evaluation (DAS-Vaginal) -> No mention in Set A
- Posterior predictive model for overall survival prediction (right lung adenocarcinoma) -> No mention in Set A
- Pre-treatment right-sidedness assessment (MRD low) -> No mention in Set A
- Prophylaxis of epoxygenase treatment (right-sidedness) -> No mention in Set A
- RT (right-sidedness testing) for adenocarcinoma post-treatment -> No mention in Set A
- RT (right-sidedness testing) for undifferentiated serous SqC post-treatment -> No mention in Set A
- RT (right-sidedness treatment) for adenocarcinoma with 47,13T inversion ... -> No mention in Set A
- RT (right-sidedness treatment) for undifferentiated serous SqC (47,12q33; -20 inversions) -> No mention in Set A
- RT, right-sidedness testing for adenocarcinoma post-treatment -> No mention in Set A
- RT, right-sidedness testing for undifferentiated serous SqC post-treatment -> No mention in Set A
- RT, right-sidedness treatment presentation at diagnosis (MRD low) -> No mention in Set A
- RT, right-sidedness treatment: pre-treatment MRD low -> No mention in Set A
- Right-sidedness assessment, MRD low (pre-treatment) -> No mention in Set A
- Right-sidedness assessment, pre-treatment (MRD low) -> No mention in Set A
- Right-sidedness presentation of adenocarcinoma with 47,13T inversion ... -> No mention in Set A
- Right-sidedness presentation of undifferentiated serous SqC, 47,12q33; -20 inversions -> No mention in Set A
- Right-sidedness presentation: pre-treatment (MRD low) -> No mention in Set A
- Right-sidedness test for adenocarcinoma (with 47,13T inversion ...) -> No mention in Set A
- Right-sidedness test for undifferentiated serous SqC (47,12q33; -20 inversions) -> No mention in Set A
- Right-sidedness test: pre-treatment (MRD low) -> No mention in Set A
- Right-sidedness test: presentation at diagnosis (MRD low) -> No mention in Set A
- Right-sidedness testing for adenocarcinoma (post-treatment) -> No mention in Set A
- Right-sidedness testing for undifferentiated serous SqC (post-treatment) -> No mention in Set A
- Right-sidedness testing: post-treatment -> No mention in Set A
- Right-sidedness testing: pre-treatment (MRD low) -> No mention in Set A
- Right-sidedness testing: presentation at diagnosis (MRD low) -> No mention in Set A
- Root cause analysis for right-sidedness, DAS-Esopharynx -> No mention in Set A
- Root cause analysis, right-sidedness evaluation (DAS-Breast) -> No mention in Set A
- Root cause analysis, right-sidedness evaluation (DAS-Cervix) -> No mention in Set A
- Root cause analysis, right-sidedness evaluation (DAS-Kidney) -> No mention in Set A
- Root cause analysis, right-sidedness evaluation (DAS-Lung) -> No mention in Set A
- Root cause analysis, right-sidedness evaluation (DAS-Malegen) -> No mention in Set A
- Root cause analysis, right-sidedness evaluation (DAS-Salivary) -> No mention in Set A
- Root cause analysis, right-sidedness evaluation (DAS-Vaginal) -> No mention in Set A
- SNP analysis: right-sidedness adenocarcinoma (47,13T inversion ...) -> No mention in Set A
- SNP analysis: right-sidedness undifferentiated serous SqC (47,12q33; -20 inversions) -> No mention in Set A
- Sample size calculation for overall survival prediction model (right lung adenocarcinoma) -> No mention in Set A
- Signature gene discovery (right-sidedness adenocarcinoma) -> No mention in Set A
- Signature gene discovery, right-sidedness undifferentiated serous SqC -> No mention in Set A
- Signature gene test for right-sidedness adenocarcinoma -> No mention in Set A
- Signature gene test for right-sidedness undifferentiated serous SqC -> No mention in Set A
- Signature gene testing (right-sidedness) adenocarcinoma -> No mention in Set A
- Signature gene testing, right-sidedness undifferentiated serous SqC -> No mention in Set A
- Subgroup analysis for overall survival prediction model (right lung adenocarcinoma) -> No mention in Set A
- Subgroups and their presentation: right-sidedness adenocarcinoma pre-treatment MRD low ... -> No mention in Set A
- Testing for undifferentiated serous SqC right-sidedness post-treatment -> No mention in Set A
- VITAMIN-B2 trial: overall survival with right-sidedness adenocarcinoma ... -> No mention in Set A
- Visualization of RT data (right-sidedness) adenocarcinoma with 47,13T inversion ... -> No mention in Set A
- Visualization of RT data, right-sidedness undifferentiated serous SqC (47,12q33; -20 inversions) -> No mention in Set A

## Equivalencias: Test → Test
- advanced degenerative changes -> aging-related changes, atherosclerosis
- aortic calcifications -> aortic stenosis, calcified plaques
- aortic unfolding -> no related terms
- arthritic changes of the spine -> gout, rheumatoid arthritis
- atelectasis -> air pocket formation, subsegmental atelectasis
- cardiomegaly -> pleural effusion
- fracture of distal right clavicle -> no related terms
- large breast mass -> breast cancer, breast neoplasm
- lucency in the right humeral head -> no related terms
- lumbar degenerative disc disease -> cervical disc degeneration, degenerative disc changes, disc degeneration
- minimal right middle lobe atelectasis -> no related terms
- pleural effusion -> ascites
- pleural_effusion -> ascites
- pneumothorax -> no related terms
- pulmonary calcifications -> pulmonary fibrosis
- subsegmental atelectasis -> partial atelectasis
- thoracic aortic atherosclerotic calcifications -> aortic calcifications, atherosclerosis
- thoracic spondylosis -> spinal stenosis
- tortuous thoracic aorta -> aortic tortuosity
- unidentified calcified lymph node -> no related terms

## Equivalencias: Gold → Gold
- Bibasilar and perihilar interstitial opacities -> Lung opacities, Specific opacity patterns
- Calcified granuloma left upper lobe -> Calcified granulomas
- Enlarged cardiac silhouette -> Cardiomegaly, Thoracic congestion
- Large right pleural effusion with atelectasis -> Pleural effusion
- Looking for terms like "Mild degenerative changes of the thoracic spine"—perhaps this could relate to other spine-related conditions or imaging findings. I should check if there's a better term than K. For each entry, list any synonyms or related medical terms in parentheses after X -> ..., K, Y, Z
- Mild degenerative changes of the thoracic spine -> Spine degeneration
- Right lung base airspace disease/atelectasis -> Atelectasis
- Small circular opacities right upper lung -> Interstitial opacities
- Thoracic aortic calcifications -> Aneurysmal changes, Atherosclerosis
### Métricas de evaluación

- **Total recuperados (Test expandido)**: 200
- **Relevantes recuperados (Gold→Test)**: 0
- **Relevantes totales (Gold expandido)**: 355
- **Precisión**: 0.00%
- **Recall**: 0.00%
- **F Score**: 0.00%
