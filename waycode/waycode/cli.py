import click
import os
import sys
from pathlib import Path

# Add the current directory to sys.path so imports work on Render/GitHub
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from refactor_agent import RefactorAgent
from utils.code_analyzer import CodeAnalyzer
from rag.memory_manager import MemoryManager

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """ WayCode - AI-Powered Code Refactoring Assistant"""
    pass

@cli.command()
@click.argument('filepath', type=click.Path(exists=True))
@click.option('--output', '-o', help='Output file path')
@click.option('--show-diff/--no-diff', default=True, help='Show diff comparison')
def refactor(filepath, output, show_diff):
    """🔧 Refactor a code file with AI suggestions."""
    try:
        click.echo(click.style("\n WayCode AI Refactor", fg='cyan', bold=True))
        
        agent = RefactorAgent()
        analyzer = CodeAnalyzer()
        
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        language = analyzer.detect_language(filepath)
        refactored = agent.refactor_code(code, language, filepath)
        
        if refactored:
            if not output:
                output = f"./output/{os.path.basename(filepath)}"
            
            os.makedirs(os.path.dirname(output) or '.', exist_ok=True)
            with open(output, 'w', encoding='utf-8') as f:
                f.write(refactored)
            
            click.echo(click.style(f" Saved to: {output}", fg='green'))
        else:
            click.echo(click.style(" Refactoring failed", fg='red'))
            sys.exit(1)
            
    except Exception as e:
        click.echo(click.style(f" Error: {str(e)}", fg='red'))
        sys.exit(1)

@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--recursive', '-r', is_flag=True, help='Index all files')
def index(path, recursive):
    """📚 Index files to learn your coding patterns."""
    try:
        agent = RefactorAgent()
        path_obj = Path(path)
        files_indexed = 0
        
        pattern = '**/*' if recursive else '*'
        for file_path in path_obj.glob(pattern) if path_obj.is_dir() else [path_obj]:
            if file_path.is_file() and file_path.suffix in ['.py', '.js', '.ts']:
                agent.analyze_project_file(str(file_path))
                files_indexed += 1
                click.echo(f"  ✓ Indexed: {file_path.name}")
        
        click.echo(click.style(f"\n Total Indexed: {files_indexed}", fg='green'))
    except Exception as e:
        click.echo(click.style(f" Error: {str(e)}", fg='red'))
        sys.exit(1)

if __name__ == '__main__':
    cli()