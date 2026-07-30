import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}
df = pd.DataFrame(data,index=["Employee 1", "Empoloyee 2", "Employee 3"])
#Add a new column
df["Job"] = ["Cook", "N/A","Cashier"]

#Add a new row
new_row = pd.DataFrame([{"Name": ["New", "Eugine"],"Age":[25,60],"Job":["N/a","Manager"]}], index=["Employee 4","Employee 5"])
df = pd.concat([df, new_row])

print(df)
print(df.loc["Employee 1"])
print(df.iloc[2])