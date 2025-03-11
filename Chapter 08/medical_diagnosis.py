import openai 
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from sklearn.ensemble import RandomForestClassifier

import numpy as np
from generate_content import generate_content

def analyze_medical_image(image_path):
    model = ResNet50(weights='imagenet', include_top=False)
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    features = model.predict(x)
    return features 

def analyze_clinical_notes(clinical_text):
    prompt = f"Extract key medical findings from the clinical notes:\n\n{clinical_text}."
    conversation =[{"role": "system", "content": "You are a medical specialist."},
                   {"role": "user",
                    "content": prompt
                   }]   
   
    return generate_content(conversation)

def symptom_checker(symptoms):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Based on the following symptoms, suggest possible diagnoses:\n\n{symptoms}",
        max_tokens=150,
        n=3,
        stop=None,
        temperature=0.5,
    )
    return [choice.text.strip() for choice in response.choices]

def recommend_treatment(patient_data, diagnosis):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Assume model is trained on historical patient data
    treatment_recommendation = model.predict(patient_data)
    return treatment_recommendation

def clinical_decision_support(patient_id, current_condition):
    patient_data = fetch_patient_data(patient_id)
    ehr_analysis = analyze_clinical_notes(patient_data['clinical_notes'])
    image_analysis = analyze_medical_image(patient_data['recent_scans'])
    current_symptoms = current_condition['symptoms']
    possible_diagnoses = symptom_checker(current_symptoms)     

    prompt=f"Given the following information:\nPatient History: {ehr_analysis}\nImage Analysis: {image_analysis}\nCurrent Symptoms: {current_symptoms}\nPossible Diagnoses: {possible_diagnoses}\n\nProvide a clinical recommendation:"    
    conversation =[{"role": "system", "content": "You are a physician."},
                   {"role": "user",
                    "content": prompt
                   }]      
    return generate_content(conversation)

