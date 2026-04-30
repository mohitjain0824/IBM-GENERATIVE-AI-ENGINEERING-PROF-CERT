import pandas as pd
import numpy as np

# 1. load data directly from url
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(url, header=None)
# print(df)

# 2. add headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
# print(df)

# 3. clean the data
# replace ? with NaN and drop rows where price is missing
df.replace('?', np.nan, inplace=True)
df.dropna(subset=["price"], axis=0, inplace=True)
# print(df)

# 4. get insights
print("--first 5 rows--")
print(df.head())

print("\n--column data types--")
print(df.dtypes)

print("\n--statistical summary--")
print(df.describe(include="all"))

print("\n--dataframe info--")
df.info()

# 5. save the result locally
df.to_csv("cleaned_automobile.csv", index=False)
print("\nFile saved as cleaned_automobile.csv")