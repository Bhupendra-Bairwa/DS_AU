# take  a number 0-9 and print the 3+33+333+...n times
n = int(input("enter a number: "))
t = 0
s = 0
for i in range(1,n+1):
    t = t * 10 + n
    print(t,end=" + ")
    s = s + t
print("\b\b =",s)
