FROM python:3.10-slim

WORKDIR /app

# System packages needed for pip + dependencies
RUN apt-get update && apt-get install -y \
    build-essential gcc libffi-dev libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install pip dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install torch==2.2.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
