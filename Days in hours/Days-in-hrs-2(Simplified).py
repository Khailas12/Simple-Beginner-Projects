def hrs_days(hrs=24):
        x = int(input("Enter the days: "))
        y = x * hrs
        print(f"hours in {x} days are {y}")
hrs_days()

while True:
    command = input("\nDo u wanna Continue [Y/N]: ").lower()
    if command == "y":
        print("\nLet's go again")
        hrs_days()

    elif command == "n":
        print("Bye")
        break
    else:
        print("Invalid input")

