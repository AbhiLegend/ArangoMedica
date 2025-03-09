import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating random names
fake = Faker()

# Define realistic medical data categories
disease_symptom_map = {
    "Pneumonia": ["Fever", "Cough", "Shortness of Breath", "Chest Pain"],
    "COVID-19": ["Fever", "Cough", "Fatigue", "Shortness of Breath", "Headache"],
    "Diabetes": ["Fatigue", "Frequent Urination", "Blurred Vision", "Weight Loss"],
    "Hypertension": ["Headache", "Dizziness", "Fatigue", "Chest Pain"],
    "Asthma": ["Shortness of Breath", "Wheezing", "Chest Tightness", "Cough"],
    "Bronchitis": ["Cough", "Fatigue", "Shortness of Breath", "Chest Pain"],
    "Tuberculosis": ["Fever", "Night Sweats", "Weight Loss", "Cough"],
    "Migraine": ["Headache", "Nausea", "Sensitivity to Light", "Dizziness"],
}

disease_treatment_map = {
    "Pneumonia": ["Oxygen Therapy", "Antibiotics"],
    "COVID-19": ["Oxygen Therapy", "Remdesivir"],
    "Diabetes": ["Insulin", "Metformin"],
    "Hypertension": ["Beta Blockers", "ACE Inhibitors"],
    "Asthma": ["Inhalers", "Steroids"],
    "Bronchitis": ["Cough Syrup", "Rest"],
    "Tuberculosis": ["Antibiotics", "Rifampin"],
    "Migraine": ["Pain Relievers", "Lifestyle Changes"],
}

drug_interactions = {
    "Metformin": ["Insulin", "Aspirin"],
    "Ibuprofen": ["Aspirin", "Prednisone"],
    "Aspirin": ["Ibuprofen", "Paracetamol"],
    "Remdesivir": ["Prednisone", "Paracetamol"],
    "Insulin": ["Metformin"],
}

genes = ["BRCA1", "TP53", "APOE", "CFTR", "HBB", "EGFR", "KRAS", "PTEN"]

# Generate patients
num_patients = 10000
patients = [fake.name() for _ in range(num_patients)]

# Generate relationships
relationships = []

for _ in range(300000):  # More edges
    patient = random.choice(patients)
    disease = random.choice(list(disease_symptom_map.keys()))
    symptoms = random.sample(disease_symptom_map[disease], random.randint(1, len(disease_symptom_map[disease])))
    treatments = disease_treatment_map[disease]
    
    # Patient diagnosed with disease
    relationships.append((patient, disease, "PATIENT_DIAGNOSED_WITH"))
    
    # Patient has symptoms related to disease
    for symptom in symptoms:
        relationships.append((patient, symptom, "PATIENT_HAS_SYMPTOM"))
        relationships.append((symptom, disease, "SYMPTOM_INDICATES_DISEASE"))
    
    # Disease treatments and drugs
    for treatment in treatments:
        relationships.append((disease, treatment, "DISEASE_HAS_TREATMENT"))

    # Disease has related genes
    gene = random.choice(genes)
    relationships.append((disease, gene, "DISEASE_HAS_GENE"))
    
    # Drug interactions
    if random.random() > 0.6:
        drug = random.choice(list(drug_interactions.keys()))
        relationships.append((disease, drug, "DISEASE_HAS_DRUG"))
        for interacting_drug in drug_interactions.get(drug, []):
            relationships.append((drug, interacting_drug, "DRUG_INTERACTS_WITH"))

# Convert to DataFrame
df = pd.DataFrame(relationships, columns=["source", "target", "relationship_type"])

# Save to CSV
csv_path = "realistic_graph_data.csv"
df.to_csv(csv_path, index=False)

csv_path
