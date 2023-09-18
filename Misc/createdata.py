import pandas as pd
import numpy as np
import random

# Generate synthetic data
n = 1000  # Number of records

# Patient ID
patient_id = [f'P{i+1}' for i in range(n)]

# Age
age = np.random.randint(18, 80, n)

# Gender
gender = [random.choice(['Male', 'Female']) for _ in range(n)]

# Treatment Type
treatment_type = [random.choice(['Surgery', 'Medication', 'Therapy']) for _ in range(n)]

# Treatment Duration
treatment_duration = np.random.randint(1, 30, n)

# Treatment Cost (rounded to 2 decimal places)
treatment_cost = np.round(np.random.uniform(500, 5000, n), 2)

# Patient Satisfaction
patient_satisfaction = np.random.randint(1, 11, n)

# Create DataFrame
df = pd.DataFrame({
    'patient_id': patient_id,
    'age': age,
    'gender': gender,
    'treatment_type': treatment_type,
    'treatment_duration': treatment_duration,
    'treatment_cost': treatment_cost,
    'patient_satisfaction': patient_satisfaction
})

# Save to CSV
df.to_csv('healthcare_synthetic_data.csv', index=False)

print("Synthetic data generated and saved to 'healthcare_synthetic_data.csv'")
