import random
TARGET = random.randint(1, 10)

def guess_in_n(n: int) -> bool:
    """
    Prompt the user to guess a number in n chances.
    Return true if guessed, false otherwise.
    """
    num_guesses = 0
    found = False
    # loop until num_guesses is 3 or number is found, then invert
    while num_guesses < 3 and not found:
        num = int(input("Guess a number between 1 and 10: "))
        if num == TARGET:
            found = True # modify LCV
        num_guesses += 1 # increment LCV
    
    return found

def main() -> None:
    print(f"TARGET: {TARGET}") # debug print statement
    if guess_in_n(3):
        print("Yay! You win!")
        # 1 / 0 Runtime error
    else:
        print("Sorry, better luck next time")

main()