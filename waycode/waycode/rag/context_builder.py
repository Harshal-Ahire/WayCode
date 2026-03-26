class ContextBuilder:
    def __init__(self, memory_manager):
        # Initialize with a memory manager for context retrieval
        self.memory = memory_manager
    
    def build_context(self, code, language):
        # Assemble string of relevant project context for the AI prompt
        context_parts = []
        
        # Retrieve cross-referenced memories from vector store
        relevant = self.memory.get_relevant_context(code, language)
        
        context_parts.append(f"Language: {language}")
        
        # Include high-level project patterns
        if relevant["project_patterns"]:
            context_parts.append("\nProject Patterns:")
            for pattern in relevant["project_patterns"]:
                context_parts.append(f"- {pattern}")
        
        # Include similar code snippets from the codebase
        if relevant["similar_code"]["documents"]:
            context_parts.append("\nSimilar code in your project:")
            for i, doc in enumerate(relevant["similar_code"]["documents"][0][:2]):
                context_parts.append(f"Example {i+1}: {doc[:200]}...")
        
        # Include insights from past refactoring operations
        if relevant["refactor_history"]["documents"]:
            context_parts.append("\nPrevious refactoring patterns:")
            for i, doc in enumerate(relevant["refactor_history"]["documents"][0][:2]):
                context_parts.append(f"- {doc[:150]}...")
        
        # Include specific detected coding style preferences
        if relevant["style_patterns"]["documents"]:
            context_parts.append("\nYour coding style preferences:")
            for doc in relevant["style_patterns"]["documents"][0]:
                context_parts.append(f"- {doc}")
        
        return "\n".join(context_parts)
