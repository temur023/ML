list = ["apple", "banana", "cherry", "orange"]
list2 = [1, 5, 7, 9, 3]
print(list[-5:-2])
if "apple" in list:
    print("Yes, 'apple' is in the list")

#inserting
list.insert(2, "watermelon")
print(list)

#merging 2 lists
#list.extend(list2)

#looping
for x in list:
    print(x)

#list comprehension
newlist = [x for x in list if x.startswith("a")]
newlist = [x.upper() for x in newlist]
print(newlist)