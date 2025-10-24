FROM python:3.8-slim

# Prevent Python from buffering stdout/stderr and writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies for TensorFlow and scientific libs
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libhdf5-dev \
    libprotobuf-dev \
    protobuf-compiler \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && \
    pip install --default-timeout=200 --retries 10 --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# (Optional) Train the model inside container — slow, use only if necessary
RUN python pipeline/training_pipeline.py

# Expose the Flask port
EXPOSE 5000

# Default command
CMD ["python", "application.py"]
