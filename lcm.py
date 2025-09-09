# find the LCM and HCF of two numbers
def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x
def lcm(x, y):
    return (x * y) // hcf(x, y)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))
print("The HCF of", num1, "and", num2, "is", hcf(num1, num2))