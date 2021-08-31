import string

while True:
    def translator(phase):
        translation = ""
        for letter in phase:

            if letter.lower() in "aeiou":
                if letter.isupper():
                    translation += "G"
                else:
                    translation += "g"

            else:
                translation += letter
        return translation

    y = translator(input("Enter: "))
    print(f"Translated O/P: {y}")

    
    x = input("\nDo u wanna continue: [Y/N]: ").lower()
    if x == "y":
        print("Here we go again") 

    elif x != "y" and "n":
        y = input("\nInvalid entry, Please Try again [Y/N]: ").lower()
        if y == "y":
            print("Alright, Here we go again\n")
        else:
            y == "n"
            print("Bye")
            break

    else:
        x == "n"
        print("Adios Amigo")
        break
    
