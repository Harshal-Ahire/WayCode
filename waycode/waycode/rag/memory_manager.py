import json
import os
from datetime import datetime
from waycode.rag.vector_store import VectorStore
from waycode.config import PROJECT_MEMORY_PATH, REFACTOR_HISTORY_PATH

class MemoryManager:
    def __init__(self):
        self.vector_store = VectorStore()
        self.project_memory = self._load_project_memory()
        self.refactor_history = self._load_refactor_history()
    
    def _load_project_memory(self):
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
        if os.path.exists(REFACTOR_HISTORY_PATH):
            with open(REFACTOR_HISTORY_PATH, 'r') as f:
                return json.load(f)
        return []
    
    def _save_project_memory(self):
        os.makedirs(os.path.dirname(PROJECT_MEMORY_PATH), exist_ok=True)
        with open(PROJECT_MEMORY_PATH, 'w') as f:
            json.dump(self.project_memory, f, indent=2)
    
    def _save_refactor_history(self):
        os.makedirs(os.path.dirname(REFACTOR_HISTORY_PATH), exist_ok=True)
        with open(REFACTOR_HISTORY_PATH, 'w') as f:
            json.dump(self.refactor_history, f, indent=2)
    
    def index_file(self, filepath, code, language):
        metadata = {
            "filename": filepath,
            "language": language,
            "indexed_at": datetime.now().isoformat()
        }
        
        self.vector_store.add_code_pattern(code, metadata)
        
        # Extract and store patterns
        self._extract_patterns(code, language)
    
    def store_refactoring(self, original, refactored, language, filename, changes):
        metadata = {
            "language": language,
            "filename": filename,
            "timestamp": datetime.now().isoformat(),
            "changes": changes
        }
        
        self.vector_store.add_refactoring(original, refactored, metadata)
        
        # Add to history
        self.refactor_history.append({
            "filename": filename,
            "language": language,
            "timestamp": metadata["timestamp"],
            "changes_summary": changes[:200]
        })
        
        self._save_refactor_history()
    
    def _extract_patterns(self, code, language):
        # Simple pattern extraction
        patterns = []
        
        # Check for async/await
        if 'async' in code and 'await' in code:
            patterns.append("prefers_async_await")
        
        # Check for functional vs class components (React)
        if language == 'javascript' or language == 'typescript':
            if 'const ' in code and '=>' in code:
                patterns.append("prefers_functional_components")
            if 'class ' in code and 'extends' in code:
                patterns.append("uses_class_components")
        
        # Check for const/let vs var
        if 'const ' in code or 'let ' in code:
            patterns.append("modern_js_syntax")
        
        # Store patterns
        for pattern in patterns:
            if pattern not in self.project_memory["common_patterns"]:
                self.project_memory["common_patterns"].append(pattern)
                self.vector_store.add_style_preference(
                    pattern,
                    {"language": language, "type": "syntax_preference"}
                )
        
        self._save_project_memory()
    
    def get_relevant_context(self, code, language, n_results=3):
        # Search for similar code patterns
        similar_code = self.vector_store.search_similar_code(code, n_results)
        
        # Search refactor history
        similar_refactors = self.vector_store.search_refactor_history(code, n_results)
        
        # Get style preferences
        styles = self.vector_store.search_style_patterns(code, n_results)
        
        return {
            "similar_code": similar_code,
            "refactor_history": similar_refactors,
            "style_patterns": styles,
            "project_patterns": self.project_memory["common_patterns"]
        }