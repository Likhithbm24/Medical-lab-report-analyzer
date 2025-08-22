import pdfplumber
import re

def extract_lab_data(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as doc:
        for page in doc:
            text += page.extract_text() or ""

    # Define regex patterns for lab values - updated to handle various formats
    patterns = {
        "Hemoglobin": r"Hemoglobin\s*\([^)]*\)\s*:\s*(\d+\.?\d*)",
        "TSH": r"TSH\s*[:\-]?\s*(\d+\.?\d*)",
        "WBC": r"WBC\s*\([^)]*\)\s*:\s*(\d+)",
        "RBC": r"RBC\s*\([^)]*\)\s*:\s*(\d+\.?\d*)",
        "Platelets": r"Platelet\s*Count\s*\([^)]*\)\s*:\s*(\d+)",
        "Cholesterol": r"Cholesterol\s*[:\-]?\s*(\d+\.?\d*)",
        "Glucose": r"Glucose\s*[:\-]?\s*(\d+\.?\d*)",
        "Creatinine": r"Creatinine\s*[:\-]?\s*(\d+\.?\d*)",
        "Bilirubin": r"Bilirubin\s*[:\-]?\s*(\d+\.?\d*)",
        "LDL": r"LDL\s*[:\-]?\s*(\d+\.?\d*)",
        "HDL": r"HDL\s*[:\-]?\s*(\d+\.?\d*)",
        "ESR": r"ESR\s*\([^)]*\)\s*:\s*(\d+)",
        "Neutrophils": r"Neutrophils\s*\([^)]*\)\s*:\s*(\d+)",
        "Lymphocytes": r"Lymphocytes\s*\([^)]*\)\s*:\s*(\d+)",
        "Monocytes": r"Monocytes\s*\([^)]*\)\s*:\s*(\d+)",
        "Eosinophils": r"Eosinophils\s*\([^)]*\)\s*:\s*(\d+)",
    }

    extracted = {}

    for test, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted[test] = match.group(1)
    
    return extracted
