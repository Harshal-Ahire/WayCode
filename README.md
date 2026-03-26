# WayCode — AI-Powered Code Refactoring System

WayCode is an AI-driven developer tool that performs **context-aware, multi-file code refactoring** using a Retrieval-Augmented Generation (RAG) pipeline.

It is designed as an **AI-assisted workflow system**, embedding LLM capabilities into real developer workflows to improve code quality, performance, and maintainability.

---

## Overview

WayCode enables automated refactoring by combining:
- Semantic code retrieval (vector search)  
- Context-aware LLM reasoning  
- Persistent memory of project-specific patterns  

The system operates beyond single-file limitations by dynamically retrieving relevant context across the codebase.

---

## Core Capabilities

- **RAG-Based Refactoring Pipeline**  
  Retrieves semantically relevant code snippets using embeddings and injects them into LLM prompts.

- **Multi-file Context Awareness**  
  Handles cross-file dependencies by dynamically building context from related files.

- **Learning Memory System**  
  Stores and reuses project-specific coding patterns for consistent refactoring.

- **AI-Driven Workflow Integration**  
  Functions as a CLI-based automation tool embedded directly into developer workflows.

- **Performance Optimization Engine**  
  Identifies inefficiencies (e.g., O(N) → O(1)) and improves algorithmic performance.

- **Resilient LLM Interaction**  
  Validates outputs and ensures syntactic correctness and safe transformations.

---

## Architecture

```
User Code → Vector Search → Context Retrieval → LLM Prompt → Refactored Code
                ↓
          Memory Storage
```

---

## Advanced Engineering Details

- **Chunking Strategy**  
  Code is segmented at function/class level for semantically meaningful retrieval.

- **Context Ranking**  
  Uses embedding similarity (cosine distance) to rank relevant snippets.

- **Dynamic Context Injection**  
  Builds prompts using multi-file context to overcome LLM token limitations.

- **Prompt Structuring**  
  Enforces consistent output format and coding standards.

- **Scalable Design**  
  Handles large codebases through retrieval rather than full-context processing.

---

## Engineering Highlights

- **RAG System in Production Workflow**  
  Applies retrieval-based AI reasoning to real developer tasks.

- **AI + Systems Integration**  
  Combines vector databases, LLMs, and CLI workflows into a unified system.

- **Workflow Automation**  
  Automates repetitive developer tasks while preserving code correctness.

---

## Tech Stack

- **Backend**: Python, FastAPI  
- **AI/ML**: Google Gemini API  
- **Vector DB**: ChromaDB  
- **CLI**: Click  
- **Concurrency**: Async processing  

---

## Planned Improvements

- Modular agent architecture for LLM orchestration  
- Dedicated retrieval components (retriever, ranker)  
- Externalized prompt management  
- Test suite for validation and robustness  

---

## Data Storage

- Vector DB: `~/.waycode/data/vector_db/`  
- Memory: `~/.waycode/data/project_memory.json`  
- History: `~/.waycode/data/refactor_history.json`  
