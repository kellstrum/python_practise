def calculate_dog_years(human_age):
    dog_years = human_age * 7
    print("You are " + str(dog_years) + " in dog years!")
    
age = int(input("What is your age? "))
calculate_dog_years(age)