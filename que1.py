# small form of the name like Bhupendra Bairwa convert into BB using only one string
name = input("Enter your name: ")
ab = name.split()
for i in ab:
    print(i[0].upper(), end="")