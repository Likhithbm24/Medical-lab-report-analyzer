import requests
import json
import os
import time

# Render API configuration
RENDER_API_KEY = os.getenv('RENDER_API_KEY')  # You'll need to set this
RENDER_API_URL = "https://api.render.com/v1"

def deploy_to_render():
    """Deploy backend to Render"""
    
    if not RENDER_API_KEY:
        print("❌ RENDER_API_KEY environment variable not set")
        print("Please set your Render API key:")
        print("1. Go to https://dashboard.render.com/account/api-keys")
        print("2. Create a new API key")
        print("3. Set: set RENDER_API_KEY=your_key_here")
        return False
    
    headers = {
        "Authorization": f"Bearer {RENDER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Service configuration
    service_data = {
        "type": "web_service",
        "name": "medical-insights-backend",
        "env": "python",
        "plan": "free",
        "region": "oregon",
        "buildCommand": "pip install -r backend/requirements.txt",
        "startCommand": "cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT",
        "envVars": [
            {"key": "PYTHON_VERSION", "value": "3.9.16"},
            {"key": "PORT", "value": "8000"}
        ],
        "healthCheckPath": "/health",
        "autoDeploy": True,
        "repo": {
            "repo": "Likhithbm24/Medical-lab-report-analyzer",
            "branch": "main",
            "owner": "Likhithbm24"
        }
    }
    
    try:
        print("🚀 Deploying backend to Render...")
        
        # Create service
        response = requests.post(
            f"{RENDER_API_URL}/services",
            headers=headers,
            json=service_data
        )
        
        if response.status_code == 201:
            service = response.json()
            service_id = service['id']
            print(f"✅ Backend service created with ID: {service_id}")
            
            # Wait for deployment
            print("⏳ Waiting for deployment to complete...")
            time.sleep(30)  # Wait for initial deployment
            
            # Get service status
            status_response = requests.get(
                f"{RENDER_API_URL}/services/{service_id}",
                headers=headers
            )
            
            if status_response.status_code == 200:
                service_info = status_response.json()
                service_url = service_info.get('serviceUrl')
                if service_url:
                    print(f"🎉 Backend deployed successfully!")
                    print(f"🌐 URL: {service_url}")
                    print(f"🔗 Health Check: {service_url}/health")
                    return service_url
                else:
                    print("⚠️ Service created but URL not available yet")
                    return None
            else:
                print(f"❌ Failed to get service status: {status_response.status_code}")
                return None
                
        else:
            print(f"❌ Failed to create service: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error deploying to Render: {str(e)}")
        return None

if __name__ == "__main__":
    deploy_to_render()
