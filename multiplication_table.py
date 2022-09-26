import random
import math

# Create the multidimensional list
multTable = [[0] * 10 for i in range(10)]

# Increment with outer for loop
for i in range(1, 10):

# Increment with inner for loop
    for j in range(1, 10):

# Assign the value to the cell
        multTable[i][j] = i * j

# Output the data
for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end="  ")
    print()