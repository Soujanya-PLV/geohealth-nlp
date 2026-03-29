import feedparser

def fetch_news(query="dengue India"):
    url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}"
    
    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "link": entry.link
        })

    return articles


def save_articles(articles, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        for article in articles:
            f.write(article["title"] + "\n")


if __name__ == "__main__":
    articles = fetch_news("dengue India")
    save_articles(articles, r"D:/Desktop/Post MS - Projects/Geohealth projects/geohealth-nlp/data/raw/sample_articles.txt")

    print(f"Saved {len(articles)} articles!")