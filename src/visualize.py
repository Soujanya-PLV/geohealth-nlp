import pandas as pd
import folium
from folium.plugins import HeatMap

def create_map(input_path, output_path):
    df = pd.read_csv(input_path)

    # Drop rows without coordinates
    df = df.dropna(subset=["latitude", "longitude"])

    # Create base map
    m = folium.Map(location=[20, 78], zoom_start=5, tiles="CartoDB positron")
   
    # Prepare heatmap data
    heat_data = df[["latitude", "longitude"]].values.tolist()
    HeatMap(heat_data).add_to(m)

    # 📍 Add clickable markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['disease']} in {row['location']}"
        ).add_to(m)

    m.save(output_path)
    print("Map with heatmap + markers created!")