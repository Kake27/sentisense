# 🎯 SentiSense – Comment Sentiment Analyzer & Insights Engine

SentiSense is a full-stack web app that scrapes comments from popular platforms like YouTube, and Reddit, performs deep sentiment analysis using a custom-trained NLP model, clusters the results, and provides AI-powered suggestions for improvement using Gemini AI.

---

## 🚀 Features

- 🔎 **Multi-platform scraping** (Reddit, YouTube)
- 💡 **Custom sentiment analysis model** (`.h5` + tokenizer `.pkl`)
- 📊 **Sentiment trend graphs and clustering**
- 🤖 **AI-generated suggestions** (via Gemini API)
- 📁 CSV export of analyzed results
- 💻 Built with FastAPI + TensorFlow + HuggingFace + Pandas

---

## 🧠 Tech Stack

| Layer        | Tech Used                      |
|--------------|-------------------------------|
| **Frontend** | React.js, axios       |
| **Backend**  | FastAPI, Uvicorn              |
| **Modeling** | TensorFlow (Keras), Tokenizer, HuggingFace Transformers |
| **Scraping** | yt-dlp (Youtube) and praw (Reddit)        |
| **AI Assist**| Gemini API (LLM)              |
| **Infra**    | OnRender / Localhost          |

---

## ⚙️ Installation & Usage
### 1) Clone the repo:
       git clone https://github.com/yourusername/sentisense.git in the console
       Change to the project directory: cd sentisense
### 2) Create the virtual environment:
       python -m venv venv
       venv\Scripts\activate
### 3) Install dependencies:
       Change the directory to backend
       pip install -r requirements.txt
### 4) Add .env variables:
       Get your client id, client secret by registering an app on Reddit and add them to the file
       Also add your GenAI API key 
### 5) Run the backend server:
       uvicorn runserver:app --reload
### 6) Install frontend dependencies:
       Change to the frontend directory 
       Run npm i
### 7) Run frontend server:
       npm run dev


