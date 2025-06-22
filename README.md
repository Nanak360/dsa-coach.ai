# 📚 DSA Coach — Interview Preparation AI Assistant

**DSA Coach** is a full-stack AI-powered web application designed to help users prepare effectively for coding interviews. It intelligently adapts to each user's background, learning preferences, and goals using LLMs and customizable learning paths.

---

## 🚀 Features

- 🧠 AI-powered syllabus generation using LangGraph + LLMs
- 🎯 Personalized onboarding to understand your goals and current level
- 🗺️ Dynamic study plan generation (with future support for feedback loops)
- 💬 Chat-based AI coach for problem-solving guidance
- 🔐 Structured backend using FastAPI
- 🌐 Modern frontend (client app) with React or Next.js (in `client/`)
- 🧪 Modular service-based monorepo architecture

---

## 📂 Project Structure

```
dsa-coach/
│
├── client/              # Frontend (React/Next.js app)
├── server/              # Backend (FastAPI app)
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── services/    # Business logic (e.g. onboarding, chat)
│   │   └── main.py      # Entry point
│   └── requirements.txt
├── .gitignore
└── README
```

---

## 🛠️ Tech Stack

**Frontend**: React / Next.js  
**Backend**: FastAPI, LangChain, LangGraph, Ollama  
**LLMs**: Ollama (local), OpenAI (optional)  
**Deployment**: Dev ready. Docker support planned.

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/dsa-coach.git
cd dsa-coach
```

### 2. Start the backend
```bash
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Start the frontend
```bash
cd ../client
npm install
npm run dev
```

### 4. One-click start (optional)
Use the provided `start.sh` script to launch both backend and frontend together.

---

## 📌 To-Do

- [x] Initial onboarding API
- [x] Chat API integration
- [ ] AI syllabus generation
- [ ] Session tracking
- [ ] User progress dashboard
- [ ] Auth & persistence layer

---

## 🤝 Contributing

Got an idea or feedback? PRs are welcome!

---

## 📄 License

MIT License © 2025