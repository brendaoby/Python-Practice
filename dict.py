dictionary = {
                "cat": "chat",
                "dog": "chien",
                "horse": "cheval",
                "cow": "vache",
                "owl": "chouette"
}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")