# Removing all repeated values from a given list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

# Browse all numbers from the source list.
for number in my_list:
    # If the number doesn't appear within the new list append it here.
	if number not in new_list:
        new_list.append(number)

# Make a copy of new_list
my_list = new_list[:]
print("The list with unique elements only:")
print(my_list)