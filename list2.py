# list functions
#append, extend, pop, remove, del

list45 = ['a','b',1,2,3,4,'bhai']

list45.append([90,99])
list45.append(100)
print(list45)

list45.extend([90,99])
print(list45)

list45 = list45+[67,89]
print(list45)

#pop return velue but remove can not return value

poped_item = list45.pop()  
print(poped_item)
print(list45)

removed_item = list45.remove(100)
print(removed_item)
print(list45)

del(list45[0])
print(list45)

# cleared_list = list45.clear()
# print(cleared_list)
# print(list45)