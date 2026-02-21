# AIDEN Server

AIDEN is the autonomous sales development agent backend. It manages prospect data, conducts automated research, and generates personalized email drafts using LLMs.

## Features

- **Prospect Management**: CRUD operations for sales prospects.
- **Automated Research**: Gathers data from LinkedIn, News, and Tech Stack sources (currently mocked).
- **Email Generation**: Uses Claude 3.5 Sonnet (via Anthropic API) to write personalized cold emails.
- **Async Processing**: Uses Celery and Redis for background task execution.
- **Production Ready**: Includes Gunicorn config, Sentry integration, and structured logging.

## Tech Stack

- **Framework**: FastAPI (Python 3.12)
- **Database**: PostgreSQL (Production) / SQLite (Local Dev)
- **ORM**: SQLAlchemy (Async) + Alembic (Migrations)
- **Task Queue**: Celery + Redis
- **AI/LLM**: Anthropic API (Claude 3.5)

## Setup & Installation

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Poetry (Dependency Manager)

### Local Development (Quick Start)

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd apps/aiden-server
   ```

2. **Install Dependencies**:
   ```bash
   poetry install
   ```

3. **Configure Environment**:
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   *Note: For local dev, `DATABASE_URL` defaults to SQLite to avoid Docker dependency issues.*

4. **Run Migrations**:
   ```bash
   poetry run alembic upgrade head
   ```

5. **Start the Server**:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```
   Access API docs at `http://localhost:8000/api/v1/docs`.

### Docker Development

To run the full stack (Postgres, Redis, Worker, API) in Docker:

1. Update `.env` to use Postgres:
   ```properties
   DATABASE_URL=postgresql+asyncpg://postgres:password@db:5432/aiden
   REDIS_URL=redis://redis:6379/0
   ```

2. Build and Run:
   ```bash
   docker-compose up --build
   ```

## API Documentation

Interactive API documentation (Swagger UI) is available at `/api/v1/docs`.

### Key Endpoints

- `GET /api/v1/prospects/`: List all prospects.
- `POST /api/v1/prospects/`: Create a new prospect.
- `POST /api/v1/prospects/{id}/research`: Trigger background research task.
- `POST /api/v1/prospects/{id}/generate-email`: Trigger email draft generation.
- `GET /api/v1/prospects/{id}/emails`: Get generated drafts.

## Deployment

### Production Settings

- **Server**: Uses Gunicorn with Uvicorn workers (`gunicorn_conf.py`).
- **Logging**: JSON structured logging configured in `app/core/log_config.py`.
- **Error Tracking**: Sentry DSN can be provided via `SENTRY_DSN` env var.

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | DB Connection String | `sqlite+aiosqlite:///./aiden.db` |
| `REDIS_URL` | Redis Connection String | `redis://localhost:6379/0` |
| `ANTHROPIC_API_KEY` | Key for AI generation | `None` |
| `SENTRY_DSN` | Sentry DSN for error tracking | `None` |
| `ENVIRONMENT` | Environment name (local/prod) | `local` |

## Testing

Run unit tests:
```bash
poetry run pytest
```

Lint code:
```bash
poetry run ruff check .
```
