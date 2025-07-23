import random

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll = input("Roll the dice? Y/N: ").capitalize()
    if roll == "Y":
        print(f"You rolled {die1}, {die2}")
    elif roll == "N":
        print("Goodbye!")
        break
    else:
        print("That's not a valid option")
