import random

def guess(x):
    rand = random.randint(1, x)
    guess = 0
    while guess != rand:
        guess = int(input(f"Enter nums btwn 1 & {x}: "))
        if guess > rand:
            print("Too high")
        elif guess < rand:
            print("Too low")


def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f" Guess: {guess} \n (H) -> High \n (L) -> Low \n (C) -> Correct \n Enter: ").upper()
        print("\n")

        if feedback == "H":
            high = guess - 1

        elif feedback == "L":
            low = guess + 1
        
        else:
            feedback != "H" and "L" 
            feedback == ""
            print("Invalid Feedback")


    print("The guessed number is")
    
comp_guess(10)

