# Ask user to input two values and store them in num1 and num 2
num1, num2 = input("Enter two numbers: ").split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# Add values and store the result in sum
sum = num1 + num2

# Subtract values and store the result in difference
difference = num1 - num2

# Multiply values and store result in product
product = num1 * num2

# Divide values and store result in quotient
quotient = num1 / num2

# Use modulus on values to find the remainder
remainder = num1 % num2

# Print results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))