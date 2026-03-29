import pandas as pd
import folium

def create_map(input_path, output_path):
    df = pd.read_csv(input_path)

    m = folium.Map(location=[20, 78], zoom_start=5)

    for _, row in df.iterrows():
        if pd.notnull(row["latitude"]):
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=f"{row['disease']} in {row['location']}"
            ).add_to(m)

    m.save(output_path)
    print("Map saved!")


if __name__ == "__main__":
    create_map(
        "data/processed/geocoded.csv",
        "outputs/map.html"
    )