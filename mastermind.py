import random

COLORS = ["R", "G", "B", "Y", "W", "0"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_cude():
        
    while True:
        guess = input("Guess: ").upper().split(" ")
        
        if len(guess) != CODE_LENGTH:
            print(f"You must guess 4 colors.")
            continue
    
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess
    