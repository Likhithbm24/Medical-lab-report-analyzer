# Medical Insights App

A comprehensive web application that analyzes medical lab reports and provides intelligent insights using AI-powered interpretation.

## 🏥 Features

- **PDF Lab Report Upload**: Upload and process medical lab reports in PDF format
- **Automated Data Extraction**: Automatically extract key lab values using advanced text parsing
- **AI-Powered Analysis**: Get intelligent interpretations of lab results with medical context
- **Comprehensive Lab Coverage**: Supports multiple lab tests including:
  - Blood counts (Hemoglobin, WBC, RBC, Platelets)
  - Thyroid function (TSH)
  - Cholesterol profile (Total, LDL, HDL)
  - Metabolic markers (Glucose, Creatinine, Bilirubin)
- **Real-time Processing**: Instant analysis and results
- **Modern Web Interface**: Clean, responsive React-based frontend
- **RESTful API**: FastAPI backend with automatic API documentation

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+ and npm
- Windows 10/11 (for Windows users)

### Backend Setup

1. **Navigate to backend directory:**

   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   # On Windows:
   .venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The backend will be available at: http://localhost:8000

   - API Documentation: http://localhost:8000/docs
   - Interactive API: http://localhost:8000/redoc

### Frontend Setup

1. **Navigate to frontend directory:**

   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**

   ```bash
   npm install
   ```

3. **Start the development server:**

   ```bash
   npm run dev
   ```

   The frontend will be available at: http://localhost:5173

## 🏗️ Architecture

### Backend (FastAPI)

- **`main.py`**: FastAPI application with CORS middleware and file upload endpoint
- **`extract.py`**: PDF text extraction and lab value parsing using PyMuPDF
- **`llm.py`**: AI-powered lab result interpretation and medical insights
- **`models.py`**: Data models and schemas
- **`utils.py`**: Utility functions and helpers

### Frontend (React + Vite)

- **`App.jsx`**: Main application component
- **`FileUpload.jsx`**: File upload component with drag-and-drop support
- **Modern UI**: Built with Tailwind CSS for responsive design

## 📊 Supported Lab Tests

| Test        | Normal Range                         | Clinical Significance      |
| ----------- | ------------------------------------ | -------------------------- |
| Hemoglobin  | 13-17 g/dL (M), 12-15 g/dL (F)       | Anemia, nutritional status |
| TSH         | 0.4-4.5 mIU/L                        | Thyroid function           |
| WBC         | 4.5-11.0 K/μL                        | Infection, inflammation    |
| RBC         | 4.7-6.1 M/μL (M), 4.2-5.4 M/μL (F)   | Anemia, blood disorders    |
| Platelets   | 150-450 K/μL                         | Clotting disorders         |
| Cholesterol | <200 mg/dL                           | Heart disease risk         |
| Glucose     | <100 mg/dL (fasting)                 | Diabetes risk              |
| Creatinine  | 0.7-1.3 mg/dL (M), 0.6-1.1 mg/dL (F) | Kidney function            |
| Bilirubin   | <1.2 mg/dL                           | Liver function             |
| LDL         | <100 mg/dL                           | Heart disease risk         |
| HDL         | >40 mg/dL (M), >50 mg/dL (F)         | Heart disease protection   |

## 🔧 API Endpoints

### POST `/upload`

Upload a PDF lab report for analysis.

**Request:**

- Content-Type: `multipart/form-data`
- Body: PDF file

**Response:**

```json
{
  "data": {
    "Hemoglobin": "14.2",
    "TSH": "2.1",
    "WBC": "7.5"
  },
  "explanation": {
    "Hemoglobin": "Normal hemoglobin level.",
    "TSH": "Normal thyroid function.",
    "WBC": "Normal WBC count."
  }
}
```

## 🎯 Usage

1. **Upload Report**: Drag and drop or select a PDF lab report
2. **Automatic Processing**: The system extracts lab values and analyzes results
3. **Get Insights**: Receive AI-powered interpretations with medical context
4. **Review Results**: View both raw data and intelligent explanations

## 🛠️ Development

### Running Tests

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Building for Production

```bash
# Frontend build
cd frontend
npm run build

# Backend production
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
medical-insights-app/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── extract.py           # PDF extraction logic
│   ├── llm.py               # AI interpretation
│   ├── models.py            # Data models
│   ├── utils.py             # Utility functions
│   ├── requirements.txt     # Python dependencies
│   └── temp/                # Temporary file storage
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Main app component
│   │   ├── components/      # React components
│   │   └── assets/          # Static assets
│   ├── package.json         # Node.js dependencies
│   └── vite.config.js       # Vite configuration
└── README.md                # This file
```

## 🔒 Security & Privacy

- **Local Processing**: All file processing happens locally
- **No Data Storage**: Files are processed in memory and not permanently stored
- **CORS Enabled**: Frontend can communicate with backend securely
- **Input Validation**: Robust file type and size validation

## 🚨 Troubleshooting

### Common Issues

1. **PyMuPDF Installation Error**

   - Solution: Use `pip install --only-binary=all PyMuPDF`

2. **Port Already in Use**

   - Solution: Change port in uvicorn command or kill existing process

3. **CORS Issues**

   - Solution: Ensure backend is running and CORS middleware is enabled

4. **File Upload Fails**
   - Solution: Check file size and ensure it's a valid PDF

### Getting Help

- Check the API documentation at http://localhost:8000/docs
- Review console logs for detailed error messages
- Ensure all dependencies are properly installed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏥 Medical Disclaimer

This application is for educational and informational purposes only. It is not intended to replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

---

**Built with ❤️ using FastAPI, React, and AI-powered medical insights**
