import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

# System path configuration
HOME = Path.home()
DATA_DIR = HOME / ".waycode" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Storage paths for vector data and history
VECTOR_DB_PATH = str(DATA_DIR / "vector_db")
PROJECT_MEMORY_PATH = str(DATA_DIR / "project_memory.json")
REFACTOR_HISTORY_PATH = str(DATA_DIR / "refactor_history.json")

# Model parameters
EMBEDDING_MODEL = "models/text-embedding-004"
MAX_CONTEXT_TOKENS = 30000
TEMPERATURE = 0.3

# Prompt template for code refactoring logic
REFACTOR_PROMPT = """You are an expert code refactoring assistant with access to the latest programming best practices.

Context from project memory:
{memory_context}

Analyze this code and provide refactoring suggestions:

Language: {language}
Code:
