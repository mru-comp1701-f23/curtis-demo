def add_until_enough(balance: float, 
                     enough: float, 
                     amount_to_add: float) -> None:
    while balance < enough:
        balance = balance + amount_to_add
        enough = enough + amount_to_add * 0.5
        print(balance) # debug print
    
    print(f"You have ${balance}")


def add_until_negative() -> float:
    # priming read
    dollars = float(input("Welcome! Please start giving me money: "))
    total = 0
    # loop condition
    while dollars > 0:
        total += dollars
        # update
        dollars = float(input("How much money would you like to add? "))
    
    return total


def main() -> None:
    # add_until_enough(100, 1000, 100)
    total = add_until_negative()
    print(f"You added ${total:.2f}")

main()