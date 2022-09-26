# Receive age from user and store in age
age = int(input("Enter your age: "))

# Decide if is important or not based on given conditions
if (age >= 1) and (age <= 18):
    print("Important birthday!")
elif (age == 21) or (age == 50):
    print("Important birthday!")
elif not (age < 65):
    print("Important birthday!")
else:
    print("Sorry, not important")
