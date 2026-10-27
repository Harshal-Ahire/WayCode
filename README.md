
<div align="center">

# WayCode — Semantic Code Search Engine & MCP Tool (RAG)

**A high-performance semantic code search RAG platform that indexes production codebases via AST parsing, exposed via FastAPI and Model Context Protocol (MCP) tool schemas for AI coding agents.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-180ms_Latency-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG_Pipeline-1C3C3C)](https://www.langchain.com/)
[![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-8A2BE2)](https://modelcontextprotocol.io/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-FF6F00)](https://www.trychroma.com/)
[![Docker](https://img.shields.io/badge/Docker-VPS_Deployment-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[**GitHub**](https://github.com/Harshal-Ahire/Waycode) · [**Report Bug**](https://github.com/Harshal-Ahire/Waycode/issues) · [**Request Feature**](https://github.com/Harshal-Ahire/Waycode/issues)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Key Capabilities](#key-capabilities)
- [System Architecture](#system-architecture)
- [AST Chunking & Retrieval Pipeline](#ast-chunking--retrieval-pipeline)
- [MCP Integration](#mcp-integration)
- [Engineering Highlights](#engineering-highlights)
- [Performance & Benchmark Impact](#performance--benchmark-impact)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Example Usage](#example-usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview

Traditional code search tools rely on regex or exact keyword matches, missing semantic intent across large repositories. Naive chunking algorithms split code by arbitrary line numbers, slicing functions in half and degrading RAG retrieval quality.

**WayCode** solves this by parsing codebases at the **AST (Abstract Syntax Tree)** level to chunk code strictly along function and class boundaries. Powered by **LangChain**, **FastAPI**, and **ChromaDB**, WayCode enables semantic code search with **180ms median query latency** and exposes its vector search indices dynamically to external LLMs through the **Model Context Protocol (MCP)**.

WayCode features an **incremental indexing engine** that re-indexes only modified files, slashing vector re-indexing runtime by 70%.

---

## Key Capabilities

| Capability | Description |
|---|---|
| **AST-Based Code Chunking** | Splits Python code files by exact syntax trees (functions & classes), boosting top-5 retrieval accuracy from 61% to 79% |
| **Model Context Protocol (MCP)** | Native MCP tool schemas allowing AI agents (Cursor, Claude Code, custom agents) to query code indices dynamically |
| **Incremental Vector Indexing** | Detects modified repository files and re-indexes changed chunks only, cutting background runtime by 70% |
| **Sub-200ms Retrieval** | FastAPI REST endpoints serving semantic code queries at 180ms median latency |
| **ChromaDB Vector Store** | Dense vector embeddings and metadata filtering (file path, symbol name, language) for exact scope control |
| **Containerized Deployment** | Full Docker containerization validated with `pytest` suite and deployed on Linux VPS |

---

## System Architecture

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐     ┌──────────────────┐
│ Target Repo     │ ──▶ │  Python AST      │ ──▶ │ Selective Vector    │ ──▶ │    ChromaDB      │
│ (Source Code)   │     │  Function Parser │     │ Indexing (70% Fast) │     │  Vector Storage  │
└─────────────────┘     └──────────────────┘     └─────────────────────┘     └──────────────────┘
                                                                                      │
                                                                                      ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐     ┌──────────────────┐
│ AI LLM Client / │ ◀── │  MCP Tool Schema │ ◀── │ FastAPI REST Engine │ ◀── │ Semantic Query   │
│ Cursor / Claude │     │  Integration     │     │ (180ms Latency)     │     │ Vector Search    │
└─────────────────┘     └──────────────────┘     └─────────────────────┘     └──────────────────┘
```

---

## AST Chunking & Retrieval Pipeline

1. **Selective File Detection** — Scans target repositories and filters out untouched files to re-index only changed code modules.

2. **AST Syntax Tree Parsing** — Parses code via Python Abstract Syntax Trees (AST), extracting whole function blocks, docstrings, and class structures instead of arbitrary text splits.

3. **Vector Embedding & Indexing** — Generates dense vector representations stored in ChromaDB alongside rich metadata, including function name, start/end lines, and dependencies.

4. **Semantic Retrieval & MCP Tool Serving** — Exposes `/search` and `/query` endpoints alongside Model Context Protocol (MCP) schemas for autonomous agent integration.

---

## MCP Integration

WayCode implements standard Model Context Protocol (MCP) tool schemas. Any MCP-compatible LLM agent can dynamically inspect the repository index.

### Example MCP Tool Schema

```json
{
  "name": "search_codebase",
  "description": "Semantically search the codebase for function implementations and class logic.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Natural language query describing desired functionality"
      },
      "top_k": {
        "type": "integer",
        "default": 5
      }
    },
    "required": ["query"]
  }
}
```

---

## Engineering Highlights

- **Syntactically Aware Context Windows:** AST-boundary parsing ensures LLMs receive full, uninterrupted functions without broken syntax.

- **Selective Delta Indexing:** Incremental processing ensures memory and compute scale with change diffs, not codebase size.

- **Low Latency Pipeline:** Asynchronous FastAPI backend tuned for real-time developer workflows with 180ms median latency.

- **Rigorous Test Validation:** Automated `pytest` suite testing parser robustness, retrieval accuracy, and vector search edge cases.

---

## Performance & Benchmark Impact

| Metric | Result | Description |
|---|---|---|
| **Top-5 Retrieval Accuracy** | 61% → 79% | Improvement evaluated across 30 benchmark queries using AST-boundary chunking |
| **Re-indexing Runtime** | 70% reduction | Achieved through selective modified-file delta processing |
| **Median Query Latency** | 180ms | Semantic endpoint retrieval latency |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language & Core | Python 3.10+ |
| Backend & APIs | FastAPI, Uvicorn |
| RAG & Orchestration | LangChain, Model Context Protocol (MCP) |
| Vector Database | ChromaDB |
| Parsing & Analysis | Python AST (`ast` module) |
| Testing & Quality | pytest |
| Deployment | Docker, Docker Compose, Linux VPS |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Docker
- Docker Compose

### Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/Harshal-Ahire/Waycode.git
cd Waycode

# Build and start the service
docker compose up --build -d
```

The FastAPI service will be running at:

- **API Base URL:** http://localhost:8000
- **Interactive API Documentation:** http://localhost:8000/docs

### Run Local Tests

```bash
# Run the test suite
pytest tests/ -v
```

---

## Example Usage

### 1. Index a Repository

```bash
curl -X POST "http://localhost:8000/api/v1/index" \
  -H "Content-Type: application/json" \
  -d '{
    "repo_path": "./sample_repo",
    "incremental": true
  }'
```

### 2. Perform Semantic Code Search

```bash
curl -X POST "http://localhost:8000/api/v1/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "function that parses AST syntax trees and extracts function definitions",
    "top_k": 5
  }'
```

---

## Project Structure

```text
Waycode/
├── app/
│   ├── main.py                 # FastAPI application & lifespan setup
│   ├── api/
│   │   └── routes.py           # REST endpoints (/search, /index, /mcp)
│   ├── indexing/
│   │   ├── ast_parser.py       # Python AST syntax tree function extractor
│   │   └── incremental.py      # Delta modified-file index manager
│   ├── retrieval/
│   │   ├── vector_store.py     # ChromaDB vector collection management
│   │   └── mcp_tools.py        # Model Context Protocol schema bindings
│   └── config.py               # Environment configuration
├── tests/
│   ├── test_ast_parser.py      # AST chunking tests
│   └── test_retrieval.py       # Benchmark evaluation tests
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Roadmap

-Expand AST-based parsing support to additional programming languages.
-Improve retrieval ranking and evaluation across larger codebases.
- Enhance MCP integration for more AI coding agents.
- Add further optimizations for incremental indexing and vector search.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
