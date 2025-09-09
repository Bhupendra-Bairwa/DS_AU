N = int(input("enter the number: "))
total = 0
# to calculate the sum of first N natural numbers
if N < 0:
    print("Please enter a positive integer")
else:
    total = sum(range(1, N + 1))
    print("The sum of the first", N, "natural numbers is:", total)
    
    