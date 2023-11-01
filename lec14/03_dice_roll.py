import random

def roll_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)

def count_12s_in_n(n: int) -> int:
    """
    Roll dice n times, counting how many 12s we get
    """
    # Initialize LCV
    counter = 0 # LCV counter
    num_12s = 0
    while counter < n: # condition
        dice_roll = roll_dice()
        if dice_roll == 12:
            num_12s += 1
        counter += 1 # LCV update last in the loop
    
    return num_12s

def main() -> None:
    num_rolls = int(input("How many rolls would you like to do? "))
    num_12s = count_12s_in_n(num_rolls)
    print(f"You got {num_12s} 12s!")

main()
    