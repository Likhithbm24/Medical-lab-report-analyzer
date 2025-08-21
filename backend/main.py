from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from extract import extract_lab_data
from llm import explain_results

app = FastAPI(
    title="Medical Insights API",
    description="AI-powered medical lab report analyzer",
    version="1.0.0"
)

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
    temp_dir = "temp"
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
        
        # Clean up temporary file
        os.remove(file_location)
        
        return {
            "data": lab_data,
            "explanation": interpretation
        }
    except Exception as e:
        # Clean up temporary file on error
        if os.path.exists(file_location):
            os.remove(file_location)
        
        return {
            "error": f"Analysis failed: {str(e)}",
            "data": {},
            "explanation": {}
        }

@app.get("/")
async def root():
    return {
        "message": "Medical Insights API is running!",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Medical Insights API"}

@app.get("/docs")
async def get_docs():
    return {"message": "API documentation available at /docs"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
