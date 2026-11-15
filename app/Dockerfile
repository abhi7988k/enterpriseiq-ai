
FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt ./requirements.txt

# Install CPU-only PyTorch first
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY Data/ ./Data/

ENV CHROMA_PATH=/app/chroma_db

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
