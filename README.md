
```markdown
# WayCode — RAG-Powered AI Code Intelligence Agent

**An intelligent AI agent for context-aware code understanding and multi-step refactoring across large repositories.**

WayCode combines **Retrieval-Augmented Generation (RAG)**, **persistent memory**, and **agentic reasoning** to help developers refactor and improve code with deep project-level understanding.

---

## Overview

WayCode is a production-ready AI agent that overcomes LLM context window limitations by dynamically retrieving relevant code across multiple files and injecting it into reasoning steps.

It enables **long-context reasoning**, **tool use**, and **multi-step planning** for complex code transformation tasks.

---

## Key Features

- **RAG-Based Code Intelligence** — Semantic search over entire codebases for accurate context retrieval
- **Multi-File Reasoning** — Understands cross-file dependencies and project architecture
- **Agentic Planning** — Breaks down complex refactoring tasks into executable steps
- **Persistent Memory** — Remembers project-specific patterns, conventions, and previous refactorings
- **Production Backend** — Built with FastAPI for scalability and reliability

---

## Architecture

```
User Query → Semantic Retrieval (ChromaDB) → Context Assembly → Agent Planning → LLM Reasoning → Safe Code Output
                  ↑
           Persistent Memory
```

---

## Tech Stack

- **Language**: Python
- **AI Frameworks**: LangChain, LangGraph, Claude Code
- **LLM**: Google Gemini
- **Vector Database**: ChromaDB
- **Backend**: FastAPI
- **Deployment**: Docker-ready

---

## What I Built

- Designed and implemented a full **RAG pipeline** for semantic code retrieval
- Developed an **agentic workflow** with planning, tool calling, and iterative reasoning
- Built persistent memory system using ChromaDB to maintain project context
- Created evaluation pipelines to measure retrieval quality and refactoring accuracy
- Exposed functionality through clean, production-ready REST APIs

---

## Repository Structure

```
waycode/
├── core/               # RAG engine and agent logic
├── memory/             # Persistent memory and project context
├── api/                # FastAPI endpoints
├── cli/                # Command-line interface
├── evaluation/         # Agent evaluation and benchmarking
└── utils/              # Prompt engineering and safety checks
```

---

## Planned Enhancements

- Modular multi-agent architecture
- Advanced evaluation harnesses
- Better failure mode detection and self-correction
- Integration with more LLMs and tools

---

**Status**: Actively developed and used for real-world code intelligence tasks.

---

**GitHub**: [Harshal Ahire](https://github.com/Harshal-Ahire)

Feel free to explore the code and run it locally!
```

