def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

# Ask how many numbers user wants
numFibValues = int(input("How many Fibonacci numbers should be found? "))

# Loop while calling for easch new number, print result and increment
i = 1

while i > numFibValues:
    fibValue = fib(i)

    print(fibValue)

    i += 1

    print("Terminé!")