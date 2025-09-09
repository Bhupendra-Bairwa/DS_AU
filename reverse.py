N = int(input("enter the number: "))
rev = 0
a = N % 10
N = N // 10
rev  = rev*10 +a
b = N % 10
N = N // 10
rev  = rev*10 +b
c = N % 10
rev  = rev*10 +c
print(rev)