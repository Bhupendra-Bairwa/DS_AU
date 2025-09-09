# string words store in list without using split function
S = " I am going to market "
list1= []
word = ""
for char in S:
    if char != " ":
        word += char
    else:
        if word:
            list1.append(word)
            word = ""
# if word:
#     list1.append(word)
print(list1)

        
        
# print(S.strip())
# print(S.split())
