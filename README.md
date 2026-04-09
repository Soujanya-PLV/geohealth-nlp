# 🌍 GeoHealth NLP Pipeline

## 📌 Overview
This project extracts disease outbreaks from news headlines and maps them geographically.

## ⚙️ Workflow
1. Scrape health-related news (Google News RSS)
2. Extract diseases and locations using NLP
3. Convert locations to coordinates
4. Visualize on an interactive map

## 🧠 Tech Used
- spaCy (NLP)
- GeoPy (Geocoding)
- Folium (Mapping)

## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py

## 🌍 Interpretation

This map represents spatial signals of disease outbreaks based on news mentions.

Higher number of mentions in a location may indicate:
- Increased reporting
- Possible outbreak clusters
- Areas requiring further investigation

⚠️ Note: This is not confirmed epidemiological data, but an early signal detection approach.