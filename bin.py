# binary to decimal converter without int function
b = input("Enter the binary number: ")
d = 0
for i in range(len(b)):
    d = d + int(b[len(b)-1-i]) * (2**i)
print(d)