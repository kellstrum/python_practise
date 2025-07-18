number1 = int(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
number2 = int(input("Enter the second number: "))

if operator == "+":
     total = number1 + number2
elif operator == "-":
     total = number1 - number2
elif operator == "*":
     total = number1 * number2
elif operator == "/":
     total = number1 / number2
else:
     print("Sorry I don't know how to do", operator, "math")
     total = None
    
if total is not None:
     print("The answer is:", total)