def fetch_news(query="dengue India"):
    import feedparser
    query = query.replace(" ", "+")
    feed = feedparser.parse(f"https://news.google.com/rss/search?q={query}")
    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "date": entry.published  # 👈 ADD THIS
        })

    return articles


def save_articles(articles, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        for article in articles:
            f.write(article["date"] + " | " + article["title"] + "\n")