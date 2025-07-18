age = int(input("Enter your age: "))

if age < 3:
    print("Your ticket is free!")
elif age <= 12:
    print("your ticket is $10")
elif age <= 64:
    print("Your ticket is $20")
else:
    print("Your ticket is $15")