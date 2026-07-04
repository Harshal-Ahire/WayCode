# WayCode — RAG-Powered AI Code Intelligence & Refactoring Agent

**An advanced AI agent system for context-aware code understanding, intelligent refactoring, and multi-step reasoning across large-scale repositories.**

WayCode combines **Retrieval-Augmented Generation (RAG)**, **agentic planning**, **persistent memory**, and **tool use** to deliver production-grade code intelligence that overcomes traditional LLM context limitations.

---

## Overview

WayCode is a full-featured AI agent that enables developers to perform complex refactoring and code improvement tasks with deep project-level understanding. It dynamically retrieves relevant code from across the entire repository, maintains persistent memory of project patterns, and executes multi-step reasoning using agentic workflows.

The system is designed with a strong emphasis on **reliability**, **scalability**, **evaluation**, and **practical developer impact**.

---

## Key Features

- **Semantic RAG Pipeline** — High-precision retrieval from large codebases using vector embeddings
- **Multi-File Reasoning** — Understands cross-file dependencies and architectural context
- **Agentic Planning** — Breaks down complex tasks into structured, executable steps using LangGraph
- **Persistent Memory** — Stores and reuses project-specific patterns, conventions, and history
- **Tool Use & Orchestration** — Integrates multiple tools for code analysis and transformation
- **Evaluation Framework** — Built-in benchmarking for retrieval quality, reasoning accuracy, and output reliability
- **Production Backend** — Scalable FastAPI service with async support and comprehensive logging

---

## Architecture

```mermaid
graph TD
    A[User Query / File] --> B[Code Indexing & Chunking]
    B --> C[ChromaDB Vector Store]
    C --> D[Semantic Retrieval Engine]
    D --> E[Context Assembler]
    E --> F[Agent Planner LangGraph]
    F --> G[LLM Reasoning Gemini + Claude Code]
    G --> H[Code Validator & Safety Layer]
    H --> I[Final Refactored Output]
    F <--> J[Persistent Memory System]
    D <--> J


    Core Components

Indexing Engine: Intelligent chunking at function/class level
Retrieval System: Cosine similarity-based ranking with dynamic context injection
Agent Orchestrator: LangGraph-based multi-step planning and tool calling
Memory Layer: Persistent storage of project knowledge and refactoring history
Evaluation Module: Automated assessment of agent performance and failure modes
API Layer: Production-ready FastAPI with observability


Tech Stack

Language: Python 3.11+
AI Frameworks: LangChain, LangGraph, Claude Code
LLM: Google Gemini
Vector Database: ChromaDB
Backend: FastAPI (Async)
Deployment: Docker-ready
CLI: Click


Engineering Highlights

Advanced semantic chunking strategy to preserve code semantics
Dynamic context injection to handle repositories exceeding LLM token limits
Robust error handling, retry mechanisms, and structured logging
Persistent memory system that learns and reuses project conventions
Comprehensive evaluation pipelines for continuous improvement


Repository Structure
textwaycode/
├── core/                 # Core RAG engine and utilities
├── retrieval/            # Vector search and ranking logic
├── memory/               # Persistent memory management
├── agent/                # LangGraph agent workflows and planning
├── api/                  # FastAPI application and routes
├── evaluation/           # Benchmarking and quality assessment
├── cli/                  # Command-line interface
├── utils/                # Prompt engineering, validation & safety
└── config/               # Configuration management

Usage
1. Index a Codebase
Bashpython -m waycode.cli index ./my-project --recursive
2. Refactor a File
Bashpython -m waycode.cli refactor src/module.py --task "optimize performance and improve readability"
3. Start API Server
Bashuvicorn waycode.api.main:app --reload

Future Enhancements

Multi-agent collaboration system
Advanced self-correction and verification loops
IDE integration (VS Code extension)
Support for additional LLMs and embedding models
Expanded evaluation harnesses and benchmarking suite
