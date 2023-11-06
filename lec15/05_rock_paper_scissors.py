import random

def play_game(comp: str, user: str) -> str:
    """
    Compares computer choice to user choice,
    returns string with winner.
    """
    if comp == user:
        winner = "Everyone"
    elif (comp == "r" and user == "p" 
          or comp == "p" and user == "s" 
          or comp == "s" and user == "r"):
        winner = "User"
    else:
        winner = "Computer"
    
    return winner

def get_computer_choice() -> str:
    x = random.randint(1, 3)
    if x == 1:
        choice = "r"
    elif x == 2:
        choice = "s"
    else:
        choice = "p"
    return choice

def valid_input() -> str:
    """
    Prompt the user to enter a value until r/p/s is found.
    """
    response = input("Chooose between r/p/s: ")
    while response != "r" and response != "p" and response != "s":
        print("I said choose between r, p, and s!")
        response = input("Chooose between r/p/s: ")
    
    return response

def play_repeatedly() -> None:
    play_again = "y" # assume the user wants to play at least once
    while play_again.lower() == "y":
        comp_choice = get_computer_choice()
        user_choice = valid_input()
        winner = play_game(comp_choice, user_choice)
        print(f"{winner} wins!")

        # update at the end
        play_again = input("Would you like to play again? (y/n): ")

def main() -> None:
    print("Welcome to rock paper scissors!")
    play_repeatedly()
    print("Thanks for playing!")

main()