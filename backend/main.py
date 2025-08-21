from fastapi import FastAPI, UploadFile, File # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import shutil
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
    file_location = f"temp/{file.filename}"
    
    # Save the file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Extract data
    lab_data = extract_lab_data(file_location)
    
    # Explain data
    interpretation = explain_results(lab_data)

    return {
        "data": lab_data,
        "explanation": interpretation
    }
