import csv
import re

# -----------------------------------------------------------------------------
# 1. Define the data as a dictionary.
#    Each key is a disease (string) and its value is a list of symptom phrases.
# -----------------------------------------------------------------------------

data = {
    "Eczema": [
        "Itching",
        "skin rash",
        "nodal skin eruptions",
        "dischromic patches",
        "skin peeling",
        "scurring"
    ],
    "Psoriasis": [
        "Red, scaly skin",
        "skin rash",
        "dischromic patches",
        "nodal skin eruptions",
        "silver like dusting",
        "small dents in nails",
        "inflammatory nails",
        "scurring"
    ],
    "Contact Dermatitis": [
        "Itching",
        "skin rash",
        "blister",
        "red sore around nose",
        "yellow crust ooze"
    ],
    "Fungal Infections": [
        "Itching",
        "skin rash",
        "nodal skin eruptions",
        "dischromic patches",
        "skin peeling",
        "blisters"
    ],
    "Common Cold": [
        "Continuous sneezing",
        "shivering",
        "chills",
        "watering from eyes",
        "cough",
        "runny nose",
        "congestion"
    ],
    "Allergic Rhinitis": [
        "Continuous sneezing",
        "watering from eyes",
        "runny nose",
        "sinus pressure",
        "loss of smell"
    ],
    "Asthma": [
        "Shortness of breath",
        "chest pain",
        "cough",
        "wheezing",
        "fast heart rate"
    ],
    "Bronchitis": [
        "Cough",
        "chest pain",
        "mucoid sputum",
        "throat irritation",
        "fast heart rate",
        "breathlessness"
    ],
    "Pneumonia": [
        "Cough",
        "chest pain",
        "high fever",
        "chills",
        "rusty sputum",
        "breathlessness"
    ],
    "Sinusitis": [
        "Sinus pressure",
        "runny nose",
        "congestion",
        "headache",
        "throat irritation"
    ],
    "Gastroenteritis": [
        "Stomach pain",
        "vomiting",
        "diarrhoea",
        "nausea",
        "loss of appetite",
        "abdominal pain",
        "dehydration"
    ],
    "Peptic Ulcers": [
        "Stomach pain",
        "nausea",
        "vomiting",
        "loss of appetite",
        "indigestion",
        "internal itching"
    ],
    "Hepatitis": [
        "Yellowing of eyes",
        "yellowish skin",
        "abdominal pain",
        "nausea",
        "loss of appetite",
        "dark urine"
    ],
    "Irritable Bowel Syndrome (IBS)": [
        "Abdominal pain",
        "constipation",
        "diarrhoea",
        "bloating",
        "gas",
        "cramps"
    ],
    "Gallstones": [
        "Abdominal pain",
        "nausea",
        "vomiting",
        "yellowing of eyes",
        "indigestion"
    ],
    "Migraine": [
        "Headache",
        "dizziness",
        "nausea",
        "sensitivity to light",
        "visual disturbances"
    ],
    "Meningitis": [
        "Stiff neck",
        "high fever",
        "headache",
        "vomiting",
        "altered sensorium",
        "sensitivity to light"
    ],
    "Stroke": [
        "Sudden numbness or weakness",
        "confusion",
        "trouble speaking",
        "dizziness",
        "loss of balance",
        "weakness of one body side"
    ],
    "Anxiety Disorders": [
        "Palpitations",
        "restlessness",
        "sweating",
        "irritability",
        "dizziness",
        "muscle tension"
    ],
    "Epilepsy": [
        "Seizures",
        "loss of awareness",
        "staring spells",
        "temporary confusion",
        "altered sensorium"
    ],
    "Arthritis": [
        "Joint pain",
        "swelling",
        "stiffness",
        "muscle weakness",
        "painful walking",
        "movement stiffness"
    ],
    "Osteoarthritis": [
        "Joint pain",
        "stiffness",
        "reduced flexibility",
        "bone spurs",
        "swelling"
    ],
    "Fibromyalgia": [
        "Widespread musculoskeletal pain",
        "fatigue",
        "sleep disturbances",
        "headaches",
        "depression"
    ],
    "Muscle Strain": [
        "Muscle pain",
        "weakness",
        "swelling",
        "limited range of motion",
        "muscle spasms"
    ],
    "Diabetes Mellitus": [
        "Excessive hunger",
        "increased appetite",
        "polyuria",
        "weight loss",
        "blurred vision",
        "fatigue",
        "excessive thirst",
        "dry mouth"
    ],
    "Hyperthyroidism": [
        "Weight loss",
        "excessive hunger",
        "sweating",
        "palpitations",
        "irritability",
        "brittle nails",
        "puffy face and eyes"
    ],
    "Hypothyroidism": [
        "Weight gain",
        "fatigue",
        "cold intolerance",
        "dry skin",
        "puffy face",
        "hoarseness",
        "muscle weakness"
    ],
    "Systemic Lupus Erythematosus": [
        "Fatigue",
        "joint pain",
        "fever",
        "rash",
        "swollen lymph nodes",
        "malaise"
    ],
    "Chronic Fatigue Syndrome": [
        "Severe fatigue",
        "unrefreshing sleep",
        "muscle pain",
        "headaches",
        "sore throat",
        "difficulty concentrating"
    ],
    "Anemia": [
        "Fatigue",
        "weakness",
        "pale skin",
        "shortness of breath",
        "dizziness",
        "irregular heartbeats"
    ],
    "Hemophilia": [
        "Excessive bleeding",
        "easy bruising",
        "joint pain",
        "swelling",
        "blood in urine"
    ],
    "Leukemia": [
        "Fever",
        "fatigue",
        "frequent infections",
        "weight loss",
        "swollen lymph nodes",
        "easy bleeding"
    ],
    "Lymphoma": [
        "Swollen lymph nodes",
        "fatigue",
        "night sweats",
        "weight loss",
        "itching",
        "fever"
    ],
    "Heart Disease": [
        "Chest pain",
        "shortness of breath",
        "palpitations",
        "fatigue",
        "dizziness",
        "swollen extremities"
    ],
    "Hypertension": [
        "Often asymptomatic, but may include headaches",
        "shortness of breath",
        "nosebleeds",
        "dizziness"
    ],
    "Myocardial Infarction": [
        "Chest pain",
        "shortness of breath",
        "sweating",
        "nausea",
        "lightheadedness",
        "pain in arms or back"
    ],
    "Tuberculosis": [
        "Chronic cough",
        "blood in sputum",
        "chest pain",
        "fatigue",
        "weight loss",
        "fever",
        "night sweats",
        "loss of appetite"
    ],
    "Influenza (Flu)": [
        "High fever",
        "chills",
        "cough",
        "sore throat",
        "muscle aches",
        "fatigue",
        "headache",
        "nasal congestion",
        "runny nose"
    ],
    "COVID-19": [
        "Fever",
        "dry cough",
        "tiredness",
        "loss of taste or smell",
        "difficulty breathing",
        "chest pain",
        "headache",
        "sore throat",
        "congestion",
        "runny nose",
        "nausea",
        "diarrhea"
    ],
    "Rheumatoid Arthritis": [
        "Joint pain",
        "swelling",
        "stiffness",
        "fatigue",
        "fever",
        "loss of appetite"
    ],
    "Chronic Obstructive Pulmonary Disease (COPD)": [
        "Shortness of breath",
        "wheezing",
        "chest tightness",
        "chronic cough",
        "frequent respiratory infections",
        "fatigue",
        "blueness of lips or fingernail beds"
    ],
    "Celiac Disease": [
        "Diarrhea",
        "weight loss",
        "bloating",
        "gas",
        "abdominal pain",
        "fatigue",
        "anemia",
        "itchy rash (dermatitis herpetiformis)"
    ],
    "Multiple Sclerosis": [
        "Numbness or weakness in limbs",
        "partial or complete loss of vision",
        "double vision",
        "tingling or pain",
        "electric-shock sensations",
        "tremor",
        "lack of coordination",
        "unsteady gait",
        "fatigue"
    ],
    "Parkinson's Disease": [
        "Tremor",
        "slowed movement",
        "rigid muscles",
        "impaired posture and balance",
        "loss of automatic movements",
        "speech changes",
        "writing changes"
    ],
    "Systemic Scleroderma": [
        "Hardened or tightened patches of skin",
        "swollen fingers and hands",
        "Raynaud's phenomenon",
        "acid reflux",
        "difficulty swallowing",
        "joint pain",
        "shortness of breath"
    ],
    "Addison's Disease": [
        "Extreme fatigue",
        "weight loss",
        "decreased appetite",
        "darkening of skin",
        "low blood pressure",
        "salt craving",
        "low blood sugar",
        "nausea",
        "diarrhea",
        "vomiting",
        "abdominal pain",
        "muscle or joint pains"
    ],
    "Cushing's Syndrome": [
        "Weight gain",
        "pink or purple stretch marks",
        "thinning skin",
        "easy bruising",
        "acne",
        "fatigue",
        "muscle weakness",
        "high blood pressure",
        "bone loss",
        "diabetes"
    ],
    "Pancreatitis": [
        "Upper abdominal pain",
        "abdominal pain that radiates to the back",
        "tenderness when touching the abdomen",
        "fever",
        "rapid pulse",
        "nausea",
        "vomiting"
    ],
    "Gout": [
        "Intense joint pain",
        "lingering discomfort",
        "inflammation and redness",
        "limited range of motion"
    ],
    "Hypoglycemia": [
        "Shakiness",
        "dizziness",
        "sweating",
        "hunger",
        "irritability or moodiness",
        "anxiety or nervousness",
        "headache"
    ],
    "Hyperglycemia": [
        "Frequent urination",
        "increased thirst",
        "blurred vision",
        "fatigue",
        "headache",
        "fruity-smelling breath",
        "nausea",
        "vomiting",
        "shortness of breath",
        "dry mouth",
        "weakness",
        "confusion"
    ],
    "Sleep Apnea": [
        "Loud snoring",
        "episodes of breathing cessation during sleep",
        "abrupt awakenings with gasping or choking",
        "morning headache",
        "difficulty staying asleep",
        "excessive daytime sleepiness",
        "irritability"
    ],
    "HIV/AIDS": [
        "Fever",
        "chills",
        "rash",
        "night sweats",
        "muscle aches",
        "sore throat",
        "fatigue",
        "swollen lymph nodes",
        "mouth ulcers"
    ],
    "Lyme Disease": [
        "Fever",
        "headache",
        "fatigue",
        "skin rash (erythema migrans)",
        "joint pain",
        "heart palpitations",
        "dizziness",
        "inflammation of the brain and spinal cord"
    ],
    "Zika Virus": [
        "Fever",
        "rash",
        "headache",
        "joint pain",
        "conjunctivitis (red eyes)",
        "muscle pain"
    ],
    "Dengue Fever": [
        "High fever",
        "severe headache",
        "pain behind the eyes",
        "severe joint and muscle pain",
        "fatigue",
        "nausea",
        "vomiting",
        "skin rash"
    ],
    "Chikungunya": [
        "Fever",
        "joint pain",
        "muscle pain",
        "headache",
        "nausea",
        "fatigue",
        "rash"
    ],
    "Malaria": [
        "Fever",
        "chills",
        "headache",
        "nausea",
        "vomiting",
        "muscle pain",
        "fatigue",
        "sweating"
    ],
    "Typhoid Fever": [
        "High fever",
        "headache",
        "stomach pain",
        "constipation or diarrhea",
        "rose-colored spots on the body"
    ],
    "Mumps": [
        "Swollen salivary glands",
        "fever",
        "headache",
        "muscle aches",
        "tiredness",
        "loss of appetite"
    ],
    "Rubella (German Measles)": [
        "Mild fever",
        "headache",
        "stuffy or runny nose",
        "inflamed red eyes",
        "enlarged tender lymph nodes",
        "fine pink rash",
        "aching joints"
    ],
    "Measles": [
        "High fever",
        "dry cough",
        "runny nose",
        "sore throat",
        "inflamed eyes",
        "tiny white spots inside the mouth",
        "skin rash"
    ],
    "Chickenpox": [
        "Fever",
        "loss of appetite",
        "headache",
        "tiredness and malaise",
        "skin rash with itchy, fluid-filled blisters"
    ],
    "Acute Sinusitis": [
        "Nasal congestion",
        "thick yellow or green discharge from the nose",
        "facial pain and pressure",
        "headache",
        "fever",
        "cough",
        "fatigue",
        "toothache"
    ],
    "Chronic Sinusitis": [
        "Nasal congestion",
        "facial pain and pressure",
        "nasal obstruction",
        "thick discolored discharge",
        "reduced sense of smell and taste",
        "headache",
        "toothache",
        "fatigue"
    ],
    "Conjunctivitis (Pink Eye)": [
        "Redness in one or both eyes",
        "itching",
        "a gritty feeling",
        "discharge that forms a crust during the night",
        "tearing"
    ],
    "Otitis Media (Middle Ear Infection)": [
        "Ear pain",
        "fever",
        "fluid drainage from the ear",
        "hearing loss",
        "irritability in children",
        "difficulty sleeping"
    ],
    "Vertigo": [
        "Spinning sensation",
        "dizziness",
        "balance problems",
        "nausea",
        "vomiting",
        "headache",
        "sweating"
    ],
    "Hypoglycemia (Low Blood Sugar)": [
        "Shakiness",
        "dizziness",
        "sweating",
        "hunger",
        "irritability or moodiness",
        "anxiety or nervousness",
        "headache"
    ],
    "Hyperglycemia (High Blood Sugar)": [
        "Frequent urination",
        "increased thirst",
        "blurred vision",
        "fatigue",
        "headache",
        "fruity-smelling breath",
        "nausea",
        "vomiting",
        "shortness of breath"
    ],
    "Gastroesophageal Reflux Disease (GERD)": [
        "Heartburn",
        "regurgitation of food or sour liquid",
        "difficulty swallowing",
        "chest pain",
        "chronic cough",
        "laryngitis",
        "new or worsening asthma"
    ],
    "Peptic Ulcer Disease": [
        "Burning stomach pain",
        "bloating",
        "heartburn",
        "nausea",
        "intolerance to fatty foods"
    ],
    "Urinary Tract Infection (UTI)": [
        "Strong, persistent urge to urinate",
        "burning sensation when urinating",
        "passing frequent, small amounts of urine",
        "cloudy urine",
        "strong-smelling urine",
        "pelvic pain"
    ],
    "Bacterial Vaginosis": [
        "Thin, gray, white or green vaginal discharge",
        "foul-smelling fishy vaginal odor",
        "vaginal itching",
        "burning during urination"
    ],
    "Candida Infections (Thrush)": [
        "White patches on the tongue and inside of the mouth",
        "redness or soreness",
        "difficulty swallowing",
        "cracking and redness at the corners of the mouth"
    ],
    "Chlamydia": [
        "Painful urination",
        "lower abdominal pain",
        "vaginal discharge in women",
        "discharge from the penis in men",
        "painful sexual intercourse",
        "bleeding between periods",
        "testicular pain in men"
    ],
    "Gonorrhea": [
        "Painful urination",
        "abnormal discharge from the penis or vagina",
        "pain or swelling in one testicle",
        "increased vaginal bleeding",
        "anal itching",
        "soreness",
        "bleeding",
        "painful bowel movements"
    ],
    "Syphilis": [
        "Painless sores on the genitals, rectum or mouth",
        "rash",
        "swollen lymph nodes",
        "fever",
        "sore throat",
        "muscle aches",
        "fatigue",
        "weight loss",
        "headache"
    ],
    "Trichomoniasis": [
        "Frothy, greenish-yellow vaginal discharge",
        "strong vaginal odor",
        "vaginal itching or irritation",
        "discomfort during intercourse",
        "painful urination"
    ],
    "Herpes Simplex Virus (HSV)": [
        "Painful blisters or ulcers at the site of infection",
        "itching",
        "burning sensation",
        "flu-like symptoms",
        "swollen lymph nodes"
    ],
    "Human Papillomavirus (HPV)": [
        "Genital warts",
        "common warts",
        "plantar warts",
        "flat warts",
        "cervical dysplasia"
    ],
    "Human Immunodeficiency Virus (HIV)": [
        "Fever",
        "chills",
        "rash",
        "night sweats",
        "muscle aches",
        "sore throat",
        "fatigue",
        "swollen lymph nodes",
        "mouth ulcers"
    ],
    "Endometriosis": [
        "Painful periods (dysmenorrhea)",
        "pain during intercourse",
        "pain with bowel movements or urination",
        "excessive bleeding",
        "infertility",
        "fatigue",
        "diarrhea",
        "constipation",
        "bloating",
        "nausea"
    ],
    "Polycystic Ovary Syndrome (PCOS)": [
        "Irregular periods",
        "excess androgen",
        "polycystic ovaries",
        "weight gain",
        "thinning hair",
        "acne",
        "fertility issues"
    ],
    "Interstitial Cystitis (Painful Bladder Syndrome)": [
        "Chronic pelvic pain",
        "a persistent urgent need to urinate",
        "frequent urination",
        "pain during intercourse"
    ],
    "Irritable Bowel Syndrome (IBS)": [
        "Abdominal pain",
        "cramping",
        "bloating",
        "gas",
        "diarrhea",
        "constipation",
        "mucus in stool"
    ],
    "Celiac Disease": [
        "Diarrhea",
        "fatigue",
        "weight loss",
        "bloating",
        "gas",
        "abdominal pain",
        "nausea",
        "vomiting",
        "constipation"
    ],
    "Crohn's Disease": [
        "Diarrhea",
        "fever",
        "fatigue",
        "abdominal pain and cramping",
        "blood in stool",
        "mouth sores",
        "reduced appetite",
        "weight loss",
        "perianal disease"
    ],
    "Ulcerative Colitis": [
        "Diarrhea",
        "often with blood or pus",
        "abdominal pain and cramping",
        "rectal pain",
        "rectal bleeding",
        "urgency to defecate",
        "inability to defecate despite urgency",
        "weight loss",
        "fatigue",
        "fever"
    ],
    "Diverticulitis": [
        "Persistent pain, often in the lower left side of the abdomen",
        "nausea and vomiting",
        "fever",
        "abdominal tenderness",
        "constipation",
        "diarrhea"
    ],
    "Panic Disorder": [
        "Recurrent panic attacks",
        "sudden intense fear",
        "palpitations",
        "sweating",
        "trembling",
        "shortness of breath",
        "chest pain",
        "nausea",
        "dizziness",
        "fear of losing control"
    ],
    "Obsessive-Compulsive Disorder (OCD)": [
        "Recurrent, unwanted thoughts (obsessions)",
        "repetitive behaviors (compulsions)",
        "anxiety",
        "distress",
        "ritualistic behaviors"
    ],
    "Bipolar Disorder": [
        "Extreme mood swings",
        "manic episodes",
        "depressive episodes"
    ],
    "Schizophrenia": [
        "Hallucinations",
        "delusions",
        "disorganized thinking",
        "abnormal motor behavior",
        "negative symptoms"
    ],
    "Post-Traumatic Stress Disorder (PTSD)": [
        "Flashbacks",
        "nightmares",
        "severe anxiety",
        "uncontrollable thoughts about the traumatic event",
        "emotional numbness",
        "irritability"
    ],
    "Major Depressive Disorder": [
        "Persistent sadness",
        "loss of interest in activities",
        "changes in appetite",
        "changes in sleep patterns",
        "fatigue",
        "feelings of worthlessness",
        "difficulty concentrating"
    ],
    "Anorexia Nervosa": [
        "Extreme weight loss",
        "restricted eating",
        "intense fear of gaining weight",
        "distorted body image",
        "excessive exercise"
    ],
    "Bulimia Nervosa": [
        "Episodes of binge eating",
        "purging",
        "fear of gaining weight",
        "distorted body image"
    ],
    "Generalized Anxiety Disorder (GAD)": [
        "Excessive worry about various aspects of life",
        "restlessness",
        "fatigue",
        "difficulty concentrating",
        "irritability",
        "muscle tension",
        "sleep disturbances"
    ],
    "Social Anxiety Disorder": [
        "Intense fear of social situations",
        "avoidance of social interactions",
        "fear of being judged",
        "excessive self-consciousness",
        "physical symptoms (blushing, sweating)"
    ],
    "Seasonal Affective Disorder (SAD)": [
        "Depression that occurs at the same time each year",
        "typically in winter",
        "low energy",
        "hypersomnia",
        "overeating",
        "weight gain",
        "social withdrawal"
    ],
    "Borderline Personality Disorder (BPD)": [
        "Intense fear of abandonment",
        "unstable relationships",
        "impulsive behavior",
        "mood swings",
        "feelings of emptiness",
        "self-harm",
        "difficulty controlling anger"
    ],
    "Chronic Fatigue Syndrome (CFS)": [
        "Severe fatigue not improved by rest",
        "sleep problems",
        "difficulty with concentration and memory",
        "muscle and joint pain",
        "headaches",
        "sore throat",
        "swollen lymph nodes"
    ],
    "Raynaud's Phenomenon": [
        "Color changes in the skin in response to cold or stress (white, blue, then red)",
        "numbness",
        "tingling",
        "pain in fingers and toes"
    ],
    "Sjogren's Syndrome": [
        "Dry eyes",
        "dry mouth",
        "joint pain",
        "swelling",
        "fatigue",
        "persistent dry cough",
        "skin rashes",
        "vaginal dryness"
    ],
    "Systemic Lupus Erythematosus (SLE)": [
        "Fatigue",
        "fever",
        "joint pain",
        "skin rashes (especially butterfly-shaped rash on the face)",
        "photosensitivity",
        "mouth ulcers",
        "Raynaud's phenomenon",
        "chest pain"
    ],
    "Rheumatic Fever": [
        "Fever",
        "painful and tender joints",
        "red, hot or swollen joints",
        "small, painless nodules beneath the skin",
        "chest pain",
        "heart murmur",
        "fatigue",
        "flat or slightly raised painless rash with a ragged edge"
    ],
    "Psoriatic Arthritis": [
        "Joint pain",
        "stiffness",
        "swelling",
        "swollen fingers and toes",
        "foot pain",
        "lower back pain",
        "nail changes"
    ],
    "Scleroderma": [
        "Tightening and hardening of the skin",
        "Raynaud's phenomenon",
        "heartburn",
        "difficulty swallowing",
        "shortness of breath",
        "joint pain"
    ],
    "Hypersensitivity Pneumonitis": [
        "Shortness of breath",
        "cough",
        "fatigue",
        "chills",
        "muscle aches",
        "loss of appetite",
        "weight loss"
    ],
    "Sarcoidosis": [
        "Fatigue",
        "fever",
        "swollen lymph nodes",
        "weight loss",
        "shortness of breath",
        "persistent dry cough",
        "chest pain",
        "skin lesions"
    ],
    "Amyotrophic Lateral Sclerosis (ALS)": [
        "Muscle weakness",
        "twitching",
        "cramping",
        "difficulty speaking and swallowing",
        "difficulty breathing",
        "paralysis"
    ],
    "Huntington's Disease": [
        "Involuntary jerking movements",
        "muscle problems",
        "difficulty with speech and swallowing",
        "cognitive decline",
        "depression",
        "mood swings"
    ],
    "Motor Neurone Disease (MND)": [
        "Progressive muscle weakness",
        "slurred speech",
        "difficulty swallowing",
        "muscle cramps and twitches",
        "weight loss"
    ],
    "Myasthenia Gravis": [
        "Muscle weakness",
        "drooping of one or both eyelids",
        "double vision",
        "difficulty swallowing",
        "shortness of breath",
        "altered speech",
        "facial muscle weakness"
    ],
    "Ehlers-Danlos Syndrome (EDS)": [
        "Hypermobile joints",
        "stretchy skin",
        "fragile skin that bruises easily",
        "chronic pain",
        "scoliosis",
        "early-onset arthritis"
    ],
    "Marfan Syndrome": [
        "Tall and slender build",
        "disproportionately long arms, legs, fingers, and toes",
        "heart murmurs",
        "extreme nearsightedness",
        "abnormally curved spine",
        "flat feet"
    ],
    "Turner Syndrome": [
        "Short stature",
        "webbed neck",
        "low-set ears",
        "low hairline at the back of the neck",
        "swelling of hands and feet",
        "cardiac defects",
        "infertility"
    ],
    "Klinefelter Syndrome": [
        "Low testosterone",
        "reduced muscle mass",
        "reduced facial and body hair",
        "enlarged breast tissue",
        "tall stature",
        "learning disabilities",
        "delayed speech and language development"
    ],
    "Cystic Fibrosis": [
        "Persistent cough with thick mucus",
        "wheezing",
        "breathlessness",
        "repeated lung infections",
        "sinusitis",
        "poor growth",
        "weight gain despite good appetite",
        "frequent greasy, bulky stools"
    ],
    "Alport Syndrome": [
        "Progressive loss of kidney function",
        "hearing loss",
        "eye abnormalities"
    ],
    "Fabry Disease": [
        "Pain, particularly in the hands and feet",
        "clusters of small, dark red spots on the skin",
        "decreased sweating",
        "corneal opacity",
        "hearing loss",
        "kidney damage",
        "heart problems"
    ],
    "Hemochromatosis": [
        "Joint pain",
        "fatigue",
        "weakness",
        "diabetes",
        "loss of sex drive",
        "impotence",
        "heart failure",
        "liver failure",
        "bronze or gray skin color"
    ],
    "Wilson's Disease": [
        "Fatigue",
        "lack of appetite",
        "abdominal pain",
        "jaundice",
        "golden-brown eye discoloration (kayser-fleischer rings)",
        "fluid buildup in legs and abdomen",
        "uncontrolled movements",
        "muscle stiffness",
        "speech problems"
    ],
    "Phenylketonuria (PKU)": [
        "Intellectual disability",
        "delayed development",
        "behavioral problems",
        "psychiatric disorders",
        "musty odor in breath, skin or urine",
        "eczema",
        "fair skin and blue eyes"
    ],
    "Hyperparathyroidism": [
        "Fragile bones",
        "kidney stones",
        "excessive urination",
        "abdominal pain",
        "tiring easily or weakness",
        "depression or forgetfulness",
        "bone and joint pain",
        "nausea",
        "vomiting",
        "loss of appetite"
    ],
    "Hypoparathyroidism": [
        "Tingling or burning in fingertips, toes, and lips",
        "muscle aches or cramps",
        "twitching or spasms of muscles, particularly around the mouth, hands, arms, and throat",
        "fatigue or weakness",
        "painful menstrual periods",
        "patchy hair loss"
    ],
    "Addison's Disease": [
        "Extreme fatigue",
        "weight loss",
        "decreased appetite",
        "darkening of skin",
        "low blood pressure",
        "salt craving",
        "low blood sugar",
        "nausea",
        "diarrhea",
        "vomiting",
        "abdominal pain",
        "muscle or joint pains"
    ],
    "Cushing's Syndrome": [
        "Weight gain",
        "pink or purple stretch marks",
        "thinning skin",
        "easy bruising",
        "acne",
        "fatigue",
        "muscle weakness",
        "high blood pressure",
        "bone loss",
        "diabetes"
    ],
    "Graves' Disease": [
        "Anxiety and irritability",
        "tremor of hands or fingers",
        "heat sensitivity",
        "weight loss",
        "enlarged thyroid (goiter)",
        "bulging eyes",
        "fatigue",
        "thick, red skin on the shins or tops of the feet"
    ],
    "Hashimoto's Thyroiditis": [
        "Fatigue",
        "weight gain",
        "cold intolerance",
        "muscle weakness",
        "joint pain and stiffness",
        "constipation",
        "dry skin",
        "puffy face",
        "hoarseness"
    ],
    "Pheochromocytoma": [
        "High blood pressure",
        "headache",
        "sweating",
        "rapid heartbeat",
        "tremors",
        "shortness of breath",
        "panic attack-type symptoms"
    ],
    "Sarcoidosis": [
        "Fatigue",
        "fever",
        "swollen lymph nodes",
        "weight loss",
        "persistent dry cough",
        "shortness of breath",
        "chest pain",
        "skin lesions"
    ],
    "Wegener's Granulomatosis (Granulomatosis with Polyangiitis)": [
        "Sinus pain and drainage",
        "nasal or oral ulcers",
        "cough",
        "shortness of breath",
        "kidney issues",
        "joint pain",
        "rashes",
        "fever",
        "weight loss"
    ],
    "Giant Cell Arteritis": [
        "Headaches",
        "scalp tenderness",
        "jaw pain",
        "vision problems",
        "fever",
        "unintentional weight loss",
        "fatigue"
    ],
    "Takayasu's Arteritis": [
        "Fatigue",
        "unintended weight loss",
        "muscle and joint pain",
        "fever",
        "night sweats",
        "weak pulse",
        "high blood pressure",
        "chest pain"
    ],
    "Lupus Nephritis": [
        "Foamy urine",
        "high blood pressure",
        "swelling in legs, feet, or ankles",
        "joint pain and swelling",
        "skin rash",
        "fever",
        "fatigue"
    ],
    "Vasculitis": [
        "Fever",
        "headache",
        "fatigue",
        "weight loss",
        "muscle and joint pain",
        "numbness or weakness in a hand or foot",
        "rash"
    ],
    "Behcet's Disease": [
        "Mouth sores",
        "genital sores",
        "inflammation of parts of the eye",
        "skin problems",
        "joint pain",
        "blood vessel inflammation",
        "digestive issues"
    ],
    "Hepatitis A": [
        "Fatigue",
        "sudden nausea and vomiting",
        "abdominal pain",
        "clay-colored bowel movements",
        "loss of appetite",
        "low-grade fever",
        "dark urine",
        "joint pain",
        "jaundice"
    ],
    "Hepatitis B": [
        "Fatigue",
        "sudden nausea and vomiting",
        "abdominal pain",
        "loss of appetite",
        "low-grade fever",
        "dark urine",
        "joint pain",
        "jaundice"
    ],
    "Hepatitis C": [
        "Fatigue",
        "sudden nausea and vomiting",
        "abdominal pain",
        "loss of appetite",
        "low-grade fever",
        "dark urine",
        "joint pain",
        "jaundice"
    ],
    "Autoimmune Hepatitis": [
        "Fatigue",
        "enlarged liver",
        "jaundice",
        "itching",
        "skin rashes",
        "joint pain",
        "abdominal discomfort",
        "spider angiomas",
        "enlarged spleen"
    ],
    "Primary Biliary Cholangitis (PBC)": [
        "Fatigue",
        "itchy skin",
        "dry eyes and mouth",
        "pain in the upper right abdomen",
        "swelling of the feet and ankles",
        "fluid buildup in the abdomen",
        "yellowing of the skin and eyes (jaundice)"
    ],
    "Hemolytic Anemia": [
        "Fatigue",
        "dizziness",
        "paleness",
        "shortness of breath",
        "dark urine",
        "jaundice",
        "fever",
        "weakness",
        "heart murmur"
    ],
    "Myelodysplastic Syndromes (MDS)": [
        "Fatigue",
        "shortness of breath",
        "unusual paleness (pallor) due to anemia",
        "easy or unusual bruising or bleeding",
        "frequent infections"
    ],
    "Aplastic Anemia": [
        "Fatigue",
        "shortness of breath",
        "rapid or irregular heart rate",
        "pale skin",
        "frequent or prolonged infections",
        "unexplained or easy bruising",
        "nosebleeds and bleeding gums",
        "prolonged bleeding from cuts",
        "skin rash"
    ],
    "Duchenne Muscular Dystrophy (DMD)": [
        "Progressive muscle weakness",
        "frequent falls",
        "difficulty rising from a lying or sitting position",
        "trouble running and jumping",
        "large calf muscles",
        "learning disabilities"
    ],
    "Becker Muscular Dystrophy (BMD)": [
        "Muscle weakness",
        "delayed motor development",
        "difficulty walking",
        "frequent falls",
        "muscle cramps",
        "enlarged calves"
    ],
    "Charcot-Marie-Tooth Disease (CMT)": [
        "Weakness in legs, ankles, and feet",
        "loss of muscle bulk in legs and feet",
        "high foot arches",
        "curled toes",
        "difficulty lifting the foot",
        "decreased ability to run",
        "foot drop",
        "frequent tripping or falling"
    ]
}

