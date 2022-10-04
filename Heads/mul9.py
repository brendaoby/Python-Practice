import random

# Generate random list from 1 to 1000
# Use range to generate 100 values
randList = list(random.randint(1, 1001) for i in range(100))

# Find multiples of 9
print(list(filter((lambda x: x % 9 == 0), randList)))