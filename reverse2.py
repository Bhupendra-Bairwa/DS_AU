N = int(input("enter the number: "))
rev = 0
while N>0:
    a = N%10
    N = N//10
    rev = rev*10 + a
print(rev)