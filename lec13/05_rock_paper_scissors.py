import random

def play_game(comp: str, user: str) -> str:
    """
    Compares computer choice to user choice,
    returns string with winner.
    """
    print(f"Computer chose {comp}, you chose {user}")

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

def main() -> None:
    comp_choice = get_computer_choice()
    user_choice = input("Chooose between r/p/s: ")
    winner = play_game(comp_choice, user_choice)
    print(f"{winner} wins!")

main()