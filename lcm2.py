# find lcm and hcf of two numbers without using function
X = int(input("Enter first number: "))
Y = int(input("Enter second number: "))

if X > Y:
    greater = X
else:
    greater = Y

while True:
    if (greater%X==0) and (greater%Y==0):
        LCM = greater
        print(LCM)
        break
    greater += 1

if X < Y:
    smaller = X
else:
    smaller = Y
for i in range(2,smaller+1):
    if (X%i==0) and (Y%i==0):
        HCF = i
        print("The HCF of the number is: ",HCF)
        

