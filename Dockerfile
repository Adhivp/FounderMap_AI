# Use Python slim image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Make ports 8000 and 8501 available to the world outside this container
EXPOSE 8000 8501

# Run the application
CMD ["sh", "-c", "python3 manage.py runserver 0.0.0.0:8000 & streamlit run main.py"]