can_vote = lambda age : True if age >= 18 else False

print("I can vote: " can_vote(16))

powerList = [lambda x: x **2, lambda x: x **3, lambda x: x **4]\

for func in powerList:
    print(func(4))

attack = {'quick': (lambda: print("Quick Attack")),
'power': (lambda: print("Power Attack"),
'miss': (lambda: print("Missed Attack")}

import random

# to let us select a random key

attackKey = random.choice(list(attack.keys())) # list() changes the dictionary to a list

attack[attackKey]()