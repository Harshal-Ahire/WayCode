import os

class CodeAnalyzer:
    def __init__(self):
        self.language_extensions = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'javascript',
            '.tsx': 'typescript',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.go': 'go',
            '.rs': 'rust',
            '.rb': 'ruby',
            '.php': 'php',
            '.cs': 'csharp',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.scala': 'scala',
            '.html': 'html',
            '.css': 'css',
            '.sql': 'sql',
            '.sh': 'bash',
        }
    
    def detect_language(self, filepath):
        _, ext = os.path.splitext(filepath)
        return self.language_extensions.get(ext.lower(), 'unknown')
    
    def analyze_complexity(self, code):
        # Simple complexity metrics
        lines = code.split('\n')
        non_empty_lines = [l for l in lines if l.strip()]
        
        metrics = {
            'total_lines': len(lines),
            'code_lines': len(non_empty_lines),
            'nesting_level': self._calculate_nesting(code),
            'function_count': code.count('def ') + code.count('function ')
        }
        
        return metrics
    
    def _calculate_nesting(self, code):
        max_nesting = 0
        current_nesting = 0
        
        for char in code:
            if char == '{' or char == '(':
                current_nesting += 1
                max_nesting = max(max_nesting, current_nesting)
            elif char == '}' or char == ')':
                current_nesting = max(0, current_nesting - 1)
        
        return max_nesting