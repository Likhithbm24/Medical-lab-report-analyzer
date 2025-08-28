#!/usr/bin/env python3
"""
Test script for PDF processing
Use this to debug PDF extraction issues
"""

import os
import sys
from extract import extract_lab_data

def test_pdf_processing(pdf_path):
    """Test PDF processing with detailed error reporting"""
    print(f"Testing PDF processing for: {pdf_path}")
    print("=" * 50)
    
    # Check if file exists
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return False
    
    # Check file size
    file_size = os.path.getsize(pdf_path)
    print(f"📁 File size: {file_size} bytes")
    
    if file_size == 0:
        print("❌ File is empty")
        return False
    
    # Check file extension
    if not pdf_path.lower().endswith('.pdf'):
        print("❌ File is not a PDF")
        return False
    
    try:
        # Try to extract data
        print("🔍 Attempting to extract lab data...")
        result = extract_lab_data(pdf_path)
        
        if result:
            print(f"✅ Success! Extracted {len(result)} lab values:")
            for key, value in result.items():
                print(f"   {key}: {value}")
        else:
            print("⚠️  No lab values extracted (empty result)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_pdf.py <path_to_pdf>")
        print("Example: python test_pdf.py sample_lab_report.pdf")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    success = test_pdf_processing(pdf_path)
    
    if success:
        print("\n🎉 PDF processing test completed successfully!")
    else:
        print("\n💥 PDF processing test failed!")
        sys.exit(1)
