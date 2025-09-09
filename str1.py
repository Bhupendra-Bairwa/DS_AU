# change an integer number into string without using string function
n = int(input("enter a number: "))
s = ''
while n > 0:
    r = n % 10
    s = chr(r + 48) + s
    n = n // 10
print(s)
print(type(s))
