# LangChain Project

A comprehensive LangChain-based project demonstrating various AI applications including agents, chatbots, RAG systems, and API integrations.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Technologies](#technologies)

## 🔍 Overview

This project showcases different implementations of LangChain for building AI-powered applications. It includes chatbots with OpenAI and Ollama, RAG (Retrieval-Augmented Generation) systems, AI agents, and API services.

## 📁 Project Structure

```
LANGCHAIN/
│
├── agents/                      # AI Agents Implementation
│   └── agents.ipynb            # Jupyter notebook with agent examples
│
├── api/                        # API Services
│   ├── app.py                 # FastAPI application with LangServe
│   └── client.py              # API client for testing endpoints
│
├── chain/                      # Chain Examples with RAG
│   ├── retriever.ipynb        # Retrieval chain implementations
│   └── attention.pdf          # Sample PDF document for processing
│
├── chatbot/                    # Chatbot Applications
│   ├── app.py                 # OpenAI-based chatbot with Streamlit
│   └── localama.py            # Local Ollama chatbot implementation
│
├── rag/                        # RAG (Retrieval-Augmented Generation)
│   ├── simplerag.ipynb        # Simple RAG implementation notebook
│   ├── attention.pdf          # Research paper for RAG demonstration
│   └── speech.txt             # Text data for retrieval
│
├── venv/                       # Virtual environment (not tracked)
│
├── .env                        # APT KEYS
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
└── README.md                  
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- OpenAI API key (for OpenAI models)
- Ollama installed (for local models)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LANGCHAIN
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the root directory
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## ✨ Features

### 🤖 AI Agents (`agents/`)
- Custom AI agents using LangChain
- Agent workflows and decision-making
- Tool integration and function calling
- Jupyter notebook with interactive examples

### 🌐 API Services (`api/`)
- **app.py**: RESTful API built with FastAPI and LangServe
  - Expose LangChain chains as API endpoints
  - Easy integration with web applications
- **client.py**: Python client for testing API endpoints

### 🔗 Retrieval Chains (`chain/`)
- **retriever.ipynb**: Advanced retrieval chain implementations
  - Document processing from PDFs
  - Vector store integration
  - Semantic search capabilities
- Sample PDF documents for testing

### 💬 Chatbots (`chatbot/`)
- **app.py**: Streamlit-based chatbot using OpenAI
  - Interactive web interface
  - Conversation history
  - Real-time responses
- **localama.py**: Local chatbot using Ollama
  - Privacy-focused (runs locally)
  - No API costs
  - Customizable models

### 📚 RAG System
- **simplerag.ipynb**: Complete RAG implementation
  - Document loading and chunking
  - Embedding generation
  - Vector database storage (FAISS/Chroma)
  - Contextual question answering
- Supports PDFs, text files, and Wikipedia
- Integration with arXiv for research papers

## 🚀 Usage

### Running the Chatbot (OpenAI)
```bash
cd chatbot
streamlit run app.py
```

### Running the Local Chatbot (Ollama)
```bash
cd chatbot
streamlit run localama.py
```

### Starting the API Server
```bash
cd api
python app.py
```

### Testing the API Client
```bash
cd api
python client.py
```

### Using Jupyter Notebooks
```bash
jupyter notebook
# Navigate to agents/agents.ipynb, chain/retriever.ipynb, or rag/simplerag.ipynb
```

## 🔧 Technologies

### Core Frameworks
- **LangChain**: Framework for LLM applications
- **LangChain OpenAI**: OpenAI integration
- **LangChain Ollama**: Local LLM integration
- **LangServe**: Deploy LangChain as REST APIs

### Web Frameworks
- **FastAPI**: Modern web framework for APIs
- **Streamlit**: Web UI for chatbot applications
- **Uvicorn**: ASGI server

### ML & AI
- **Sentence Transformers**: Text embeddings
- **FAISS**: Vector similarity search
- **ChromaDB**: Vector database

### Data Processing
- **BeautifulSoup4 (bs4)**: Web scraping
- **PyPDF**: PDF processing
- **Wikipedia**: Wikipedia API integration
- **arXiv**: Research paper access

### Utilities
- **python-dotenv**: Environment variable management
- **sse_starlette**: Server-sent events

## 📝 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key
# Add other API keys as needed
```

### Model Configuration

- **OpenAI Models**: Configured in chatbot/app.py
- **Ollama Models**: Configured in chatbot/localama.py
- Modify model parameters in respective files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

**Note**: Make sure to keep your API keys secure and never commit them to version control. Always use environment variables for sensitive information.
