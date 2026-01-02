from google.cloud import storage
from pathlib import Path
from dotenv import load_dotenv
import getpass
import pandas as pd
import numpy
import os

load_dotenv()
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
BUCKET = os.getenv("GOOGLE_CLOUD_BUCKET")
USER = getpass.getuser()

#read 2025 player stats into df, profile data
df = pd.read_csv(f"/Users/{USER}/VALSTATS/data/raw/VCT_Archive/vct_2025/players_stats/players_stats.csv")

#df.info()
#print(df.describe())
#print(df.head(10))

#convert to catagorical columns for Tournament, Stage, Match Type, Players, Teams; show memory savings
#Tournament Col
print("Tournament Col Categorical Conversion Memory usage")
print("Before: ", df["Tournament"].memory_usage(deep=True))
df["Tournament"] = df["Tournament"].astype("category")
print("After: ", df["Tournament"].memory_usage(deep=True), "\n")

#Stage Col
print("Stage Col Categorical Conversion Memory usage")
print("Before: ", df["Stage"].memory_usage(deep=True))
df["Stage"] = df["Stage"].astype("category")
print("After: ", df["Stage"].memory_usage(deep=True), "\n")

#Match Type Col
print("Match Type Col Categorical Conversion Memory usage")
print("Before: ", df["Match Type"].memory_usage(deep=True))
df["Match Type"] = df["Match Type"].astype("category")
print("After: ", df["Match Type"].memory_usage(deep=True), "\n")


#Players Col
print("Players Col Categorical Conversion Memory usage")
print("Before: ", df["Players"].memory_usage(deep=True))
df["Players"] = df["Players"].astype("category")
print("After: ", df["Players"].memory_usage(deep=True), "\n")

#Teams Col
print("Teams Col Categorical Conversion Memory usage")
print("Before: ", df["Teams"].memory_usage(deep=True))
df["Teams"] = df["Teams"].astype("category")
print("After: ", df["Teams"].memory_usage(deep=True), "\n")


#see categories
#print(df["Tournament"].cat.categories)