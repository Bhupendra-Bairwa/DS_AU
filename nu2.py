# take  a number 1-9 and print the 3+33+333+... only four times
n = int(input("enter a number: "))
t = 0
s = 0   
for i in range(1,5):
    t = t * 10 + n
    print(t,end=" + ")
    s = s + t   
print("\b\b =",s)