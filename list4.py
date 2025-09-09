A = [[1,2,3],['a','b','c']]
new_list = [ele for sublist in A for ele in sublist]
print(new_list)