dict = {
    "model": "Ferrari",
    "year": 2020
}
print(dict["model"])
dict["color"] = "red"
print(dict)
dict["year"] = 2021
print(dict)
print(dict.values())

if "model" in dict:
    print("Yes, 'model' is one of the keys in the dict dictionary.")

for x in dict:
    print(dict[x])

for x,y in dict.items():
    print("key: " + x + ", value: " + str(y))