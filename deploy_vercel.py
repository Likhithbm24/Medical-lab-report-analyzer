import requests
import json
import os
import time

# Vercel API configuration
VERCEL_TOKEN = os.getenv('VERCEL_TOKEN')  # You'll need to set this
VERCEL_API_URL = "https://api.vercel.com/v1"

def deploy_to_vercel(backend_url):
    """Deploy frontend to Vercel"""
    
    if not VERCEL_TOKEN:
        print("❌ VERCEL_TOKEN environment variable not set")
        print("Please set your Vercel token:")
        print("1. Go to https://vercel.com/account/tokens")
        print("2. Create a new token")
        print("3. Set: set VERCEL_TOKEN=your_token_here")
        return False
    
    headers = {
        "Authorization": f"Bearer {VERCEL_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        print("🚀 Deploying frontend to Vercel...")
        
        # First, get user info
        user_response = requests.get(
            f"{VERCEL_API_URL}/user",
            headers=headers
        )
        
        if user_response.status_code != 200:
            print(f"❌ Failed to get user info: {user_response.status_code}")
            return False
        
        user = user_response.json()
        user_id = user['id']
        
        # Create project
        project_data = {
            "name": "medical-insights-frontend",
            "framework": "vite",
            "buildCommand": "npm run build",
            "outputDirectory": "dist",
            "installCommand": "npm install",
            "rootDirectory": "frontend",
            "env": [
                {
                    "key": "VITE_API_URL",
                    "value": backend_url,
                    "target": ["production", "preview", "development"]
                }
            ]
        }
        
        # Create project
        project_response = requests.post(
            f"{VERCEL_API_URL}/projects",
            headers=headers,
            json=project_data
        )
        
        if project_response.status_code == 201:
            project = project_response.json()
            project_id = project['id']
            print(f"✅ Frontend project created with ID: {project_id}")
            
            # Deploy the project
            deploy_data = {
                "name": "medical-insights-frontend",
                "target": "production"
            }
            
            deploy_response = requests.post(
                f"{VERCEL_API_URL}/projects/{project_id}/deployments",
                headers=headers,
                json=deploy_data
            )
            
            if deploy_response.status_code == 200:
                deployment = deploy_response.json()
                deployment_id = deployment['id']
                print(f"✅ Deployment started with ID: {deployment_id}")
                
                # Wait for deployment
                print("⏳ Waiting for deployment to complete...")
                time.sleep(60)  # Wait for deployment
                
                # Get deployment status
                status_response = requests.get(
                    f"{VERCEL_API_URL}/deployments/{deployment_id}",
                    headers=headers
                )
                
                if status_response.status_code == 200:
                    deployment_info = status_response.json()
                    deployment_url = deployment_info.get('url')
                    if deployment_url:
                        print(f"🎉 Frontend deployed successfully!")
                        print(f"🌐 URL: https://{deployment_url}")
                        return f"https://{deployment_url}"
                    else:
                        print("⚠️ Deployment completed but URL not available yet")
                        return None
                else:
                    print(f"❌ Failed to get deployment status: {status_response.status_code}")
                    return None
                    
            else:
                print(f"❌ Failed to start deployment: {deploy_response.status_code}")
                print(f"Response: {deploy_response.text}")
                return None
                
        else:
            print(f"❌ Failed to create project: {project_response.status_code}")
            print(f"Response: {project_response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error deploying to Vercel: {str(e)}")
        return False

if __name__ == "__main__":
    backend_url = input("Enter your Render backend URL: ")
    deploy_to_vercel(backend_url)
