# WayCode - AI-Powered Code Refactoring Agent

<!--
WayCode is an AI-powered code refactoring tool built to solve a real limitation of LLMs:
large codebases exceed context windows, making refactoring unreliable.

This project uses Retrieval-Augmented Generation (RAG) with vector search
to retrieve only the most relevant code context, enabling accurate multi-file refactoring
while preserving coding style and improving performance.
-->

<!-- ===========================
CORE FEATURES
=========================== -->

<!--
- Uses Google Gemini as the LLM for refactoring decisions
- RAG pipeline with ChromaDB to retrieve relevant code context
- Learns user coding patterns across runs (style memory)
- Optimizes performance issues such as O(N) → O(1)
- Enforces clean code standards (PEP 8, typing, error handling)
- Supports multiple languages (Python, JS, TS, Java, Go)
-->

<!-- ===========================
ARCHITECTURE
=========================== -->

```text
User Code → Vector Search → Context Retrieval → LLM → Refactored Code
                ↓
          Persistent Style Memory

# Refactor a single file
python -m waycode.cli refactor mycode.py

# Index a project to build vector embeddings and learn style
python -m waycode.cli index myproject/ -r

# Refactor with custom output path
python -m waycode.cli refactor app.py -o refactored_app.py

# BEFORE: no typing, no error handling, O(N) lookup

def getData():
    import requests
    x = requests.get("https://api.example.com/users")
    return x.json()

def getUser(id):
    for user in users:
        if user["id"] == id:
            return user

# AFTER: typed, defensive, clean, O(1) lookup

import requests
from typing import Optional, Dict

def get_data() -> Optional[Dict]:
    try:
        response = requests.get("https://api.example.com/users", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def get_user(user_id: int) -> Optional[Dict]:
    return users_dict.get(user_id)

<!-- =========================== WHAT THE AGENT FIXES =========================== --> <!-- - Naming consistency (PEP 8) - Missing type hints and docstrings - Error handling and edge cases - Performance bottlenecks - Code smells and anti-patterns - Import hygiene - Defensive programming issues --> <!-- =========================== HOW IT WORKS (INTERNALLY) =========================== --> <!-- 1. Analyze source code to detect issues and patterns 2. Convert code chunks into embeddings 3. Retrieve relevant context using vector similarity search 4. Inject context into the LLM prompt 5. Generate refactored, ready-to-use code 6. Store learned style preferences for future runs --> <!-- =========================== PROJECT STRUCTURE =========================== -->

waycode/
├── waycode/
│   ├── cli.py              # CLI entry point
│   ├── config.py           # Prompts and configuration
│   ├── refactor_agent.py   # Core refactoring logic
│   ├── rag/                # RAG components
│   │   ├── vector_store.py
│   │   ├── embeddings.py
│   │   ├── memory_manager.py
│   │   └── context_builder.py
│   └── utils/
│       ├── code_analyzer.py
│       └── diff_generator.py
├── examples/
├── requirements.txt
└── setup.py

