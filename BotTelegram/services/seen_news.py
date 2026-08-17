"""
Módulo de deduplicação de notícias.

Persiste os links já enviados em `data/seen_news.json`, com TTL de 3 dias.
Entradas mais antigas que 72 horas são removidas automaticamente a cada ciclo.
"""

import json
import os
from datetime import datetime, timedelta, timezone

# Caminho do arquivo de estado (montado como volume no Docker)
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
SEEN_FILE = os.path.join(DATA_DIR, "seen_news.json")

TTL_DAYS = 3


def _now_iso() -> str:
    """Retorna o timestamp atual em ISO 8601 (UTC)."""
    return datetime.now(timezone.utc).isoformat()


def _is_expired(timestamp_iso: str) -> bool:
    """Retorna True se o timestamp for mais antigo que TTL_DAYS dias."""
    try:
        seen_at = datetime.fromisoformat(timestamp_iso)
        return datetime.now(timezone.utc) - seen_at > timedelta(days=TTL_DAYS)
    except (ValueError, TypeError):
        return True  # entrada malformada: descartar


def load_seen() -> dict[str, dict[str, str]]:
    """
    Carrega o histórico de notícias já enviadas do disco.

    Retorna um dicionário no formato:
        { categoria: { url: timestamp_iso } }

    Links com TTL expirado são removidos automaticamente.
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(SEEN_FILE):
        return {}

    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            raw: dict = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}

    # Limpa entradas expiradas
    cleaned: dict[str, dict[str, str]] = {}
    for category, entries in raw.items():
        active = {
            url: ts
            for url, ts in entries.items()
            if not _is_expired(ts)
        }
        if active:
            cleaned[category] = active

    return cleaned


def save_seen(seen: dict[str, dict[str, str]]) -> None:
    """Persiste o histórico atualizado no disco."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(seen, f, ensure_ascii=False, indent=2)


def filter_new(
    articles: list[dict],
    seen: dict[str, dict[str, str]],
    category: str,
) -> list[dict]:
    """
    Filtra a lista de artigos, retornando apenas os que ainda não foram enviados.

    Após a chamada, `seen[category]` é atualizado com os novos links —
    mas o save no disco só acontece em `save_seen()`, chamado pelo scheduler
    depois que o envio for confirmado.
    """
    category_seen = seen.setdefault(category, {})
    new_articles = []

    for article in articles:
        link = article.get("link", "")
        if link and link not in category_seen:
            new_articles.append(article)
            category_seen[link] = _now_iso()

    return new_articles
