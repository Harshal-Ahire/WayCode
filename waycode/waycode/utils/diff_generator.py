import difflib

class DiffGenerator:
    def generate_diff(self, original, refactored):
        original_lines = original.splitlines(keepends=True)
        refactored_lines = refactored.splitlines(keepends=True)
        
        diff = difflib.unified_diff(
            original_lines,
            refactored_lines,
            fromfile='original',
            tofile='refactored',
            lineterm=''
        )
        
        return ''.join(diff)
    
    def generate_side_by_side(self, original, refactored):
        original_lines = original.splitlines()
        refactored_lines = refactored.splitlines()
        
        max_len = max(len(original_lines), len(refactored_lines))
        
        result = []
        result.append(f"{'ORIGINAL':<50} | {'REFACTORED':<50}")
        result.append("-" * 103)
        
        for i in range(max_len):
            orig = original_lines[i] if i < len(original_lines) else ''
            refac = refactored_lines[i] if i < len(refactored_lines) else ''
            
            result.append(f"{orig:<50} | {refac:<50}")
        
        return '\n'.join(result)