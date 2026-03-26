# WayCode - AI-Powered Code Refactoring Agent

An intelligent CLI code refactoring assistant that learns your coding style using RAG (Retrieval-Augmented Generation) architecture with vector search and LLM integration.

## Features

- **AI-Powered Refactoring** - Uses Google Gemini API with web search for latest best practices.
- **RAG Pipeline** - Vector search with ChromaDB to inject relevant code context into prompts.
- **Learning Memory** - Remembers your coding patterns and preferences across sessions.
- **Multi-Language Support** - Python, JavaScript, TypeScript, Java, Go, and more.
- **Performance Optimized** - Identifies and fixes $O(N)$ to $O(1)$ improvements.
- **Modern Standards** - Enforces PEP 8, type hints, error handling, and clean code principles.

## Tech Stack

- **Backend**: Python, FastAPI
- **AI/ML**: Google Gemini API, RAG Architecture
- **Vector Database**: ChromaDB with semantic embeddings
- **CLI**: Click framework
- **Async Processing**: Concurrent session handling with parallel LLM calls

## Architecture

```text
User Code → Vector Search → Context Retrieval → LLM Prompt → Refactored Code
                ↓
          Memory Storage (learns patterns)

