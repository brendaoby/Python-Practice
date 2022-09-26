# Allow user to input age, convert to int and store in age
age = int(input("Please enter your age: "))

# Decide grade and output result based on given conditions
if (age < 5):
    print("Sorry sugar, you can't go to school until you're 5")
elif (age == 5):
    print("Go to Kindergarten, honey!")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}, sweetie!".format(grade))
else:
    print("Go to college, champ!")