# List comprehension for hotel with three buildings
# 15 floors and 20 rooms on each floor
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Assign some rooms to guests
rooms[1][9][13] = True
rooms[2][9][13] = True
rooms[2][8][11] = True
rooms[1][6][10] = True
rooms[2][2][2] = True
rooms[1][1][1] = True
rooms[0][4][1] = False

# Check for vacancy on the 15th floor of the hotel
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

#Display results
print("We have {} rooms vacant".format(vacancy))