# -----------------------------------------------------------------------------
# 2. Define a helper function to format each symptom:
#    - Convert to lowercase
#    - Replace spaces with underscores
#    - Remove commas (if any)
#    - Remove content inside parentheses
# -----------------------------------------------------------------------------

def format_symptom(symptom):
    s = symptom.strip().lower()
    # Remove commas
    s = s.replace(",", "")
    # Remove parentheses and their contents
    s = re.sub(r'\(.*?\)', '', s)
    # Replace spaces with underscores
    s = s.replace(" ", "_")
    # Replace multiple underscores with one
    s = re.sub(r'_+', '_', s)
    # Remove leading/trailing underscores
    return s.strip('_')

# -----------------------------------------------------------------------------
# 3. Build a list of rows.
#    For each disease, join the formatted symptoms with commas.
# -----------------------------------------------------------------------------

rows = []
for disease, symptom_list in data.items():
    formatted_symptoms = [format_symptom(sym) for sym in symptom_list]
    # Remove duplicate symptom keywords (if any) while preserving order
    seen = set()
    unique_symptoms = []
    for sym in formatted_symptoms:
        if sym not in seen:
            seen.add(sym)
            unique_symptoms.append(sym)
    symptoms_str = ",".join(unique_symptoms)
    rows.append((disease, symptoms_str))

# Optionally, sort rows by disease name
rows.sort(key=lambda x: x[0].lower())

# -----------------------------------------------------------------------------
# 4. Write the dataset.csv file.
# -----------------------------------------------------------------------------

with open("dataset.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    writer.writerow(["Disease", "Symptoms"])
    # Write each row
    for row in rows:
        writer.writerow(row)

print("dataset.csv has been created.")
