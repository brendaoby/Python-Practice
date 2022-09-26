# User inputs investment amount and expected interest
invest = input("Enter your total investment: ")
rate = input("Enter your expected investment rate: ")

# Convert to float and round rate to 2 decimal places
invest = float(invest)
rate = float(rate) * .01

# Each year interest increases by investment + investment * interest rate
for i in range(10):
    earn = invest + (invest * rate)

# Displays earnings after a 10 year period
print("Your earnings after a 10 year period will be ${:.2f}".format(earn))