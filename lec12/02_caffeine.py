def print_caffeine_needs(caffeine: float) -> None:
    """
    Informs the user if they have enough caffeine
    """
    if caffeine > 200:
        print("TOO MUCH!")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 50:
        print("Good start")
    else:
        print("You need more!")

def print_caffeine_backwards(caffeine: float) -> None:
    if caffeine > 50:
        print("Good start")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 200:
        print("TOO MUCH!")
    else:
        print("You need more!")

def main() -> None:
    print_caffeine_needs(75)
    print_caffeine_backwards(75)
    print_caffeine_needs(0)
    print_caffeine_backwards(0)
    print_caffeine_needs(320)
    print_caffeine_backwards(320)

main()