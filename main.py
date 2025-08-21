from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Now import from backend
from extract import extract_lab_data
from llm import explain_results

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Create temp directory if it doesn't exist
    temp_dir = "backend/temp"
    os.makedirs(temp_dir, exist_ok=True)
    
    file_location = f"{temp_dir}/{file.filename}"
    
    # Save the file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Extract data
        lab_data = extract_lab_data(file_location)
        
        # Explain data
        interpretation = explain_results(lab_data)
        
        return {
            "data": lab_data,
            "explanation": interpretation
        }
    except Exception as e:
        return {
            "error": f"Analysis failed: {str(e)}",
            "data": {},
            "explanation": {}
        }

@app.get("/")
async def root():
    return {"message": "Medical Insights API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
