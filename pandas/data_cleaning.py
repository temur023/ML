import pandas as pd

df = pd.read_csv("data.csv")
#1.drop irrelevant columns

# df = df.drop(columns=["Legendary", "No"])

#2
# df = df.dropna(subset=["Type2"])
df= df.fillna({"Type2":"None"})


#3 Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS "})


#4 Standardize text

df["Name"] = df["Name"].str.lower()


#5 Fix data types
df["Legendary"] = df["Legendary"].astype(bool)


#6 Remove duplicate values
df = df.drop_duplicates()
print(df.to_string())


