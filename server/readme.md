# DSA Coach Server

A backend server built with **FastAPI** and **LangChain** for the DSA Coach project. This server uses **Ollama** for running local LLMs and provides intelligent coaching for data structure and algorithm interview preparation.

## Features

- RESTful API endpoints via FastAPI
- Local LLM integration using Ollama
- LangChain for LLM orchestration
- Auto-generated interactive API docs (Swagger UI)
- Scalable modular architecture
- Easy integration with vector DBs and TTS

## Requirements

- Python 3.10+
- FastAPI
- LangChain
- Ollama (running locally)
- Uvicorn

## Installation

```bash
git clone https://github.com/yourusername/dsa-coach.git
cd dsa-coach/server
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running the Server

Make sure you have Ollama running with your desired model (e.g., `llama3`):

```bash
ollama run llama3
```

Then start the backend:

```bash
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger API documentation.

## Project Structure

```
server/
├── app/
│   ├── api/              # Route handlers
│   ├── core/             # Config, env setup
│   ├── database/         # DB utilities
│   ├── models/           # Pydantic models
│   ├── services/         # LLM, syllabus logic, etc.
│   ├── utils/            # Helpers and shared utilities
│   └── main.py           # App entrypoint
├── .env
├── .gitignore
├── requirements.txt
└── readme.md
```

## License

MIT