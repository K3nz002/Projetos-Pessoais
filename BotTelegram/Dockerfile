# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Evita que o Python bufferize stdout/stderr — logs aparecem em tempo real no Docker
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Instala dependências separado do código para aproveitar cache de camadas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte
COPY . .

# Diretório de dados persistentes (montado como volume)
RUN mkdir -p /app/data

VOLUME ["/app/data"]

CMD ["python", "main.py"]
