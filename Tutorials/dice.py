import random

number = random.randint(1, 6)
roll = input("Type roll to roll the dice: ")
if roll == "roll":
    print("You rolled a", number)
else:
    print("You didn't type roll")
    