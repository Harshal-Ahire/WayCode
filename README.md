<div align="center">

# 🧭 WayCode — Code Intelligence Platform

**A backend service that indexes and understands large codebases — enabling fast semantic search and AI-assisted code generation across repositories.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_Workflows-1C3C3C)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-FF6F00)](https://www.trychroma.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[**GitHub**](#) · [**Report Bug**](#) · [**Request Feature**](#)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Key Capabilities](#key-capabilities)
- [System Architecture](#system-architecture)
- [Indexing Pipeline](#indexing-pipeline)
- [Retrieval Pipeline](#retrieval-pipeline)
- [Engineering Highlights](#engineering-highlights)
- [Performance Impact](#performance-impact)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview

Understanding a large, multi-language codebase is one of the hardest problems in developer tooling — plain-text search misses structural context, and re-indexing an entire repo on every change doesn't scale.

**WayCode** is a backend service that parses repositories at the **AST (Abstract Syntax Tree) level** across Python, JavaScript, and TypeScript, builds a searchable index of code structure and semantics, and keeps that index fresh through **incremental updates** — avoiding full repository reprocessing on every change.

On top of that index sits a modular retrieval pipeline that powers repository search and code generation tools, built for integration into AI coding agents and developer workflows.

---

## Key Capabilities

| Capability | Description |
|---|---|
| 🌳 **Multi-Language AST Parsing** | Parses and indexes Python, JavaScript, and TypeScript repositories at the syntax-tree level |
| ⚡ **Incremental Indexing** | Re-indexes only changed files/functions instead of the full repo, cutting reprocessing time by 70% |
| 🔍 **Modular Retrieval Pipeline** | ChromaDB-backed vector search with metadata filtering for precise, context-aware code retrieval |
| 🛠️ **Integrated Code Tools** | Tooling for repository search and code generation, designed for agentic workflows |
| 🧵 **Asynchronous Indexing Workers** | Background workers process large repositories without blocking API requests |
| 🐳 **Containerized & CI-Tested** | Dockerized with Docker Compose; GitHub Actions CI runs integration tests on every change |

---

## System Architecture

```
┌────────────┐     ┌───────────────┐     ┌────────────────┐     ┌──────────────┐     ┌────────────────┐
│ Repository │ ──▶ │ AST Parsing   │ ──▶ │ Incremental    │ ──▶ │ ChromaDB     │ ──▶ │ Search / Code   │
│ (ingest)   │     │ (Py/JS/TS)    │     │ Index Updates  │     │ Vector Store │     │ Generation Tools│
└────────────┘     └───────────────┘     └────────────────┘     └──────────────┘     └────────────────┘
```

Indexing and retrieval are decoupled: async workers handle the (potentially heavy) parsing and embedding work, while the FastAPI layer serves fast, low-latency queries against the already-built index.

---

## Indexing Pipeline

1. **Repository Ingestion** — clones/reads the target repo and identifies changed files since the last index run.
2. **AST Parsing** — parses Python, JavaScript, and TypeScript source into abstract syntax trees to extract structural and semantic units (functions, classes, imports).
3. **Incremental Update** — only re-processes and re-embeds units affected by the change, rather than the entire repository — the core optimization behind the 70% reprocessing time reduction.
4. **Async Worker Execution** — indexing runs on background workers so it never blocks incoming API requests.

---

## Retrieval Pipeline

- **Vector Storage** — code embeddings are stored in **ChromaDB** for fast approximate nearest-neighbor search.
- **Metadata Filtering** — queries can be scoped by file path, language, symbol type, or other metadata alongside semantic similarity.
- **Tool Integration** — retrieval is exposed as a set of composable tools (repository search, code generation) that can be called by downstream agents or applications, built with **LangGraph**.

---

## Engineering Highlights

- **Structural, not just textual, understanding** — AST-level parsing captures code semantics that plain-text or regex search cannot.
- **Efficiency-first indexing** — incremental updates mean the system scales with the size of a *change*, not the size of the *repository*.
- **Non-blocking architecture** — asynchronous workers keep the API responsive even while large repositories are being indexed.
- **Production-grade delivery** — containerized with Docker Compose and validated through GitHub Actions CI with integration tests on every commit.

---

## Performance Impact

- ⚡ **70% reduction** in reprocessing time via incremental indexing
- 🔍 Precise retrieval through combined vector similarity + metadata filtering
- 🧵 Non-blocking indexing under asynchronous workers
- ✅ Continuous validation via automated integration tests in CI

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, FastAPI |
| **Agentic Orchestration** | LangGraph |
| **Vector Store** | ChromaDB |
| **Parsing** | AST-based parsers (Python, JavaScript, TypeScript) |
| **Infrastructure** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions (integration tests) |

---

## Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose

### Installation

```bash
git clone https://github.com/<your-username>/waycode.git
cd waycode

# Build and run with Docker Compose
docker compose up --build
```

The API will be available at `http://localhost:8000`.

### Index a Repository

```bash
curl -X POST "http://localhost:8000/index" \
  -H "Content-Type: application/json" \
  -d '{"repo_path": "/path/to/repo"}'
```

### Query the Index

```bash
curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "function that validates JWT tokens", "language": "python"}'
```

---

## Project Structure

```
waycode/
├── app/
│   ├── main.py                 # FastAPI entry point
│   ├── indexing/
│   │   ├── ast_parser.py        # Multi-language AST parsing
│   │   ├── incremental.py       # Incremental update logic
│   │   └── workers.py           # Async indexing workers
│   ├── retrieval/
│   │   ├── vector_store.py      # ChromaDB integration
│   │   └── tools.py             # Search / code-gen tools (LangGraph)
│   └── api/
│       └── routes.py
├── tests/
│   └── integration/             # CI integration tests
├── docker-compose.yml
├── Dockerfile
└── README.md
```

> Update this tree to match your actual repo layout.

---

## Roadmap

- [ ] Support for additional languages (Go, Rust, Java)
- [ ] Cross-repository code search
- [ ] Web UI for repository exploration
- [ ] Benchmark suite for retrieval quality (precision/recall on code search tasks)

---



If you found this project interesting, consider giving it a ⭐

</div>
