# AI Resume Job Matcher

An AI-powered web application that matches resumes with job descriptions using NLP and Machine Learning.

## Features
- Resume PDF upload
- Job description analysis
- Match score (0–100%)
- Explainable keyword overlap
- REST API + Web UI

## Tech Stack
- Python
- Flask
- scikit-learn
- NLP (TF-IDF, Cosine Similarity)
- PyPDF2

## How It Works
1. Extracts text from resume PDF
2. Cleans and preprocesses text
3. Converts text to vectors using TF-IDF
4. Computes similarity using cosine similarity

## Run Locally
```bash
pip install -r requirements.txt
python app.py
