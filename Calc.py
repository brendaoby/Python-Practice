# Store the user input of two numbers and operator
num1, operator, num2 = input("Enter a calculation: ").split()

# Covert string to int
num1 = int(num1)
num2 = int(num2)

# if +, -, *, /, provide result based on addition, subtraction, multiplication, division
# Print result
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Use either +, -, * or /")
