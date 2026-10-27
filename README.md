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


AST Chunking & Retrieval Pipeline
Selective File Detection — Scans target repos and filters out untouched files to re-index only changed code modules.

AST Syntax Tree Parsing — Parses code via Python Abstract Syntax Trees (AST), extracting whole function blocks, docstrings, and class structures instead of arbitrary text splits.

Vector Embedding & Indexing — Generates dense vector representations stored in ChromaDB alongside rich metadata (function name, start/end lines, dependencies).

Semantic Retrieval & MCP Tool Serving — Exposes /search and /query endpoints alongside Model Context Protocol (MCP) schemas for autonomous agent integration.

MCP Integration
WayCode implements standard Model Context Protocol (MCP) tool schemas. Any MCP-compatible LLM agent can dynamically inspect the repository index:
