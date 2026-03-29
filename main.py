from src.scrape_news import fetch_news, save_articles
from src.extract_entities import process_file
from src.geocode import geocode_locations
from src.visualize import create_map

# Step 0: Fetch news
articles = fetch_news("dengue India")
save_articles(articles, "data/raw/sample_articles.txt")

# Step 1: Extract entities
process_file(
    "data/raw/sample_articles.txt",
    "data/processed/extracted_entities.csv"
)

# Step 2: Geocode
geocode_locations(
    "data/processed/extracted_entities.csv",
    "data/processed/geocoded.csv"
)

# Step 3: Create map
create_map(
    "data/processed/geocoded.csv",
    "outputs/map.html"
)

print("Pipeline completed successfully!")