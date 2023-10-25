import random
TARGET = random.randint(1, 10)

def play_game(guess: int) -> str:
    """
    Compares user's guess to target, returns string with win or not.
    """
    result = ""
    if guess == TARGET:
        result = "Yay! You win!"
    elif guess < TARGET:
        result = "Too low!"
    # could be elif guess > TARGET
    else: # must be greater than
        result = "Too high!"
    
    return result


def main() -> None:
    print(f"TARGET: {TARGET}") # debug print statement
    num = int(input("Guess a number between 1 and 10: "))
    print(play_game(num))

main()