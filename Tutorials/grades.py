score = int(input("Enter your score: "))

if score < 60:
    print("You got an F")
elif score < 70:
    print("You got a D")
elif score < 80:
    print("You got a C")
elif score < 90:
    print("You got a B")
else:
    print("You got an A!")
