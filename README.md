# AI Journaling Companion

A lightweight, privacy-first journaling API that helps users reflect on daily thoughts using basic AI sentiment analysis.

## What This Project Does

- Users submit short journal entries  
- The API analyzes sentiment and subjectivity  
- Entries are stored locally (no cloud, no external APIs)  
- A summary endpoint shows trends over time  

This project demonstrates:
- API design  
- Clean modular architecture  
- Basic NLP usage  
- Input validation via FastAPI  


## How It Works

1. User submits a journal entry via the API  
2. Text is analyzed using TextBlob  
3. Sentiment & subjectivity scores are generated  
4. Entry is stored locally  
5. Summary endpoint aggregates insights  

## Tech Stack

- Python 3  
- FastAPI  
- TextBlob (NLP)  
- Local JSON storage  
- Uvicorn (ASGI server)  

## How to Run Locally

### 1. Verify Python Installation
```bash
python3 --version

### 2. Start the API
python3 -m uvicorn src.main:app --reload

### 3. Open API Docs
http://127.0.0.1:8000
http://127.0.0.1:8000/docs


