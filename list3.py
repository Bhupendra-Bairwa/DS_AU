#list compreshion

new_list = list(range(1,10))
print(new_list)
# squared_list = [i**2 for i in new_list]
# print(squared_list)

# squared_list = [i**2 for i in new_list if i%2==0]
# print(squared_list)

# even_odd = ['even' if i%2==0 else 'odd' for i in new_list]
# print(even_odd)

list_less_6 =[i for i in new_list if i<6]
print(list_less_6)