from werkzeug.datastructures import ImmutableMultiDict
import numpy as np
from pickle import load
from flask import Flask, render_template,request,url_for, redirect
model = load(open('model.pkl', 'rb'))
app = Flask(__name__)

symptoms = ['itching', 'skinrash', 'nodalskineruptions', 'continuoussneezing',
       'shivering', 'chills', 'jointpain', 'stomachpain', 'acidity',
       'ulcersontongue', 'musclewasting', 'vomiting',
       'burningmicturition', 'spottingurination', 'fatigue', 'weightgain',
       'anxiety', 'coldhandsandfeets', 'moodswings', 'weightloss',
       'restlessness', 'lethargy', 'patchesinthroat',
       'irregularsugarlevel', 'cough', 'highfever', 'sunkeneyes',
       'breathlessness', 'sweating', 'dehydration', 'indigestion',
       'headache', 'yellowishskin', 'darkurine', 'nausea',
       'lossofappetite', 'painbehindtheeyes', 'backpain', 'constipation',
       'abdominalpain', 'diarrhoea', 'mildfever', 'yellowurine',
       'yellowingofeyes', 'acuteliverfailure', 'fluidoverload',
       'swellingofstomach', 'swelledlymphnodes', 'malaise',
       'blurredanddistortedvision', 'phlegm', 'throatirritation',
       'rednessofeyes', 'sinuspressure', 'runnynose', 'congestion',
       'chestpain', 'weaknessinlimbs', 'fastheartrate',
       'painduringbowelmovements', 'paininanalregion', 'bloodystool',
       'irritationinanus', 'neckpain', 'dizziness', 'cramps', 'bruising',
       'obesity', 'swollenlegs', 'swollenbloodvessels',
       'puffyfaceandeyes', 'enlargedthyroid', 'brittlenails',
       'swollenextremeties', 'excessivehunger', 'extramaritalcontacts',
       'dryingandtinglinglips', 'slurredspeech', 'kneepain',
       'hipjointpain', 'muscleweakness', 'stiffneck', 'swellingjoints',
       'movementstiffness', 'spinningmovements', 'lossofbalance',
       'unsteadiness', 'weaknessofonebodyside', 'lossofsmell',
       'bladderdiscomfort', 'foulsmellofurine', 'continuousfeelofurine',
       'passageofgases', 'internalitching', 'toxiclook(typhos)',
       'depression', 'irritability', 'musclepain', 'alteredsensorium',
       'redspotsoverbody', 'bellypain', 'abnormalmenstruation',
       'dischromicpatches', 'wateringfromeyes', 'increasedappetite',
       'polyuria', 'familyhistory', 'mucoidsputum', 'rustysputum',
       'lackofconcentration', 'visualdisturbances',
       'receivingbloodtransfusion', 'receivingunsterileinjections',
       'coma', 'stomachbleeding', 'distentionofabdomen',
       'historyofalcoholconsumption', 'fluidoverload', 'bloodinsputum',
       'prominentveinsoncalf', 'palpitations', 'painfulwalking',
       'pusfilledpimples', 'blackheads', 'scurring', 'skinpeeling',
       'silverlikedusting', 'smalldentsinnails', 'inflammatorynails',
       'blister', 'redsorearoundnose', 'yellowcrustooze', 'prognosis',
       'Not available']

symptom_code = [56, 102,  74,  26,  98,  20,  57, 109,   3, 120,  70, 123,  18,
       106,  42, 127,   6,  21,  66, 128,  94,  60,  82,  53,  27,  46,
       110,  15, 111,  30,  50,  45, 131,  29,  72,  61,  76,   7,  24,
         1,  32,  65, 132, 130,   4,  43, 114, 112,  64,  14,  83, 118,
        91, 100,  95,  23,  19, 125,  41,  77,  79,  13,  55,  73,  35,
        28,  17,  75, 117, 115,  87,  37,  16, 116,  38,  39,  36, 103,
        58,  47,  71, 107, 113,  67, 105,  62, 121, 126,  63,  10,  44,
        25,  81,  52, 119,  31,  54,  69,   5,  93,   8,   2,  33, 124,
        49,  84,  40,  68,  96,  59, 122,  89,  90,  22, 108,  34,  48,
        43,  12,  86,  80,  78,  88,   9,  97, 101,  99, 104,  51,  11,
        92, 129,  85,   0]

diseases = ['Fungal Infection', 'Allergy', 'GERD', 'Chronic Cholestasis',
       'Drug Reaction', 'Peptic ulcer disease', 'AIDS', 'Diabetes',
       'Gastroenteritis', 'Bronchial Asthma', 'Hypertension', 'Migraine',
       'Cervical spondylosis', 'Paralysis(brainhemorrhage)', 'Jaundice',
       'Malaria', 'Chicken-Pox', 'Dengue', 'Typhoid', 'hepatitis-A',
       'Hepatitis-B', 'Hepatitis-C', 'Hepatitis-D', 'Hepatitis-E',
       'Alcoholic-Hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
       'Dimorphichemmorhoids(piles)', 'Heart-Attack', 'Varicoseveins',
       'Hypo-thyroidism', 'Hyper-thyroidism', 'Hypo-glycemia',
       'Osteo-arthristis', 'Arthritis',
       'Paroymsal Positional Vertigo(vertigo)', 'Acne',
       'Urinary Tract Infection', 'Psoriasis', 'Impetigo']

