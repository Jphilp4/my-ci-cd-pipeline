import sys
import time

def mock_deploy():
    print("Starting mock deployment process...")
    steps = [
        "Preparing application for deployment",
        "Checking dependencies",
        "Compressing application files",
        "Uploading to mock server",
        "Configuring mock server environment",
        "Starting application on mock server",
        "Running post-deployment checks"
    ]
    
    for step in steps:
        print(f"Step: {step}")
        time.sleep(1)  # Simulate some processing time
    
    print("Mock deployment completed successfully!")

if __name__ == "__main__":
    mock_deploy()
    sys.exit(0)  # Exit with success status
