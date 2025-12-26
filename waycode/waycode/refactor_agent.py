import os
import sys
import json
from google import genai
from google.genai import types
from waycode.config import *
from waycode.rag.memory_manager import MemoryManager
from waycode.rag.context_builder import ContextBuilder
from waycode.utils.code_analyzer import CodeAnalyzer
from waycode.utils.diff_generator import DiffGenerator

class RefactorAgent:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.memory = MemoryManager()
        self.context_builder = ContextBuilder(self.memory)
        self.analyzer = CodeAnalyzer()
        self.diff_gen = DiffGenerator()
        
    def refactor_code(self, code, language, filename=None):
        print("Analyzing code...")
        
        # Get relevant context from memory
        context = self.context_builder.build_context(code, language)
        
        # Build prompt with memory context
        prompt = REFACTOR_PROMPT.format(
            memory_context=context,
            language=language,
            code=code
        )
        
        # IMPORTANT: Google Search tool removed to avoid quota 'limit: 0' errors
        print("Generating refactor using AI model...")
        
        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=TEMPERATURE
                # tools=[types.Tool(google_search=types.GoogleSearch())]  <-- REMOVED
            )
        )
        
        result = response.text
        
        # Parse response
        refactored = self._parse_refactored_code(result)
        
        if refactored:
            # Generate diff
            diff = self.diff_gen.generate_diff(code, refactored['code'])
            
            # Store in memory for learning
            self.memory.store_refactoring(
                original=code,
                refactored=refactored['code'],
                language=language,
                filename=filename,
                changes=refactored.get('explanation', '')
            )
            
            print("\nRefactoring complete!")
            print("\n" + "="*60)
            print("EXPLANATION:")
            print("="*60)
            print(refactored.get('explanation', 'No explanation provided'))
            print("\n" + "="*60)
            print("DIFF:")
            print("="*60)
            print(diff)
            print("\n" + "="*60)
            print("REFACTORED CODE:")
            print("="*60)
            print(refactored['code'])
            
            return refactored['code']
        else:
            print("Could not parse refactored code")
            print(result)
            return None
    
    def _parse_refactored_code(self, response):
        # Extract code blocks from markdown
        lines = response.split('\n')
        in_code = False
        code_lines = []
        explanation_lines = []
        current_section = 'explanation'
        
        for line in lines:
            if line.strip().startswith('```'):
                if in_code:
                    in_code = False
                    current_section = 'explanation'
                else:
                    in_code = True
                    current_section = 'code'
                continue
            
            if in_code:
                code_lines.append(line)
            elif current_section == 'explanation':
                explanation_lines.append(line)
        
        if code_lines:
            return {
                'code': '\n'.join(code_lines),
                'explanation': '\n'.join(explanation_lines).strip()
            }
        
        return None
    
    def analyze_project_file(self, filepath):
        print(f"Learning from {filepath}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        language = self.analyzer.detect_language(filepath)
        
        # Store file in vector DB for future context
        self.memory.index_file(filepath, code, language)
        
        print(f"Indexed {filepath}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python refactor_agent.py <file_path>")
        print("   or: python refactor_agent.py --index <file_path>")
        sys.exit(1)
    
    agent = RefactorAgent()
    
    if sys.argv[1] == '--index':
        # Index mode: learn from codebase
        filepath = sys.argv[2]
        agent.analyze_project_file(filepath)
    else:
        # Refactor mode
        filepath = sys.argv[1]
        
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        language = agent.analyzer.detect_language(filepath)
        
        refactored = agent.refactor_code(code, language, filepath)
        
        if refactored:
            # Save refactored code
            output_path = f"./output/{os.path.basename(filepath)}"
            os.makedirs('./output', exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(refactored)
            
            print(f"\nSaved to: {output_path}")

if __name__ == "__main__":
    main()