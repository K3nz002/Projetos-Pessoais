import feedparser

def get_latest_world_news(rss_url: str, limit: int = 3) -> list:
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:limit]:
        articles.append({
            "title": entry.title,
            "link": entry.link
        })
    return articles