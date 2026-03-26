import chromadb
from waycode.config import VECTOR_DB_PATH
import os

class VectorStore:
    def __init__(self):
        # Create persistent storage directory if missing
        if not os.path.exists(VECTOR_DB_PATH):
            os.makedirs(VECTOR_DB_PATH, exist_ok=True)
        
        self.client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
        
        # Initialize specialized memory collections
        self.code_collection = self._get_or_create_collection("code_patterns")
        self.refactor_collection = self._get_or_create_collection("refactor_history")
        self.style_collection = self._get_or_create_collection("style_preferences")
    
    def _get_or_create_collection(self, name):
        # Helper to retrieve or initialize a ChromaDB collection
        try:
            return self.client.get_collection(name)
        except:
            return self.client.create_collection(
                name=name,
                metadata={"hnsw:space": "cosine"}
            )
    
    def add_code_pattern(self, code, metadata):
        # Index raw code patterns with metadata
        self.code_collection.add(
            documents=[code],
            metadatas=[metadata],
            ids=[f"code_{metadata.get('filename', 'unknown')}_{hash(code)}"]
        )
    
    def add_refactoring(self, original, refactored, metadata):
        # Store transformation history for future learning
        doc = f"Original:\n{original}\n\nRefactored:\n{refactored}"
        self.refactor_collection.add(
            documents=[doc],
            metadatas=[metadata],
            ids=[f"refactor_{hash(original)}"]
        )
    
    def add_style_preference(self, pattern, metadata):
        # Index specific naming or architectural style preferences
        self.style_collection.add(
            documents=[pattern],
            metadatas=[metadata],
            ids=[f"style_{hash(pattern)}"]
        )
    
    def search_similar_code(self, query, n_results=3):
        # Query existing codebase patterns
        return self.code_collection.query(
            query_texts=[query],
            n_results=n_results
        )
    
    def search_refactor_history(self, query, n_results=3):
        # Query past refactoring transformations
        return self.refactor_collection.query(
            query_texts=[query],
            n_results=n_results
        )
    
    def search_style_patterns(self, query, n_results=3):
        # Query style conventions for consistency
        return self.style_collection.query(
            query_texts=[query],
            n_results=n_results
        )
    
    def get_all_styles(self):
        # Retrieve all stored style preferences
        try:
            return self.style_collection.get()
        except:
            return None
