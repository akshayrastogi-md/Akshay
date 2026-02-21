FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY pyproject.toml poetry.lock* ./

# Configure poetry to not create virtualenvs
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --without dev

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Make start script executable
RUN chmod +x start.sh

# Start command (using start script)
CMD ["./start.sh"]
