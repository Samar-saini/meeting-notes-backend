# Meeting Notes Summarizer Backend

A backend service that summarizes meeting transcripts using a transformer-based model.

## Setup Instructions

### Requirements

- Python 3.10+
- Docker (for containerized deployment)
###Architecture:-
FastAPI: Web framework

Transformers (HuggingFace): Summarization model

Docker: Deployment containerization

Optional: Redis + Celery for async processing

###Assumptions:-
Input is a single string of raw meeting notes.

Output is a single summary.

Model used is sshleifer/distilbart-cnn-12-6 to reduce memory requirements.


### Local Setup

```bash
git clone https://github.com/<your-username>/meeting-notes-backend.git
cd meeting-notes-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000



