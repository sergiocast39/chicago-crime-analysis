import pandas as pd
import requests
import time


# Constants
BASE_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
LIMIT = 50000
FIELDS = ["fbi_code", "date", "district", "primary_type", "id", "arrest", "ward"]
SELECT_FIELDS = ",".join(FIELDS)
DATE_FILTER = "$where=date between '2010-01-01T00:00:00' and '2019-12-31T23:59:59'"


def fetch_data():
    offset = 0
    all_data = []

    print("Starting data fetch...")

    while True:
        url = (
            f"{BASE_URL}?$select={SELECT_FIELDS}&{DATE_FILTER}&$limit={LIMIT}&$offset={offset}"
        )
        print(f"Fetching records {offset} to {offset + LIMIT}...")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Request failed: {e}")
            break

        batch = response.json()
        if not batch:
            print("✅ No more data to fetch.")
            break

        all_data.extend(batch)
        offset += LIMIT
        time.sleep(0.5)  # Avoid hammering the API

    if not all_data:
        print("⚠️ No data retrieved.")
        return pd.DataFrame()

    df = pd.DataFrame(all_data)

    # Convert 'date' field to datetime
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    print(f"✅ Total rows retrieved: {len(df)}")
    return df