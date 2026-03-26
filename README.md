# WayCode — AI-Powered Code Refactoring System

WayCode is an AI-driven developer tool that performs **context-aware, multi-file code refactoring** using a Retrieval-Augmented Generation (RAG) pipeline.

It is designed as an **AI-assisted development workflow**, embedding LLM capabilities directly into real coding environments to improve code quality, performance, and maintainability.

---

## Overview

WayCode automates code refactoring by combining:
- Semantic code retrieval using embeddings  
- Context-aware LLM reasoning  
- Persistent memory of project-specific patterns  

The system overcomes LLM context limitations by dynamically retrieving relevant code across files.

---

## Key Capabilities

- **RAG-Based Refactoring Pipeline**  
  Retrieves relevant code context using vector search and injects it into LLM prompts.

- **Multi-file Context Awareness**  
  Handles cross-file dependencies by dynamically constructing context.

- **Learning Memory System**  
  Stores project-specific patterns and reuses them for consistent refactoring.

- **Workflow Integration (CLI)**  
  Operates as a CLI tool embedded directly into developer workflows.

- **Performance Optimization**  
  Identifies inefficient patterns and improves algorithmic complexity.

- **Safe Code Transformation**  
  Validates outputs to prevent syntax errors and unsafe changes.

---

## Architecture

```
User Code → Vector Search → Context Retrieval → LLM Prompt → Refactored Code
                ↓
          Memory Storage
```

---

## Advanced Engineering Details

- **Chunking Strategy**  
  Code is segmented at function/class level to preserve semantic meaning.

- **Context Ranking**  
  Uses embedding similarity (cosine distance) to prioritize relevant snippets.

- **Dynamic Context Injection**  
  Builds prompts from multi-file context to overcome token limitations.

- **Prompt Structuring**  
  Enforces consistency, coding standards, and safe outputs.

- **Scalable Design**  
  Handles large repositories using retrieval instead of full-context processing.

---

## Engineering Highlights

- **RAG Applied to Developer Workflows**  
  Integrates retrieval-based AI reasoning into real coding tasks.

- **AI + Systems Integration**  
  Combines vector databases, LLMs, and CLI tooling into a unified system.

- **Automation of Repetitive Tasks**  
  Reduces manual effort in refactoring while maintaining correctness.

---

## Tech Stack

- **Backend**: Python, FastAPI  
- **AI/ML**: Google Gemini API  
- **Vector Database**: ChromaDB  
- **CLI**: Click  
- **Concurrency**: Async processing  

---

## Usage

### Refactor a file

```bash
python -m waycode.cli refactor mycode.py
```

### Index a codebase

```bash
python -m waycode.cli index myproject/ -r
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

## Planned Improvements

- Modular agent architecture for LLM orchestration  
- Dedicated retrieval components (retriever, ranker)  
- Externalized prompt templates  
- Test suite for validation and reliability  

---

## Data Storage

- Vector DB: `~/.waycode/data/vector_db/`  
- Memory: `~/.waycode/data/project_memory.json`  
- History: `~/.waycode/data/refactor_history.json`  

---

## Design Philosophy

WayCode focuses on:
- Practical developer productivity improvements  
- Maintainability and correctness  
- Scalable AI-assisted workflows  
