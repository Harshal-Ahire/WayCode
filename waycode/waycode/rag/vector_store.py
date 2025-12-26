import chromadb
from waycode.config import VECTOR_DB_PATH
import os

class VectorStore:
    def __init__(self):
        # Fix: Only create directory if it doesn't exist
        if not os.path.exists(VECTOR_DB_PATH):
            os.makedirs(VECTOR_DB_PATH, exist_ok=True)
        
        self.client = chromadb.PersistentClient(
            path=VECTOR_DB_PATH
        )
        
        # Collections for different types of memory
        self.code_collection = self._get_or_create_collection("code_patterns")
        self.refactor_collection = self._get_or_create_collection("refactor_history")
        self.style_collection = self._get_or_create_collection("style_preferences")
    
    def _get_or_create_collection(self, name):
        try:
            return self.client.get_collection(name)
        except:
            return self.client.create_collection(
                name=name,
                metadata={"hnsw:space": "cosine"}
            )
    
    def add_code_pattern(self, code, metadata):
        self.code_collection.add(
            documents=[code],
            metadatas=[metadata],
            ids=[f"code_{metadata.get('filename', 'unknown')}_{hash(code)}"]
        )
    
    def add_refactoring(self, original, refactored, metadata):
        doc = f"Original:\n{original}\n\nRefactored:\n{refactored}"
        self.refactor_collection.add(
            documents=[doc],
            metadatas=[metadata],
            ids=[f"refactor_{hash(original)}"]
        )
    
    def add_style_preference(self, pattern, metadata):
        self.style_collection.add(
            documents=[pattern],
            metadatas=[metadata],
            ids=[f"style_{hash(pattern)}"]
        )
    
    def search_similar_code(self, query, n_results=3):
        results = self.code_collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
    
    def search_refactor_history(self, query, n_results=3):
        results = self.refactor_collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
    
    def search_style_patterns(self, query, n_results=3):
        results = self.style_collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
    
    def get_all_styles(self):
        try:
            results = self.style_collection.get()
            return results
        except:
            return None