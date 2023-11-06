import random

def roll_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)

def count_12s_in_n(n: int) -> int:
    """
    Roll dice n times, counting how many 12s we get
    """
    num_12s = 0
    # _ is a convention for unused variable
    for _ in range(0, n, 1): 
        dice_roll = roll_dice()
        if dice_roll == 12:
            num_12s += 1
    
    return num_12s

def main() -> None:
    num_rolls = int(input("How many rolls would you like to do? "))
    num_12s = count_12s_in_n(num_rolls)
    print(f"You got {num_12s} 12s!")

main()
    