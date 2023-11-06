INTEREST = 0.02

def acccumulate_interest(starting_balance: float, 
                         n: int, add_per_year: float) -> float:
    """
    Starting at starting_balance, add compound interest each year
    for n years. Return the final balance.
    """

    # accumulator initialization
    balance = starting_balance
    for year in range(0, n, 1):
        balance += add_per_year
        balance *= (1 + INTEREST)
        print(f"Year {year}: {balance}") # debug print statement
        # same as balance = balance * (1 + INTEREST)
    
    return balance

def main() -> None:
    final = acccumulate_interest(100, 10, 50)
    print(f"You have ${final:.2f}")

main()