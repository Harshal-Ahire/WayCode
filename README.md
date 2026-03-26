Markdown# WayCode - AI-Powered Code Refactoring Agent

An intelligent CLI code refactoring assistant that learns your coding style using RAG (Retrieval-Augmented Generation) architecture with vector search and LLM integration.

## Features

- **AI-Powered Refactoring** - Uses Google Gemini API with web search for latest best practices.
- **RAG Pipeline** - Vector search with ChromaDB to inject relevant code context into prompts.
- **Learning Memory** - Remembers your coding patterns and preferences across sessions.
- **Multi-Language Support** - Python, JavaScript, TypeScript, Java, Go, and more.
- **Performance Optimized** - Identifies and fixes $O(N)$ to $O(1)$ improvements.
- **Modern Standards** - Enforces PEP 8, type hints, error handling, and clean code principles.

## Tech Stack

- **Backend**: Python, FastAPI
- **AI/ML**: Google Gemini API, RAG Architecture
- **Vector Database**: ChromaDB with semantic embeddings
- **CLI**: Click framework
- **Async Processing**: Concurrent session handling with parallel LLM calls

## Architecture

```text
User Code → Vector Search → Context Retrieval → LLM Prompt → Refactored Code
                ↓
          Memory Storage (learns patterns)
The RAG pipeline enables accurate multi-file refactoring beyond standard context window limits by retrieving relevant code examples from your project history.🛡️ Reliability & Security (Production Focused)Rate Limit Management: Implemented exponential backoff for Gemini API calls to handle high-frequency refactoring sessions without overhead.Token Optimization: Uses a dynamic sliding window for context retrieval to ensure the most relevant code snippets are prioritized within the LLM’s context limits.PII & IP Security: Designed for local-first vector storage (~/.waycode/). Sensitive codebase indices and metadata never leave the local environment, ensuring compliance with enterprise security standards.Atomic File Operations: Refactored code is written to temporary buffers before finalization to prevent data loss during interruptions.InstallationBashgit clone [https://github.com/Harshal-Ahire/WayCode.git](https://github.com/Harshal-Ahire/WayCode.git)
cd WayCode
pip install -r requirements.txt
SetupGet a free Gemini API key from Google AI StudioCreate .env file:BashGEMINI_API_KEY=your_api_key_here
Install the package:Bashpip install -e .
UsageRefactor a fileBashpython -m waycode.cli refactor mycode.py
Learn from your codebaseBashpython -m waycode.cli index myproject/ -r
Custom output locationBashpython -m waycode.cli refactor app.py -o refactored_app.py
ExampleBefore:Pythondef getData():
    import requests
    x = requests.get('[https://api.example.com/users](https://api.example.com/users)')
    return x.json()

def getUser(id):
    for user in users:
        if user['id'] == id:
            return user
After:Pythonimport requests
from typing import Optional, Dict

def get_data() -> Optional[Dict]:
    """Fetches user data from API."""
    try:
        # Implemented timeout and error handling for production reliability
        response = requests.get('[https://api.example.com/users](https://api.example.com/users)', timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # Logging error for observability
        print(f"Error: {e}")
        return None

def get_user(user_id: int) -> Optional[Dict]:
    """Retrieves user by ID with O(1) lookup."""
    return users_dict.get(user_id)
What WayCode FixesNaming Conventions: Enforces PEP 8 and language-specific standards.Performance Optimization: $O(N) \to O(1)$ lookups and asynchronous code migration.Defensive Programming: Comprehensive error handling and edge-case validation.Structural Integrity: Import organization, type hinting, and docstring generation.How It WorksAnalysis - Scans your code for issues and patterns.Context Retrieval - Searches ChromaDB for semantically similar code examples.LLM Processing - Gemini API generates refactored code with real-time web search for the latest libraries.Memory Storage - Learns your naming and formatting preferences for future refactorings.Output - Saves clean code with detailed explanations of changes.Project StructurePlaintextwaycode/
├── waycode/
│   ├── cli.py              # Command-line interface
│   ├── config.py           # Configuration and prompts
│   ├── refactor_agent.py   # Main refactoring engine
│   ├── rag/                # RAG pipeline components
│   │   ├── vector_store.py
│   │   ├── embeddings.py
│   │   ├── memory_manager.py
│   │   └── context_builder.py
│   └── utils/              # Utilities
│       ├── code_analyzer.py
│       └── diff_generator.py
├── examples/
├── requirements.txt
└── setup.py
Data StorageVector database: ~/.waycode/data/vector_db/Memory: ~/.waycode/data/project_memory.jsonHistory: ~/.waycode/data/refactor_history.json
