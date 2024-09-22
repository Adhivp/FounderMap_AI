import os
import subprocess
import sys
from azure.functions import HttpRequest, HttpResponse

# Define the port for Streamlit (default is 8501)
STREAMLIT_PORT = 8501

def start_django():
    """Start the Django application."""
    # Start Django using manage.py's runserver
    subprocess.Popen([sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'])

def start_streamlit():
    """Start the Streamlit application on a different port."""
    # Start Streamlit on the specified port (e.g., 8501)
    subprocess.Popen([sys.executable, '-m', 'streamlit', 'run', 'Main/main.py', '--server.port', str(STREAMLIT_PORT)])

def main(req: HttpRequest) -> HttpResponse:
    """Azure Function entry point."""
    
    # Check if the services are already running
    try:
        if os.environ.get('WEBSITE_INSTANCE_ID') is None:
            # Only start Django and Streamlit if running locally
            print("Starting Django and Streamlit...")
            start_django()
            start_streamlit()
        else:
            print("Azure environment detected, skipping local start.")
    except Exception as e:
        print(f"Error starting apps: {e}")
        return HttpResponse(f"Error: {e}", status_code=500)

    return HttpResponse("Both Django and Streamlit are running!", status_code=200)
