import random

# Create a list toss
toss = []

# Populate it randomly with 100 values H or T
for i in range (0, 100):
    toss += random.choice(['H', 'T'])

# Display results
print("Heads: ", toss.count('H'))
print("Tails: ", toss.count('T'))