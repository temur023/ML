import pandas as pd

data = [100,200,300,400,500]

series = pd.Series(data, index=["a","b","c","d","e"])
print(series)
series.loc["c"] = 1000
print(series.loc["a"])
print(series)
print(series.iloc[2])

#filtering
print(series[series > 200])

calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 2000
}
cseries = pd.Series(calories)
print(cseries)