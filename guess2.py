# Guessing game 

import random
winning_numbar = random.randint(1,100)
print(winning_numbar)
counter = 0
while True:
    print("Guessing Game.......")
    your_guess = int(input("Enter your Guess: "))
    if your_guess == winning_numbar:
        print("Congrates you win.")
        break
    elif your_guess < winning_numbar:
        print("Go up")
        counter += 1
    elif your_guess > winning_numbar:
        print("Go Down")
        counter += 1
    if counter == 5:
        print("Tumse nahi ho payega")
        break