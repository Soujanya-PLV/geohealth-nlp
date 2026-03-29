import pandas as pd
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="geohealth_app")

def geocode_locations(input_path, output_path):
    df = pd.read_csv(input_path)

    latitudes = []
    longitudes = []

    for loc in df["location"]:
        try:
            location = geolocator.geocode(loc)
            if location:
                latitudes.append(location.latitude)
                longitudes.append(location.longitude)
            else:
                latitudes.append(None)
                longitudes.append(None)
        except:
            latitudes.append(None)
            longitudes.append(None)

        time.sleep(1)  # avoid API block

    df["latitude"] = latitudes
    df["longitude"] = longitudes

    df.to_csv(output_path, index=False)
    print("Geocoding complete!")


if __name__ == "__main__":
    geocode_locations(
        "data/processed/extracted_entities.csv",
        "data/processed/geocoded.csv"
    )