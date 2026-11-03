def is_pangram(text):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(text.lower()))

# print(is_pangram("Hekkoisaf ad"))