import React, { useState, useRef } from "react";
import axios from "axios";

export default function FileUpload() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);
  const [explanation, setExplanation] = useState(null);
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState(null);
  const resultsRef = useRef(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setSuccess(false);
    setError(null);
    setData(null);
    setExplanation(null);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select a file.");

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);
    setSuccess(false);
    setError(null);
    setData(null);
    setExplanation(null);

    try {
      console.log("Uploading file:", file.name);
      const res = await axios.post("http://localhost:8000/upload", formData);
      console.log("Response received:", res.data);

      if (res.data.error) {
        setError(res.data.error);
        setSuccess(false);
      } else {
        setData(res.data.data);
        setExplanation(res.data.explanation);
        setSuccess(true);
        setError(null);
        setTimeout(() => {
          resultsRef.current?.scrollIntoView({ behavior: "smooth" });
        }, 500);
      }
    } catch (error) {
      console.error("Upload error:", error);
      setError(
        `Upload failed: ${
          error.response?.data?.detail || error.message || "Unknown error"
        }`
      );
      setSuccess(false);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-container">
      <h1 className="title">Smart Medical Lab Report Analyzer</h1>

      <div className="upload-box">
        <h2>📋 Upload Your Lab Report</h2>
        <p style={{ color: "#6b7280", marginBottom: "25px" }}>
          Upload a PDF lab report to receive AI-powered analysis and medical
          insights
        </p>

        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          style={{ marginBottom: "20px" }}
        />

        <button onClick={handleUpload} disabled={loading}>
          {loading ? (
            <>
              <div
                className="loader"
                style={{ display: "inline-block", marginRight: "10px" }}
              ></div>
              Analyzing Report...
            </>
          ) : (
            <>🔬 Upload & Analyze</>
          )}
        </button>

        {file && (
          <div className="file-name">
            📄 File Selected: <strong>{file.name}</strong>
          </div>
        )}
      </div>

      {error && <div className="error-message">❌ {error}</div>}

      {success && (
        <div className="success-message">
          ✅ Report analyzed successfully! Your medical insights are ready
          below.
        </div>
      )}

      {loading && (
        <div className="loading-message">
          🔄 Processing your lab report... This may take a few moments.
        </div>
      )}

      {data && explanation && (
        <div ref={resultsRef} className="results">
          <h2>Medical Analysis Results</h2>

          {Object.keys(data).length === 0 ? (
            <div
              style={{
                textAlign: "center",
                padding: "40px",
                background: "white",
                borderRadius: "15px",
                boxShadow: "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
              }}
            >
              <p style={{ fontSize: "1.1rem", color: "#6b7280" }}>
                No lab values were found in the PDF. Please ensure the PDF
                contains lab test results.
              </p>
            </div>
          ) : (
            <>
              <div
                style={{
                  textAlign: "center",
                  marginBottom: "30px",
                  padding: "20px",
                  background: "linear-gradient(135deg, #f0f9ff, #e0f2fe)",
                  borderRadius: "15px",
                  border: "2px solid #60a5fa",
                }}
              >
                <h3 style={{ color: "#1e3a8a", marginBottom: "10px" }}>
                  📊 Summary: {Object.keys(data).length} Lab Tests Analyzed
                </h3>
                <p style={{ color: "#6b7280" }}>
                  Your report has been processed using advanced medical AI
                  algorithms
                </p>
              </div>

              {Object.keys(data).map((key, index) => (
                <div
                  className="result-card"
                  key={key}
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <h3>{key}</h3>
                  <p>
                    <strong>Test Value:</strong> {data[key]}
                  </p>
                  <div className="explanation">
                    <strong>Medical Interpretation:</strong> {explanation[key]}
                  </div>
                </div>
              ))}

              <div
                style={{
                  textAlign: "center",
                  marginTop: "40px",
                  padding: "25px",
                  background: "linear-gradient(135deg, #f0fdf4, #dcfce7)",
                  borderRadius: "15px",
                  border: "2px solid #22c55e",
                }}
              >
                <h3 style={{ color: "#059669", marginBottom: "15px" }}>
                  ⚠️ Medical Disclaimer
                </h3>
                <p style={{ color: "#6b7280", fontSize: "0.95rem" }}>
                  This analysis is for informational purposes only and should
                  not replace professional medical advice. Always consult with
                  qualified healthcare professionals for medical decisions.
                </p>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
}
