import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

DISEASES = ["dengue", "malaria", "cholera", "diarrhea"]

def extract_entities(text):
    doc = nlp(text)

    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    diseases = [d for d in DISEASES if d in text.lower()]

    return diseases, locations


def process_file(input_path, output_path):
    results = []

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        # Handle both formats (with or without date)
        if "|" in line:
            _, text = line.split("|", 1)
        else:
            text = line

        diseases, locations = extract_entities(text)

        for d in diseases:
            for loc in locations:
                results.append({
                    "text": text,
                    "disease": d,
                    "location": loc
                })

    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print("Entities extracted!")


if __name__ == "__main__":
    process_file(
        "data/raw/sample_articles.txt",
        "data/processed/extracted_entities.csv"
    )