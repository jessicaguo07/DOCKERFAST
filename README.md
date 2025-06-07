# 🧠 FastAPI Sentiment Analysis API

This project is a production-ready **FastAPI** application that serves a **sentiment analysis model** (`cardiffnlp/twitter-roberta-base-sentiment`) for scoring short text inputs (e.g., tweets) as **positive**, **neutral**, or **negative**.

---

## 📌 Features

- ✅ RESTful API with FastAPI
- ✅ Uses HuggingFace Transformers + PyTorch
- ✅ Softmax-normalized sentiment scoring
- ✅ Secure endpoint with API key validation
- ✅ Clean text preprocessing pipeline
- ✅ Docker-ready with `.gitignore` for model size control

---

## 🔧 Requirements

Install dependencies in a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
