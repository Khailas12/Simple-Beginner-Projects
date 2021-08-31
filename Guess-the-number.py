import random

x = int(input("Enter the lower num: "))
y = int(input("\nEnter the higher num: "))

limit = 5
num = random.randint(x, y)
tries = print(f"\nYou have got {limit} Healths to play")
count = 0
guess = ""

while count < 5:
    guess = int(input("Take a guess: "))
    count += 1
    if num > guess:
        print("\nToo low")

    elif num < guess:
        print("\nToo High")

    else:
        num == guess
        if limit == 5:
            print(f"{num} is Correct, You just competed it in the first Try")
        else:
            if limit == 1:
                print(f"You just finished with {limit} health")
            else:    
                print(f"\n          Your guess was {num} \nCompeted within {count} tries and with {limit} Healths left")
        break
    
    limit -= 1
    print(f"\nYou have {limit} more Healths Left")

if guess != num:
    print(f"\nOops, Out of Health \nThe num was {num}")



    
        
