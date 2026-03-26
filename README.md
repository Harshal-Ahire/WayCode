# WayCode - AI-Powered Code Refactoring Agent

An intelligent CLI-based code refactoring assistant that learns your coding style using a Retrieval-Augmented Generation (RAG) pipeline with vector search and LLM integration.

WayCode goes beyond simple formatting by performing **context-aware, multi-file refactoring**, improving code quality, structure, and performance while adapting to your project-specific patterns.

---

## Features

- **AI-Powered Refactoring** – Uses Google Gemini API with web search to apply up-to-date best practices  
- **RAG Pipeline** – Retrieves semantically relevant code context using ChromaDB to guide refactoring  
- **Learning Memory** – Adapts to your coding style and project patterns across sessions  
- **Multi-Language Support** – Python, JavaScript, TypeScript, Java, Go, and more  
- **Performance Optimization** – Detects and improves inefficient patterns (e.g., O(N) → O(1))  
- **Modern Standards** – Enforces PEP 8, type hints, error handling, and clean architecture principles  

---

## Tech Stack

- **Backend**: Python, FastAPI  
- **AI/ML**: Google Gemini API, RAG Architecture  
- **Vector Database**: ChromaDB (semantic embeddings)  
- **CLI**: Click framework  
- **Concurrency**: Async processing with parallel LLM calls  

---

## Architecture

```
User Code → Vector Search → Context Retrieval → LLM Prompt → Refactored Code
                ↓
          Memory Storage (pattern learning)
```

The RAG pipeline enables **accurate multi-file refactoring beyond context window limits** by retrieving relevant code examples and patterns from indexed project history.

---

## Advanced Details

- **Chunking Strategy**: Code is segmented at function/class level to preserve semantic meaning  
- **Context Ranking**: Retrieved snippets are ranked via embedding similarity (cosine distance)  
- **Multi-file Awareness**: Dynamically injects relevant files to handle cross-file dependencies  
- **Prompt Engineering**: Structured prompts enforce consistency, safety, and best practices  
- **Failure Handling**: Responses are validated to prevent syntax errors and unsafe transformations  
- **Learning Memory**: Stores project-specific patterns and reuses them for consistent refactoring  
- **Scalability**: Designed to handle large codebases through retrieval instead of full-context loading  

---

## Installation

```bash
git clone https://github.com/Harshal-Ahire/WayCode.git
cd WayCode
pip install -r requirements.txt
```

---

## Setup

1. Get a free Gemini API key from: https://aistudio.google.com/apikey  

2. Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

3. Install the package:

```bash
pip install -e .
```

---

## Usage

### Refactor a file

```bash
python -m waycode.cli refactor mycode.py
```

### Learn from your codebase

```bash
python -m waycode.cli index myproject/ -r
```

### Custom output location

```bash
python -m waycode.cli refactor app.py -o refactored_app.py
```

---

## Example

**Before:**
```python
def getData():
    import requests
    x = requests.get('https://api.example.com/users')
    return x.json()

def getUser(id):
    for user in users:
        if user['id'] == id:
            return user
```

**After:**
```python
import requests
from typing import Optional, Dict

def get_data() -> Optional[Dict]:
    """Fetches user data from API."""
    try:
        response = requests.get('https://api.example.com/users', timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def get_user(user_id: int) -> Optional[Dict]:
    """Retrieves user by ID with O(1) lookup."""
    return users_dict.get(user_id)
```

---

## What WayCode Fixes

- Naming conventions (PEP 8 compliance)  
- Type hints and documentation  
- Error handling and edge cases  
- Performance issues (O(N) → O(1))  
- Code smells and anti-patterns  
- Modern syntax and best practices  
- Import organization  
- Defensive programming patterns  

---

## How It Works

1. **Analysis** – Scans code to detect patterns, inefficiencies, and anti-patterns  
2. **Context Retrieval** – Fetches relevant examples from the vector database  
3. **LLM Processing** – Generates refactored code using Gemini with enriched context  
4. **Memory Storage** – Stores useful patterns for future reuse  
5. **Output Generation** – Produces clean, optimized code with improvements applied  

---

## Project Structure

```bash
waycode/
├── waycode/
│   ├── cli.py                      # Command-line interface
│
│   ├── agents/                    # Core AI agents
│   │   ├── refactor_agent.py      # Orchestrates refactoring workflow
│   │   ├── prompt_builder.py      # Constructs structured LLM prompts
│   │   └── response_parser.py     # Validates and parses LLM outputs
│
│   ├── retrieval/                 # RAG pipeline (context retrieval)
│   │   ├── vector_store.py        # ChromaDB interactions
│   │   ├── embeddings.py          # Embedding generation
│   │   ├── retriever.py           # Fetches relevant code snippets
│   │   ├── ranker.py              # Ranks context using similarity
│   │   └── context_builder.py     # Builds final prompt context
│
│   ├── services/                  # Business logic layer
│   │   └── refactor_service.py    # High-level refactoring orchestration
│
│   ├── memory/                    # Learning system
│   │   └── memory_manager.py      # Stores and retrieves coding patterns
│
│   ├── prompts/                   # Prompt templates
│   │   ├── refactor_prompt.txt
│   │   └── system_prompt.txt
│
│   ├── utils/                     # Utility modules
│   │   ├── code_analyzer.py
│   │   └── diff_generator.py
│
│   └── config.py                  # Configuration and global settings
│
├── tests/                         # Unit and integration tests
├── examples/                      # Sample inputs and outputs
├── requirements.txt
└── setup.py
```

---

## Architecture Overview

WayCode follows a layered architecture to ensure modularity, scalability, and maintainability:

- **CLI Layer** → Handles user interaction and command parsing  
- **Service Layer** → Orchestrates refactoring workflows  
- **Agent Layer** → Manages LLM interaction and prompt lifecycle  
- **Retrieval Layer (RAG)** → Fetches and ranks relevant code context  
- **Memory Layer** → Stores and reuses learned coding patterns  

This separation enables:
- Easier testing and extensibility  
- Clear boundaries between AI logic and application logic  
- Scalable handling of large, multi-file codebases  

---

## Data Storage

- **Vector Database**: `~/.waycode/data/vector_db/`  
- **Memory Store**: `~/.waycode/data/project_memory.json`  
- **History**: `~/.waycode/data/refactor_history.json`  

All data is stored locally and remains private to your machine.

---

## Notes

WayCode is designed as a **developer-first AI tool**, focusing on:
- Practical code quality improvements  
- Maintainability and readability  
- Scalable AI-assisted workflows  

Future improvements may include:
- Automated evaluation benchmarks  
- IDE integrations  
- Fine-tuned models for code-specific tasks  
