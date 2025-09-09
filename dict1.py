# make a list and itrate it and make a dictionary with the count of each element
list34 = ["a","b","m","x","y","a","m","m"]
dict1 = {}
for ele in list34:
    if ele in dict1:
        dict1[ele] += 1
    else:
        dict1[ele] = 1
print(dict1)