diseases_code = [15,  4, 16,  9, 14, 33,  1, 12, 17,  6, 23, 30,  7, 32, 28, 29,  8,
       11, 37, 40, 19, 20, 21, 22,  3, 36, 10, 34, 13, 18, 39, 26, 24, 25,
       31,  5,  0,  2, 38, 35, 27]

symptom_weight_dict = {'itching': 1, 'skinrash': 3, 'nodalskineruptions': 4, 'continuoussneezing': 4, 'shivering': 5, 'chills': 3, 'jointpain': 3, 'stomachpain': 5, 'acidity': 3, 'ulcersontongue': 4, 'musclewasting': 3, 'vomiting': 5, 'burningmicturition': 6, 'spottingurination': 6, 'fatigue': 4, 'weightgain': 3, 'anxiety': 4, 'coldhandsandfeets': 5, 'moodswings': 3, 'weightloss': 3, 'restlessness': 5, 'lethargy': 2, 'patchesinthroat': 6, 'irregularsugarlevel': 5, 'cough': 4, 'highfever': 7, 'sunkeneyes': 3, 'breathlessness': 4, 'sweating': 3, 'dehydration': 4, 'indigestion': 5, 'headache': 3, 'yellowishskin': 3, 'darkurine': 4, 'nausea': 5, 'lossofappetite': 4, 'painbehindtheeyes': 4, 'backpain': 3, 'constipation': 4, 'abdominalpain': 4, 'diarrhoea': 6, 'mildfever': 5, 'yellowurine': 4, 'yellowingofeyes': 4, 'acuteliverfailure': 6, 'fluidoverload': 4, 'swellingofstomach': 7, 'swelledlymphnodes': 6, 'malaise': 6, 'blurredanddistortedvision': 5, 'phlegm': 5, 'throatirritation': 4, 'rednessofeyes': 5, 'sinuspressure': 4, 'runnynose': 5, 'congestion': 5, 'chestpain': 7, 'weaknessinlimbs': 7, 'fastheartrate': 5, 'painduringbowelmovements': 5, 'paininanalregion': 6, 'bloodystool': 5, 'irritationinanus': 6, 'neckpain': 5, 'dizziness': 4, 'cramps': 4, 'bruising': 4, 'obesity': 4, 'swollenlegs': 5, 'swollenbloodvessels': 5, 'puffyfaceandeyes': 5, 'enlargedthyroid': 6, 'brittlenails': 5, 'swollenextremeties': 5, 'excessivehunger': 4, 'extramaritalcontacts': 5, 'dryingandtinglinglips': 4, 'slurredspeech': 4, 'kneepain': 3, 'hipjointpain': 2, 'muscleweakness': 2, 'stiffneck': 4, 'swellingjoints': 5, 'movementstiffness': 5, 'spinningmovements': 6, 'lossofbalance': 4, 'unsteadiness': 4, 'weaknessofonebodyside': 4, 'lossofsmell': 3, 'bladderdiscomfort': 4, 'foulsmellofurine': 5, 'continuousfeelofurine': 6, 'passageofgases': 5, 'internalitching': 4, 'toxiclook(typhos)': 5, 'depression': 3, 'irritability': 2, 'musclepain': 2, 'alteredsensorium': 2, 'redspotsoverbody': 3, 'bellypain': 4, 'abnormalmenstruation': 6, 'dischromicpatches': 6, 'wateringfromeyes': 4, 'increasedappetite': 5, 'polyuria': 4, 'familyhistory': 5, 'mucoidsputum': 4, 'rustysputum': 4, 'lackofconcentration': 3, 'visualdisturbances': 3, 'receivingbloodtransfusion': 5, 'receivingunsterileinjections': 2, 'coma': 7, 'stomachbleeding': 6, 'distentionofabdomen': 4, 'historyofalcoholconsumption': 5, 'bloodinsputum': 5, 'prominentveinsoncalf': 6, 'palpitations': 4, 'painfulwalking': 2, 'pusfilledpimples': 2, 'blackheads': 2, 'scurring': 2, 'skinpeeling': 3, 'silverlikedusting': 2, 'smalldentsinnails': 2, 'inflammatorynails': 2, 'blister': 4, 'redsorearoundnose': 2, 'yellowcrustooze': 3, 'prognosis': 5, 'Not available':0}
disease_code_dict = {x:y for x,y in zip(diseases_code, diseases)}
symptom_code_dict = {x:y for x,y in zip(symptoms, symptom_code)}

def symptoms_to_disease(symptoms):
    total_weight = 0
    pred_arr = []
    for i in symptoms:
        total_weight += symptom_weight_dict[i]
        
        pred_arr.append(symptom_code_dict[i])
    pred_arr.append(total_weight)
    if(sum(pred_arr) == 0):
        return "Please enter atleast one symptom"
    
    disease = model.predict([pred_arr])
    return disease_code_dict[disease[0]]
    




@app.route('/', methods=["POST", "GET"])
def home():
    
    if request.method == "POST":
        
        form_values = request.form.to_dict(flat=False)
        pred_values = [i[0] for i in form_values.values()]
        pred_disease = symptoms_to_disease(pred_values)
        

        
        return render_template('index.html', data=pred_disease)
        
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    

