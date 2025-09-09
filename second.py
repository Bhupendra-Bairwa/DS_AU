# swapping two numbers without using a third variable

A = int(input("enter the number: "))
B = int(input("enter another number: "))

A = A + B
B = A - B
A = A - B

print("after swaping the value of A is: ",A)
print("after swaping the value of B is: ",B)