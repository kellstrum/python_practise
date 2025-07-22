import datetime

# Ask for birthday
birth_year = int(input("What year were you born? "))
birth_month_name = input("What month were you born? ").strip().capitalize()
birth_day = int(input("What day were you born? "))

# Convert month name to number
month_number = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# Find month number
birth_month = month_number.get(birth_month_name)

# Check
if birth_month is None:
    print("That is not a valid month")
else:
    # Get today's date
    today = datetime.date.today()

    # Calculate age
    age = today.year - birth_year
    birthday_has_passed = (today.month, today.day) >= (birth_month, birth_day)
    if not birthday_has_passed:
        age -= 1

    # Print result
    print(f"You are {age} years old!")

    if today.month == birth_month and today.day == birth_day:
        print("Happy Birthday!")
