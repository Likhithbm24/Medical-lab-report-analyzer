# 🏥 Medical Insights - Smart Lab Report Analyzer

A sophisticated AI-powered application that analyzes medical lab reports using advanced PDF processing and machine learning algorithms to provide instant medical insights and interpretations.

![Medical Insights App](https://img.shields.io/badge/Medical-AI%20Powered-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![React](https://img.shields.io/badge/React-18+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)

## 🌟 Features

### 🔬 **Advanced PDF Analysis**
- **PDF Text Extraction**: Uses PyMuPDF for high-quality text extraction
- **Smart Pattern Recognition**: Regex-based lab value detection
- **Multi-format Support**: Handles various lab report formats

### 🧠 **AI-Powered Medical Insights**
- **Intelligent Interpretation**: AI algorithms analyze lab values
- **Medical Thresholds**: Built-in medical reference ranges
- **Professional Explanations**: Clear, medical-grade interpretations

### 🎨 **Professional Medical UI**
- **Medical Theme**: Professional healthcare application design
- **Responsive Design**: Works perfectly on all devices
- **Modern Interface**: Clean, intuitive user experience

### 📊 **Comprehensive Lab Test Coverage**
- **Blood Tests**: Hemoglobin, WBC, RBC, Platelets
- **Metabolic Panel**: Glucose, Creatinine, Bilirubin
- **Lipid Profile**: Cholesterol, LDL, HDL
- **Thyroid Function**: TSH levels
- **Inflammatory Markers**: ESR, Neutrophils, Lymphocytes

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/Likhithbm24/Medical-lab-report-analyzer.git
cd Medical-lab-report-analyzer

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\Activate.ps1
# Linux/Mac
source .venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run the server
cd ..
python test_server.py
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Access the Application
- **Backend API**: http://localhost:8000
- **Frontend**: http://localhost:5173
- **Health Check**: http://localhost:8000/health

## 🏗️ Architecture

### Backend (FastAPI)
```
backend/
├── main.py              # Main FastAPI application
├── extract.py           # PDF text extraction & lab value parsing
├── llm.py              # AI interpretation engine
├── models.py           # Data models
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
└── temp/               # Temporary file storage
```

### Frontend (React + Vite)
```
frontend/
├── src/
│   ├── components/
│   │   └── FileUpload.jsx    # Main upload component
│   ├── App.jsx               # Main application
│   ├── main.jsx              # Entry point
│   └── App.css               # Medical-themed styling
├── package.json              # Node.js dependencies
└── index.html                # HTML template
```

## 🔧 API Endpoints

### POST `/upload`
Upload and analyze a PDF lab report.

**Request:**
- `file`: PDF file (multipart/form-data)

**Response:**
```json
{
  "data": {
    "Hemoglobin": "13.8",
    "WBC": "7500",
    "Platelets": "250000"
  },
  "explanation": {
    "Hemoglobin": "Normal hemoglobin level.",
    "WBC": "Normal WBC count.",
    "Platelets": "Normal platelet count."
  }
}
```

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## 🧪 Supported Lab Tests

| Test Category | Tests | Normal Range |
|---------------|-------|--------------|
| **Blood Count** | Hemoglobin, WBC, RBC, Platelets | Variable by age/sex |
| **Metabolic** | Glucose, Creatinine, Bilirubin | Standard ranges |
| **Lipid** | Cholesterol, LDL, HDL | Cardiovascular risk |
| **Thyroid** | TSH | 0.4-4.5 mIU/L |
| **Inflammatory** | ESR, Neutrophils, Lymphocytes | Infection markers |

## 🎨 UI Features

### Medical Theme
- **Professional Color Scheme**: Medical blues and greens
- **Medical Icons**: 🏥 🔬 📊 🧠 ⚠️
- **Responsive Design**: Mobile-first approach
- **Smooth Animations**: Professional transitions

### User Experience
- **Drag & Drop**: Easy file upload
- **Real-time Processing**: Live analysis feedback
- **Clear Results**: Organized test result display
- **Medical Disclaimer**: Professional compliance

## 🔒 Security & Compliance

- **CORS Enabled**: Secure cross-origin requests
- **File Validation**: PDF format verification
- **Temporary Storage**: Secure file handling
- **Medical Disclaimer**: Professional liability protection

## 🚀 Deployment

### Local Development
```bash
# Backend
python test_server.py

# Frontend
cd frontend
npm run dev
```

### Production Deployment
```bash
# Build frontend
cd frontend
npm run build

# Run backend with production server
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Medical Disclaimer

**This application is for informational purposes only and should not replace professional medical advice. Always consult with qualified healthcare professionals for medical decisions.**

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Likhithbm24/Medical-lab-report-analyzer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Likhithbm24/Medical-lab-report-analyzer/discussions)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Likhithbm24/Medical-lab-report-analyzer&type=Date)](https://star-history.com/#Likhithbm24/Medical-lab-report-analyzer&Date)

---

**Built with ❤️ for the medical community**
