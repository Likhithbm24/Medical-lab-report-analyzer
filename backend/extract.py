import pdfplumber
import re
import os

def extract_lab_data(pdf_path):
    """
    Extract lab data from PDF file with proper error handling
    """
    # Validate file exists and is readable
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    if not os.path.isfile(pdf_path):
        raise ValueError(f"Path is not a file: {pdf_path}")
    
    text = ""
    doc = None
    
    try:
        # Open PDF with error handling
        doc = pdfplumber.open(pdf_path)
        
        # Check if PDF opened successfully
        if doc is None:
            raise ValueError("Failed to open PDF file")
        
        # Check if PDF has pages
        if not hasattr(doc, 'pages') or len(doc.pages) == 0:
            raise ValueError("PDF has no pages or is corrupted")
        
        # Extract text from each page
        for i, page in enumerate(doc.pages):
            try:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    print(f"Warning: Page {i+1} returned no text")
            except Exception as e:
                print(f"Warning: Error extracting text from page {i+1}: {e}")
                continue
        
        # Check if we got any text
        if not text.strip():
            raise ValueError("No text could be extracted from PDF")
            
    except Exception as e:
        # Clean up
        if doc:
            doc.close()
        raise Exception(f"Error processing PDF: {str(e)}")
    
    finally:
        # Always close the document
        if doc:
            doc.close()
    
    print(f"Extracted text length: {len(text)} characters")
    print(f"First 200 characters: {text[:200]}...")

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
        try:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                extracted[test] = match.group(1)
        except Exception as e:
            print(f"Warning: Error processing pattern for {test}: {e}")
            continue
    
    print(f"Extracted {len(extracted)} lab values: {list(extracted.keys())}")
    return extracted
