def explain_results(data: dict):
    interpretations = {
        "Hemoglobin": lambda val: "Low hemoglobin may indicate anemia or nutritional issues." if float(val) < 13 else "Normal hemoglobin level.",
        "TSH": lambda val: "High TSH could suggest hypothyroidism." if float(val) > 4.5 else "Normal thyroid function.",
        "WBC": lambda val: "High WBC may indicate infection." if float(val) > 11000 else "Normal WBC count.",
        "Platelets": lambda val: "Low platelets could suggest clotting issues." if float(val) < 150000 else "Normal platelet count.",
        "RBC": lambda val: "Low RBC may indicate anemia." if float(val) < 4.7 else "Normal RBC count.",
        "Cholesterol": lambda val: "High cholesterol increases heart disease risk." if float(val) > 200 else "Normal cholesterol.",
        "Glucose": lambda val: "High glucose could indicate diabetes risk." if float(val) > 100 else "Normal glucose level.",
        "Creatinine": lambda val: "High creatinine may suggest kidney issues." if float(val) > 1.2 else "Normal kidney function.",
        "Bilirubin": lambda val: "High bilirubin could mean liver problems." if float(val) > 1.2 else "Normal liver function.",
        "LDL": lambda val: "High LDL increases heart disease risk." if float(val) > 100 else "Normal LDL.",
        "HDL": lambda val: "Low HDL increases heart risk." if float(val) < 40 else "Good HDL level.",
        "ESR": lambda val: "High ESR may indicate inflammation or infection." if float(val) > 20 else "Normal ESR level.",
        "Neutrophils": lambda val: "High neutrophils may indicate bacterial infection." if float(val) > 68 else "Normal neutrophil count.",
        "Lymphocytes": lambda val: "High lymphocytes may indicate viral infection." if float(val) > 40 else "Normal lymphocyte count.",
        "Monocytes": lambda val: "High monocytes may indicate chronic inflammation." if float(val) > 10 else "Normal monocyte count.",
        "Eosinophils": lambda val: "High eosinophils may indicate allergies or parasitic infection." if float(val) > 4 else "Normal eosinophil count.",
    }

    explanation = {}

    for key, val in data.items():
        explanation[key] = interpretations.get(key, lambda x: "No info available.")(val)

    return explanation
