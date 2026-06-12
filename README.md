# 🤖 AgentBot: Autonomous AI Agentic System

An advanced, modular AI Agent platform designed to facilitate complex, multi-step agentic workflows. By leveraging a decoupled Client-Server architecture, this system provides a highly responsive UI with a robust, scalable backend capable of executing agentic tasks, tool-calling, and dynamic reasoning.

---

## 🚀 Key Features

* **Agentic Orchestration:** Built with an `agent.py` core to handle autonomous decision-making and tool-usage logic.
* **Decoupled Architecture:** Clean separation between the Streamlit-based frontend and the FastAPI backend for improved maintainability.
* **Optimized Dependency Management:** Built using `uv` for blazing-fast environment setup and resolution.
* **Persistent Session Management:** Intuitive UI controls for handling chat sessions, context, and state.
* **Modular Vector Storage:** Encapsulated vector retrieval logic, allowing for easy swaps between various storage providers and embedding models.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend UI** | Streamlit |
| **Backend Framework** | FastAPI |
| **Agent Framework** | LangChain / LangGraph |
| **Package Manager** | `uv` |
| **Vector Store** | Pinecone / FAISS |

---

## 📁 Architecture Overview

```text
├── backend/
│   ├── agent.py            # Core agent logic and tool orchestration
│   ├── config.py           # Backend environment/settings configuration
│   ├── main.py             # FastAPI server entry point
│   └── vectorstore.py      # Vector database connection and retrieval logic
├── frontend/
│   ├── app.py              # Main Streamlit UI entry point
│   ├── backend_api.py      # HTTP client requests to the backend
│   ├── session_manager.py  # User session and state management
│   └── ui_components.py    # Reusable Streamlit UI widgets
├── requirements.txt        # Dependency list
└── uv.lock                 # Fast dependency resolution lock file


## ⚙️ Getting Started
1. Installation
This project uses uv for dependency management. If you don't have it installed:
```bash
pip install uv
```

Clone the repo and sync your environment:
```bash
git clone [https://github.com/your-username/agentbot.git](https://github.com/your-username/agentbot.git)
cd agentbot
uv sync
```

2. Environment Setup
Create a .env file in the root directory:
```bash
GROQ_API_KEY="your_groq_api_key_here"
PINECONE_API_KEY="your_pinecone_api_key_here"
PINECONE_ENVIRONMENT="your_pinecone_environment"
TAVILY_API_KEY="your_tavily_api_key"
FASTAPI_BASE_URL="http://localhost:8000"
```
3. Running the System
You need to run both the backend and frontend simultaneously:

Terminal 1: Start the Backend (FastAPI)

```bash
cd backend
# Activate your venv if needed: source .venv/bin/activate
uvicorn main:app --reload
```
Terminal 2: Start the Frontend (Streamlit)
```bash
cd frontend
streamlit run app.py
```

## 🛡️ Modular Design Philosophy
The frontend/ package is kept intentionally lightweight, handling only state and UI rendering, while the backend/ handles the "heavy lifting"—reasoning, RAG retrieval, and agentic tool-use. This allows for independent scaling and testing of your agent logic.

