import pandas as pd

df = pd.read_csv("data.csv")


print(df[df["Height"] > 2])
print(df[df["Weight"] > 100])
print(df[df["Legendary"] == 1])