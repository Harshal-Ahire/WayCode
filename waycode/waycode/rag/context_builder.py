class ContextBuilder:
    def __init__(self, memory_manager):
        self.memory = memory_manager
    
    def build_context(self, code, language):
        context_parts = []
        
        # Get relevant memories
        relevant = self.memory.get_relevant_context(code, language)
        
        # Build context string
        context_parts.append(f"Language: {language}")
        
        # Add project patterns
        if relevant["project_patterns"]:
            context_parts.append("\nProject Patterns:")
            for pattern in relevant["project_patterns"]:
                context_parts.append(f"- {pattern}")
        
        # Add similar code context
        if relevant["similar_code"]["documents"]:
            context_parts.append("\nSimilar code in your project:")
            for i, doc in enumerate(relevant["similar_code"]["documents"][0][:2]):
                context_parts.append(f"Example {i+1}: {doc[:200]}...")
        
        # Add refactoring history insights
        if relevant["refactor_history"]["documents"]:
            context_parts.append("\nPrevious refactoring patterns:")
            for i, doc in enumerate(relevant["refactor_history"]["documents"][0][:2]):
                context_parts.append(f"- {doc[:150]}...")
        
        # Add style preferences
        if relevant["style_patterns"]["documents"]:
            context_parts.append("\nYour coding style preferences:")
            for doc in relevant["style_patterns"]["documents"][0]:
                context_parts.append(f"- {doc}")
        
        return "\n".join(context_parts)