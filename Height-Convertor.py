def new():
    unit = input("Feet or CMS [F/C]: ").upper()

    if unit == "F":
        height = float(input("\nEnter your Height in Feet: "))
        cms = height * 30.48
        print(f"Height in CMS is {cms}")

        ft = float(input("\nEnter your Height in CMS: "))
        feet = ft / 30.48
        print(f"Your height in Feet is {feet}")

    else:
        print("Invalid Entry, Please Try Again")


def main():
    while True:
        new()
        command = input("\nDo you wanna continue [Y/N]: ").upper()
        if command == "Y":
            print("Let's Go Again")

        elif command == "N":
            print(("Bye.."))
            break

        else:
            print("Invalid Entry")
            return


main()
