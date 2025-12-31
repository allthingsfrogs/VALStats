from google.cloud import storage
from pathlib import Path
from dotenv import load_dotenv
import os
import getpass

load_dotenv()
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
BUCKET = os.getenv("GOOGLE_CLOUD_BUCKET")
USER = getpass.getuser()

storage_client = storage.Client(project=PROJECT_ID)

def upload_file(local_path: Path, gcs_object_name: str):
    bucket = storage_client.bucket(BUCKET)
    blob = bucket.blob(gcs_object_name)
    blob.upload_from_filename(str(local_path))

years = [2021, 2022, 2023, 2024, 2025]

for y in years:
    local_csv = Path(f"/Users/{USER}/VALSTATS/data/raw/VCT_Archive/vct_{y}/players_stats/players_stats.csv")
    gcs_object = f"bronze/player_stats/season_year={y}/player_stats.csv"
    upload_file(local_csv, gcs_object)
    print(f"Uploaded {local_csv} to: ", f"gs://{BUCKET}/{gcs_object}")

