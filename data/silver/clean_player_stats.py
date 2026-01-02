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

df.info()
#print(df.describe())
#print(df.head(10))

#convert to catagorical columns for Tournament, Stage, Match Type, Player, Teams
#show memory savings
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

#Player Col
print("Player Col Categorical Conversion Memory usage")
print("Before: ", df["Player"].memory_usage(deep=True))
df["Player"] = df["Player"].astype("category")
print("After: ", df["Player"].memory_usage(deep=True), "\n")

#Teams Col
print("Teams Col Categorical Conversion Memory usage")
print("Before: ", df["Teams"].memory_usage(deep=True))
df["Teams"] = df["Teams"].astype("category")
print("After: ", df["Teams"].memory_usage(deep=True), "\n")

#see categories
#print(df["Tournament"].cat.categories)

#explore categorical data cols
cat_metrics = [
    "Tournament", 
    "Stage", 
    "Match Type", 
    "Player", 
    "Teams"]

def cat_exploration():
    for col in cat_metrics:
        print(f"{col} Summary: ")
        print(df[f"{col}"].value_counts(), "\n")


#explore numerical data cols
num_metrics = [
    "Rounds Played",
    "Rating",
    "Average Combat Score",
    "Kills:Deaths",
    "Average Damage Per Round",
    "Kills Per Round",
    "Assists Per Round",
    "First Kills Per Round",
    "First Deaths Per Round",
    "Maximum Kills in a Single Map",
    "Kills",
    "Deaths",
    "Assists",
    "First Kills",
    "First Deaths"
]

def numerical_exploration():
    for col in num_metrics:
        print(f"{col} Summary: ")
        print("Min: ", df[f"{col}"].min())
        print("Max: ", df[f"{col}"].max())
        print("Mean: ", df[f"{col}"].mean())
        print("Std: ", df[f"{col}"].std(), "\n")

numerical_exploration()
cat_exploration()
