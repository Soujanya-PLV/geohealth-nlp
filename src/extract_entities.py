import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

# Simple disease list (can expand later)
DISEASES = ["dengue", "malaria", "cholera", "diarrhea"]

def extract_entities(text):
    doc = nlp(text)
    
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    
    found_diseases = [d for d in DISEASES if d in text.lower()]
    
    return found_diseases, locations


def process_file(input_path, output_path):
    results = []

    with open(input_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        diseases, locations = extract_entities(line)

        for d in diseases:
            for loc in locations:
                results.append({
                    "text": line.strip(),
                    "disease": d,
                    "location": loc
                })

    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print("Entities extracted and saved!")


if __name__ == "__main__":
    process_file(
        "data/raw/sample_articles.txt",
        "data/processed/extracted_entities.csv"
    )