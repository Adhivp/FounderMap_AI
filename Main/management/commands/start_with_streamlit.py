from django.core.management.base import BaseCommand
import subprocess
import os

class Command(BaseCommand):
    help = 'Run Django server and Streamlit application'

    def handle(self, *args, **options):
        # Function to run Streamlit server
        def run_streamlit():
            streamlit_cmd = [
                'streamlit', 'run', 'main/main.py',
                '--server.port', '8501',
                '--server.enableCORS', 'false'
            ]
            # Run Streamlit as a background process
            subprocess.Popen(streamlit_cmd)

        # Function to run Django server
        def run_django():
            django_cmd = [
                'python', 'manage.py', 'runserver'
            ]
            subprocess.run(django_cmd, check=True)

        # Start Streamlit server in background
        run_streamlit()

        # Start Django server in main thread
        run_django()
