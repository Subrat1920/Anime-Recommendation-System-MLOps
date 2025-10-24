# ==============================
# Base Image
# ==============================
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (optional but common)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git gcc \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# Install Dependencies
# ==============================
# Copy only dependency files first to leverage caching
COPY requirements.txt setup.py ./

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Install dependencies (includes -e . for editable install)
RUN pip install --default-timeout=200 --retries 10 --no-cache-dir -r requirements.txt

# ==============================
# Copy Source Code
# ==============================
COPY . .

# ==============================
# Expose Flask Port & Run
# ==============================
EXPOSE 5000

# Default command to run the Flask app
# (update "app:app" if your main file or Flask instance name differs)
CMD ["python", "application.py"]
