# AIDEN Server

**AIDEN** is an autonomous, AI-powered Sales Development Representative (SDR) agent backend. It automates the entire outbound sales workflow: from deep prospect research and hyper-personalized email drafting to managing multi-touch sequences and learning from successful interactions.

---

## 🏗️ Architecture

AIDEN follows an asynchronous, event-driven architecture designed for scalability and resilience.

```mermaid
graph TD
    User[User / Client] -->|API Request| API[FastAPI Server]
    API -->|Read/Write| DB[(PostgreSQL)]
    API -->|Queue Task| Redis[(Redis)]

    subgraph "Worker Nodes"
        Worker[Celery Worker] -->|Consume Task| Redis
        Worker -->|Update Status| DB

        Worker -->|1. Research| ResearchService
        Worker -->|2. Draft| LLMService
        Worker -->|3. Learn| VectorService
    end

    subgraph "External World"
        ResearchService -->|Free| DDG[DuckDuckGo]
        ResearchService -->|Free| Web[Website Scraper]
        ResearchService -->|Paid| Proxycurl[LinkedIn API]
        ResearchService -->|Paid| Apollo[Apollo.io]

        LLMService -->|Generate| Claude[Anthropic Claude 3.5]
    end

    subgraph "Knowledge Base"
        VectorService -->|Store/Retrieve| Milvus[(Milvus Vector DB)]
        LLMService -->|RAG Query| VectorService
    end
```

---

## 🚀 Features

### Phase 1: Core Foundation
*   **Prospect Management**: CRUD operations for prospects with status tracking (`NEW`, `RESEARCHED`, `DRAFTED`).
*   **Async Task Engine**: Robust Celery + Redis setup to handle long-running research jobs.
*   **LLM Integration**: Integration with Anthropic (Claude 3.5) for high-quality email generation.

### Phase 2: Sequences & Integrations
*   **Campaigns & Sequences**: Support for multi-step outreach campaigns (`SequenceStep`).
*   **Real Data Enrichment**: Integration with **Apollo.io** (enrichment) and **Proxycurl** (LinkedIn scraping).
*   **Resilience**: Global exception handling, structured logging, and task retries with backoff.

### Phase 3: Intelligence & Cost Optimization
*   **Waterfall Research Strategy**:
    1.  **Level 1 (Free)**: Searches DuckDuckGo for LinkedIn URLs and Company News. Scrapes company homepage text.
    2.  **Level 2 (Paid Fallback)**: If critical data (like LinkedIn URL) is missing, it falls back to premium APIs (Proxycurl/Apollo) to ensure quality.
*   **Vector Memory (RAG)**:
    *   **Milvus Integration**: Stores successful email drafts as vector embeddings.
    *   **Few-Shot Prompting**: Before writing an email, AIDEN searches Milvus for similar successful examples and feeds them to Claude as context.

---

## 🛠️ Tech Stack

*   **Framework**: FastAPI (Python 3.12)
*   **Database**: PostgreSQL 15 (Async SQLAlchemy + Alembic)
*   **Task Queue**: Celery + Redis
*   **Vector DB**: Milvus (Standalone) + Sentence Transformers (Local Embeddings)
*   **AI/LLM**: Anthropic API (Claude 3.5 Sonnet)
*   **Harvesting**: DuckDuckGo, BeautifulSoup, Proxycurl, Apollo

---

## ⚡ Setup & Installation

### Prerequisites
*   Python 3.12+
*   Docker & Docker Compose
*   Poetry (Dependency Manager)

### Option 1: Local Development (Lightweight)
Suitable for logic testing. Uses SQLite. *Note: Vector DB features will be mocked or unavailable without Docker.*

1.  **Clone & Install**:
    ```bash
    git clone <repo>
    cd apps/aiden-server
    poetry install
    ```

2.  **Configure Environment**:
    ```bash
    cp .env.example .env
    # Edit .env: Ensure DATABASE_URL uses sqlite (default)
    ```

3.  **Run Migrations**:
    ```bash
    poetry run alembic upgrade head
    ```

4.  **Start Services**:
    *   **Redis** (Required): `docker run -d -p 6379:6379 redis:alpine`
    *   **API Server**: `poetry run uvicorn app.main:app --reload`
    *   **Worker**: `poetry run celery -A app.core.celery_app worker --loglevel=info`

### Option 2: Full Production Stack (Docker)
Runs everything (API, Worker, Postgres, Redis, Milvus) in containers. **Required for full RAG/Vector capabilities.**

1.  **Update Config**:
    Edit `.env` to point to docker service names:
    ```properties
    DATABASE_URL=postgresql+asyncpg://postgres:password@db:5432/aiden
    REDIS_URL=redis://redis:6379/0
    MILVUS_HOST=milvus-standalone
    ```

2.  **Build & Run**:
    ```bash
    docker-compose up --build -d
    ```
    *   API: `http://localhost:8000`
    *   Docs: `http://localhost:8000/api/v1/docs`
    *   Milvus: `localhost:19530`

---

## ⚙️ Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| **Core** | | |
| `DATABASE_URL` | DB Connection String | `sqlite+aiosqlite:///./aiden.db` |
| `REDIS_URL` | Redis Connection | `redis://localhost:6379/0` |
| `ENVIRONMENT` | Environment (local/prod) | `local` |
| `SENTRY_DSN` | Sentry Error Tracking | `None` |
| **AI & Vector** | | |
| `ANTHROPIC_API_KEY` | Claude 3.5 API Key | `None` |
| `MILVUS_HOST` | Milvus Host | `localhost` |
| `MILVUS_PORT` | Milvus Port | `19530` |
| **Data Harvesting** | | |
| `APOLLO_API_KEY` | Apollo.io Key | `None` |
| `PROXYCURL_API_KEY` | Proxycurl (LinkedIn) Key | `None` |
| `NEWS_API_KEY` | Google News API Key | `None` |

---

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
poetry install --with dev

# Run tests
poetry run pytest
```

---

## 🚀 Deployment

The project includes a production-ready `Dockerfile` and `start.sh` script.
*   **Web Server**: Uses `Gunicorn` with Uvicorn workers (`gunicorn_conf.py`).
*   **Migrations**: Automatically runs `alembic upgrade head` on container start.
*   **Logging**: structured JSON logging configured in `app/core/log_config.py`.
