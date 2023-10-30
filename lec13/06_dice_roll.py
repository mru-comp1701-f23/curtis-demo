import random

def roll_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)

def rolls_until_12() -> int:
    """
    Repeatedly roll dice until a 12 is reached.
    Returns number of rolls.
    """
    # Initialize LCV
    dice_roll = roll_dice()
    counter = 1
    while dice_roll != 12: # condition
        counter = counter + 1
        print(counter)
        dice_roll = roll_dice() # LCV update last in the loop
    
    return counter

def main() -> None:
    print(f"It took {rolls_until_12()} rolls to get a 12!")

main()
    