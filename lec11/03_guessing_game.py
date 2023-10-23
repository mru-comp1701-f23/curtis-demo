import random
TARGET = random.randint(1, 10)

def main() -> None:
    print(f"TARGET: {TARGET}") # debug print statement
    num = int(input("Guess a number between 1 and 10: "))
    if num == TARGET:
        print("Yay! You win!")
        # 1 / 0 Runtime error
    else:
        print("Sorry, better luck next time")

main()