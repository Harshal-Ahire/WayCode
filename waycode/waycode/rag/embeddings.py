from google import genai
from waycode.config import GEMINI_API_KEY, EMBEDDING_MODEL

class EmbeddingGenerator:
    def __init__(self):
        # Initialize the GenAI client with project configuration
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = EMBEDDING_MODEL
    
    def generate_embedding(self, text):
        # Convert text content into vector embeddings for indexing
        result = self.client.models.embed_content(
            model=self.model,
            content=text
        )
        return result.embeddings[0].values
    
    def generate_query_embedding(self, query):
        # Convert search queries into vector embeddings for retrieval
        result = self.client.models.embed_content(
            model=self.model,
            content=query
        )
        return result.embeddings[0].values
