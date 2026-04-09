import pandas as pd
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="geohealth_app")

# Known bad centroids to reject (country/region-level fallbacks)
CENTROID_BLACKLIST = [
    (22.3511148, 78.6677428),   # India (generic)
    (20.5937,    78.9629),      # India (alternate)
    (28.6138954, 77.2090057),   # Delhi (too broad — keep if you want city-level)
]

CENTROID_TOLERANCE = 0.05       # degrees — tighten to 0.01 for stricter matching


def is_blacklisted(lat, lon):
    """Return True if the coordinate is a known country/region centroid."""
    for blat, blon in CENTROID_BLACKLIST:
        if abs(lat - blat) < CENTROID_TOLERANCE and abs(lon - blon) < CENTROID_TOLERANCE:
            return True
    return False


def geocode_locations(input_path, output_path):
    df = pd.read_csv(input_path)

    latitudes  = []
    longitudes = []
    resolved   = []     # track whether geocoding succeeded meaningfully

    for loc in df["location"]:
        lat, lon, ok = None, None, False
        try:
            location = geolocator.geocode(str(loc))
            if location:
                if is_blacklisted(location.latitude, location.longitude):
                    print(f"  [CENTROID] Rejected '{loc}' → ({location.latitude:.4f}, {location.longitude:.4f})")
                else:
                    lat, lon, ok = location.latitude, location.longitude, True
                    print(f"  [OK]       '{loc}' → ({lat:.4f}, {lon:.4f})")
            else:
                print(f"  [MISS]     '{loc}' — no result")
        except Exception as e:
            print(f"  [ERROR]    '{loc}' — {e}")

        latitudes.append(lat)
        longitudes.append(lon)
        resolved.append(ok)
        time.sleep(1)   # respect Nominatim rate limit

    df["latitude"]  = latitudes
    df["longitude"] = longitudes
    df["geocoded"]  = resolved  # useful for QA — filter on this downstream

    total     = len(df)
    succeeded = sum(resolved)
    print(f"\nGeocode summary: {succeeded}/{total} locations resolved "
          f"({100*succeeded//total}%)")

    df.to_csv(output_path, index=False)
    print(f"Saved → {output_path}")


if __name__ == "__main__":
    geocode_locations(
        "data/processed/extracted_entities.csv",
        "data/processed/geocoded.csv"
    )