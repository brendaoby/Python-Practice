# Prompt user to enter word
user_word = input("Enter your word: ")

# Convert words to uppercase letters
user_word = user_word.upper()

# Eat up the vowels and dsiplay the voweless word
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
