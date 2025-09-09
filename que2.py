#Combine two lists index-wise(columns wise)
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
list3= []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)
