# Horizon Memory

> The memory layer that understands your data — not just stores it.

Horizon Memory is a Python SDK that unifies **knowledge base management** and **agent context management** into a single, developer-friendly library. It handles 100s–1000s of files, extracts entities and relationships, builds a knowledge graph, and provides research-grade retrieval with auto-generated insights — all with zero external dependencies in dev mode.

---

## What Makes It Different

| Capability | Horizon | Mem0 | Zep | Cognee |
|---|---|---|---|---|
| Document corpus memory (100s–1000s files) | ✅ | ❌ | ❌ | ✅ |
| Agent conversation memory | ✅ | ✅ | ✅ | ⚠️ |
| Auto-insights (topics, trends, gaps) | ✅ | ❌ | ❌ | ❌ |
| Research-grade multi-hop retrieval | ✅ | ❌ | ❌ | ❌ |
| Relationship visualization export | ✅ | ❌ | ❌ | ❌ |
| `pip install` zero-deps dev mode | ✅ | ✅ | ❌ | ✅ |
| Framework-agnostic agent SDK | ✅ | ❌ | ❌ | ❌ |
| CLI + HTTP API + Python SDK | ✅ | ⚠️ | ⚠️ | ✅ |

---

## Project Status

> 🏗️ **Phase 0 — Project Initialization** — Architecture planned, structure laid out. Implementation starting soon.

---

## Quick Start (Coming Soon)

```bash
pip install horizon-memory

# CLI
horizon init
horizon ingest ./my-documents/
horizon ask "What pricing strategy do competitors use?"
horizon insights

# HTTP API
horizon serve
curl http://localhost:8765/health
```
---

## Architecture

Horizon Memory is built in four layers:

```
┌─────────────────────────────────────────  ┐
│           PUBLIC API LAYER                │
│   Python SDK  │  CLI  │  HTTP API         │
├─────────────────────────────────────────  ┤
│           SERVICE LAYER                   │
│   Orchestration, auth, validation         │
├─────────────────────────────────────────  ┤
│          CORE ENGINES                     │
│   Pipeline Orchestrator                   │
│   ingest → chunk → embed → extract        │
│   → link → index → insight                │
├─────────────────────────────────────────  ┤
│        STORAGE ABSTRACTION                │
│   Vector (LanceDB/PGVector)               │
│   Graph (Kuzu/Neo4j)                      │
│   Relational (SQLite/PostgreSQL)          │
│   Blob (LocalFS/S3/Azure)                 │
└─────────────────────────────────────────  ┘
```

---

## Development

```bash
# Clone and install
pip install -e ".[dev,local]"

# Run the API
python -m horizon.api.app

# Run tests
pytest
```

### Project Structure

```
horizon/
├── api/              # FastAPI application
├── cli/              # Typer CLI tool
├── engines/          # Orchestration & pipeline glue
├── ingestion/        # Load, parse, chunk, extract, OCR, normalize
│   ├── loader/       #   File loaders (PDF, MD, CSV, JSON, code, URL)
│   ├── parser/       #   Format-specific text extraction
│   ├── chunking/     #   Fixed, semantic, recursive, AST-aware
│   ├── strategy/     #   Full, incremental, differential ingest
│   ├── ocr/          #   Image & scanned PDF text extraction
│   ├── extraction/   #   Entity & relationship extraction
│   ├── normalizer/   #   Text cleaning & sanitization
│   └── retrieval/    #   Embedding lookups during ingest
│
├── retrieval/        # Multi-strategy search & ranking
│   ├── exact/        #   Keyword, ID, filter lookup
│   ├── fusion/       #   RRF, weighted score combinators
│   ├── lexical/      #   BM25, TF-IDF, full-text
│   ├── graph/        #   Entity-relationship traversal
│   ├── temporal/     #   Time-aware, bi-temporal facts
│   ├── reranking/    #   Cross-encoder, LLM relevance scoring
│   ├── regex/        #   Pattern-based extraction
│   ├── planner/      #   Query decomposition & routing
│   └── vector/       #   Dense, sparse, hybrid embedding
│
├── db/               # Database backends
│   ├── vector/       #   LanceDB, PGVector, Qdrant
│   ├── graph/        #   Kuzu, Neo4j, FalkorDB
│   ├── relational/   #   Relational protocols
│   ├── sqlite/       #   SQLite implementation
│   └── postgres/     #   PostgreSQL implementation
│
├── storage/          # Blob storage (S3, Azure, local FS)
├── adapters/         # External service clients (qdrant, neo4j, opensearch, pgvector)
├── service/          # Orchestration layer
├── llm/              # LLM client abstraction (OpenAI, Anthropic, custom)
├── data_model/       # Document, Chunk, Entity, Relationship, Collection, Session
├── logger/           # Structured logging
├── settings/         # Env vars, config defaults, validation
└── utils/            # Hashing, text, timing
```

---

## Configuration

Horizon Memory is **zero-config by default** — it works out of the box with embedded databases. Scale to production by swapping backends:

```python
from horizon import HorizonConfig, StorageConfig

config = HorizonConfig(
    storage=StorageConfig(
        vector_backend="pgvector",
        graph_backend="neo4j",
        relational_backend="postgres",
    )
)
horizon = HorizonClient(config=config)
```

---

## Core Principles

1. **Local-first by default** — LanceDB + Kuzu + SQLite = zero external deps for dev
2. **Scale when ready** — Swap to PGVector + Neo4j + PostgreSQL via config
3. **Transparent pipelines** — Every stage is inspectable and debuggable
4. **Pythonic DX** — Async-first, type hints everywhere, sensible defaults
5. **Framework-agnostic** — Adapters for OpenAI, LangChain, LlamaIndex, CrewAI
6. **Insight over storage** — Horizon doesn't just store data — it understands it

---

## License

MIT

## Author

Ayush — developer.zang.000@gmail.com
