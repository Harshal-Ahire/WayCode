import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

# Use user's home directory for data storage
HOME = Path.home()
DATA_DIR = HOME / ".waycode" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

VECTOR_DB_PATH = str(DATA_DIR / "vector_db")
PROJECT_MEMORY_PATH = str(DATA_DIR / "project_memory.json")
REFACTOR_HISTORY_PATH = str(DATA_DIR / "refactor_history.json")

EMBEDDING_MODEL = "models/text-embedding-004"

MAX_CONTEXT_TOKENS = 30000
TEMPERATURE = 0.3

REFACTOR_PROMPT = """You are an expert code refactoring assistant with access to the latest programming best practices.

Context from project memory:
{memory_context}

Analyze this code and provide refactoring suggestions:

Language: {language}
Code:
```
{code}
```

Provide:
1. Issues found (code smells, anti-patterns, performance issues)
2. Refactored code with improvements
3. Brief explanation for each change
4. Confidence level (high/medium/low)

CRITICAL RULES FOR REFACTORED CODE:
- Write CLEAN, MINIMAL code
- Use BRIEF single-line docstrings ONLY for non-obvious functions
- NO multi-line docstrings with Args/Returns/Raises sections
- NO excessive comments
- Let code be self-documenting through clear naming and type hints
- Keep it concise and readable
- Focus on: readability, performance, modern syntax, best practices

Example of preferred style:
```python
def get_user(user_id: int) -> dict | None:
    \"\"\"Retrieves user by ID.\"\"\"
    return self.users.get(user_id)
```
"""

ANALYSIS_PROMPT = """Analyze this codebase file and extract key patterns, conventions, and style preferences.

File: {filename}
Language: {language}
Code:
```
{code}
```

Extract:
- Naming conventions
- Code style patterns
- Preferred patterns (functional vs OOP, async patterns, etc)
- Common imports and dependencies
- Architecture patterns

Return as JSON.
"""

# Safety validation
if not GEMINI_API_KEY:
    print("\nWARNING: GEMINI_API_KEY not found in .env file!")
    print("Please create a .env file with: GEMINI_API_KEY=your_key_here")