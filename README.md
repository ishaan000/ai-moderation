# Moderation AI (FastAPI + OpenAI)
This project implements a moderation API using **FastAPI**, **Docker**, and **OpenAI's Moderation API**.
It detects and flags potentially harmful content such as hate speech, harassment, and violence, aligning with industry-standard practices for content moderation.

## Features

- **Content moderation** using OpenAI's Moderation API
- Docker containerization for reproducibility and portability
- Prepared for Kubernetes deployment

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd moderation-api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure OpenAI API key
Create .env in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```
### 5. Run the FastAPI app locally
```bash
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs to interact with the API.

### 6. Dockerize & Run
```bash
docker build -t moderation-ai:latest .
docker run -p 8000:8000 --env-file=.env moderation-ai:latest
```
