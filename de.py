# decimal to binary converter without bin function
N = int(input("Enter the decimal number: "))
# print(bin(N).replace("0b", ""))
b = ""
while N > 0:
    b = str(N % 2) + b
    N = N // 2
print(b)
