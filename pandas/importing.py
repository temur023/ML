import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")
print(df.to_string()) #in order to print everything 

#SELECTION BY COLUMN
# print(df["Name"])
print(df["Height"])
print(df[["Height","Weight"]])

#SELECTION BY ROWS
print(df)
print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
print(df.iloc[0:11:2, 0:3]) #start end step, start:end columns

#Exercise
pokemon = input("Enter a name of a Pokemon: ")
# found = df.loc[pokemon]
# if(found.any()):
#     print(found)
# else:
#     print("Pokemon not found!")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} does not exist")