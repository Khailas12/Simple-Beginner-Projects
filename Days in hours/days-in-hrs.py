hrs = 24
days = ""
while True:
    x = int(input("Enter the num of days: "))
    y = hrs * x
    if x == 1:
        print(f"Hours in 1 day is {y}\n")
    else:
        print(f"Hours in {x} days are {y}\n")
    
    command = input("Do You wanna continue [Y/N]: ").lower()
    if command == "y":
        print("Here we go again\n")

    elif command == "n":
        print("bye")
        break
    
    else:
        command != "y" and "n"
        c = input("Invalid Entry, Please try again [Y/N]: ").lower()
        if c == "y":
            print("Good to go\n")
        elif c == "n":
            print("Bei")
            break
        else:
            print("Maximum Entry Exceeded, bye")
            break