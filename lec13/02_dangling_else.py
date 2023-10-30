import random

dice_roll = random.randint(1, 6)
if dice_roll > 3:
    print("It's a hit!")
    if dice_roll == 6:
        print("Doubled!")
    # else: # if it's not a 6...
    #     print("You missed!") 
else:
    print("You missed!")

print("Game over")
    