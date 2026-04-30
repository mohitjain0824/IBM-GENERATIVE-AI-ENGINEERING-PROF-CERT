import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. IMPORT DATA ---
# Source URL for the Automobile Dataset
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

# Define headers as specified in the lab
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# Load the dataset directly into a Pandas dataframe
df = pd.read_csv(url, names=headers)

# --- 2. IDENTIFY AND HANDLE MISSING VALUES ---
# Convert "?" to NaN for computational speed and convenience[cite: 2]
df.replace("?", np.nan, inplace=True)

# Replace missing 'normalized-losses' with the mean[cite: 2]
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg_norm_loss)

# Replace missing 'bore' with the mean[cite: 2]
avg_bore = df['bore'].astype('float').mean(axis=0)
df["bore"] = df["bore"].replace(np.nan, avg_bore)

# Replace missing 'stroke' with the mean (Question #1)[cite: 2]
avg_stroke = df["stroke"].astype("float").mean(axis=0)
df["stroke"] = df["stroke"].replace(np.nan, avg_stroke)

# Replace missing 'horsepower' and 'peak-rpm' with their respective means[cite: 2]
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'] = df['horsepower'].replace(np.nan, avg_horsepower)

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'] = df['peak-rpm'].replace(np.nan, avg_peakrpm)

# Replace missing 'num-of-doors' with the most frequent value ("four")[cite: 2]
most_freq_door = df['num-of-doors'].value_counts().idxmax()
df["num-of-doors"] = df["num-of-doors"].replace(np.nan, most_freq_door)

# Drop all rows that do not have price data[cite: 2]
df = df.dropna(subset=["price"], axis=0)
df = df.reset_index(drop=True)

# --- 3. CORRECT DATA FORMAT ---
# Convert columns to correct numerical types[cite: 2]
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price", "peak-rpm"]] = df[["price", "peak-rpm"]].astype("float")

# --- 4. DATA STANDARDIZATION ---
# Convert mpg to L/100km (L/100km = 235 / mpg)[cite: 2]
df['city-L/100km'] = 235 / df["city-mpg"]

# Transform highway-mpg to highway-L/100km (Question #2)[cite: 2]
df["highway-mpg"] = 235 / df["highway-mpg"]
df = df.rename(columns={'highway-mpg': 'highway-L/100km'})

# --- 5. DATA NORMALIZATION ---
# Scale 'length', 'width', and 'height' to a range of 0 to 1[cite: 2]
df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max() # (Question #3)[cite: 2]

# --- 6. BINNING ---
# Group horsepower into 'Low', 'Medium', and 'High' categories[cite: 2]
df["horsepower"] = df["horsepower"].astype(int)
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)

# --- 7. INDICATOR (DUMMY) VARIABLES ---
# Convert 'fuel-type' to indicator variables for regression[cite: 2]
dummy_fuel = pd.get_dummies(df["fuel-type"])
dummy_fuel.rename(columns={'gas': 'fuel-type-gas', 'diesel': 'fuel-type-diesel'}, inplace=True)
df = pd.concat([df, dummy_fuel], axis=1)
df = df.drop("fuel-type", axis=1)

# Convert 'aspiration' to indicator variables (Question #4 & #5)[cite: 2]
dummy_aspiration = pd.get_dummies(df['aspiration'])
dummy_aspiration.rename(columns={'std': 'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
df = pd.concat([df, dummy_aspiration], axis=1)
df = df.drop('aspiration', axis=1)

# --- 8. FINAL OUTPUT ---
print("Successfully wrangled data. Final columns:")
print(df.columns.values)
print("\nPreview of first 5 rows:")
print(df.head())

# Save the final cleaned dataframe[cite: 2]
df.to_csv('clean_df.csv', index=False)