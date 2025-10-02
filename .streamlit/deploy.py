import os
import subprocess
import sys

def deploy_to_streamlit_cloud():
    """Deploy the application to Streamlit Cloud"""
    print("🚀 Preparing for Streamlit deployment...")
    
    # Check if all required files exist
    required_files = ['app.py', 'requirements.txt']
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Missing required file: {file}")
            return False
    
    print("✅ All required files found")
    print("📁 Project structure ready for deployment")
    
    print("""
    📋 Deployment Instructions:
    
    1. Push this code to a GitHub repository
    2. Go to https://share.streamlit.io
    3. Connect your GitHub account
    4. Select this repository
    5. Set main file path to: app.py
    6. Click 'Deploy'
    
    🔗 Your app will be available at: https://your-app-name.streamlit.app
    """)
    
    return True

if __name__ == "__main__":
    deploy_to_streamlit_cloud()
