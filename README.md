# Meeting Notes Summarizer Backend

A backend service that summarizes meeting transcripts using a transformer-based model.

## Setup Instructions

### Requirements

- Python 3.10+
- Docker (for containerized deployment)

### Local Setup

```bash
git clone https://github.com/<your-username>/meeting-notes-backend.git
cd meeting-notes-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
