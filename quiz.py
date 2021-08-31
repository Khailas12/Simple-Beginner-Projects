def sample():
    command = input("\n X for Clue\n [A / B / C / D]\nEnter: ").upper()
    return command

def nam():
    name = input("What's your name: ")
    print(f"Well {name}, Let's begin...\n")

clues = 3
count = 0

def ques1():
    global clues
    global count
    print("1) Whos's the CEO of Google?\n A. Bill Gates\n B. Sundar Pichai\n C. Tim Cook\n D. Elon Musk")
    q1 = sample()
    if q1 == "B":
        count += 1
        print("\nRight Answer\n")

    elif q1 == "X":
        print("\nClue: He's an Indian\n")
        ques1()

    else:
        count == 0
        print(f"\nOops, B. Sundar Pichai was the right answer\n")

def ques2():
    global count
    global clues
    print("\n2) Where is the headquarters of Microsoft?\n A. Texas\n B. New York\n C. California\n D. Florida")
    q2 = sample()
    if q2 == "C":
        count += 1
        print("\nRight Answer\n")

    elif q2 == "X":
        clues -= 1
        print("\nClue: Silicon Valley\n")
        ques2()

    else:
        count == 1
        print(f"\nOops, C. Ejmel Was the right Answer\n")

def ques3():
    global count
    print("\n3) Who's the Director of Titanic?\n A. Steven Spielberg\n B. Quentin Tarantino\n C. David Fincher\n D. James Cameron")
    q3 = sample()
    if q3 == "D":
        count += 1
        print(f"\nRight Answer\n")
    
    elif q3 == "X":
        print("\nClue: Director of Terminator")
        ques3()

    else:
        count == 0
        print(f"\nOops, D. James Cameron Was the right answer\n")


def point():
    print(f"Your Current point is {count}\n")
    print(f"You have {clues} clues left")

def total_point():
    print(f"The total points you've earned is {count}")     

def main():
    nam()
    ques1()
    point()
    ques2()
    point()
    ques3()
    total_point()

main()





