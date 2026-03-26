import json
import os
from datetime import datetime
from waycode.rag.vector_store import VectorStore
from waycode.config import PROJECT_MEMORY_PATH, REFACTOR_HISTORY_PATH

class MemoryManager:
    def __init__(self):
        # Initialize storage engines and load persistent data
        self.vector_store = VectorStore()
        self.project_memory = self._load_project_memory()
        self.refactor_history = self._load_refactor_history()
    
    def _load_project_memory(self):
        # Load project-wide patterns and styles from JSON
        if os.path.exists(PROJECT_MEMORY_PATH):
            with open(PROJECT_MEMORY_PATH, 'r') as f:
                return json.load(f)
        return {
            "style_preferences": {},
            "common_patterns": [],
            "dependencies": [],
            "architecture": {}
        }
    
    def _load_refactor_history(self):
        # Load transformation history logs
        if os.path.exists(REFACTOR_HISTORY_PATH):
            with open(REFACTOR_HISTORY_PATH, 'r') as f:
                return json.load(f)
        return []
    
    def _save_project_memory(self):
        # Persist project patterns to disk
        os.makedirs(os.path.dirname(PROJECT_MEMORY_PATH), exist_ok=True)
        with open(PROJECT_MEMORY_PATH, 'w') as f:
            json.dump(self.project_memory, f, indent=2)
    
    def _save_refactor_history(self):
        # Persist refactoring logs to disk
        os.makedirs(os.path.dirname(REFACTOR_HISTORY_PATH), exist_ok=True)
        with open(REFACTOR_HISTORY_PATH, 'w') as f:
            json.dump(self.refactor_history, f, indent=2)
    
    def index_file(self, filepath, code, language):
        # Add file content to vector search and extract coding patterns
        metadata = {
            "filename": filepath,
            "language": language,
            "indexed_at": datetime.now().isoformat()
        }
        
        self.vector_store.add_code_pattern(code, metadata)
        self._extract_patterns(code, language)
    
    def store_refactoring(self, original, refactored, language, filename, changes):
        # Log successful refactors to vector store and history file
        metadata = {
            "language": language,
            "filename": filename,
            "timestamp": datetime.now().isoformat(),
            "changes": changes
        }
        
        self.vector_store.add_refactoring(original, refactored, metadata)
        
        self.refactor_history.append({
            "filename": filename,
            "language": language,
            "timestamp": metadata["timestamp"],
            "changes_summary": changes[:200]
        })
        
        self._save_refactor_history()
    
    def _extract_patterns(self, code, language):
        # Analyze code for preferred syntax and architectural patterns
        patterns = []
        
        # Detect concurrency preferences
        if 'async' in code and 'await' in code:
            patterns.append("prefers_async_await")
        
        # Detect JS/TS specific component styles
        if language in ('javascript', 'typescript'):
            if 'const ' in code and '=>' in code:
                patterns.append("prefers_functional_components")
            if 'class ' in code and 'extends' in code:
                patterns.append("uses_class_components")
            if 'const ' in code or 'let ' in code:
                patterns.append("modern_js_syntax")
        
        # Update project memory and vector style store
        for pattern in patterns:
            if pattern not in self.project_memory["common_patterns"]:
                self.project_memory["common_patterns"].append(pattern)
                self.vector_store.add_style_preference(
                    pattern,
                    {"language": language, "type": "syntax_preference"}
                )
        
        self._save_project_memory()
    
    def get_relevant_context(self, code, language, n_results=3):
        # Retrieve cross-referenced context for RAG-based refactoring
        similar_code = self.vector_store.search_similar_code(code, n_results)
        similar_refactors = self.vector_store.search_refactor_history(code, n_results)
        styles = self.vector_store.search_style_patterns(code, n_results)
        
        return {
            "similar_code": similar_code,
            "refactor_history": similar_refactors,
            "style_patterns": styles,
            "project_patterns": self.project_memory["common_patterns"]
        }
