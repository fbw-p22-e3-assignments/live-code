def count_characters(string):
    dict_char = {}
    for char in string.lower():
        dict_char[char] = string.lower().count(char)
    return dict(sorted(dict_char.items(), key=lambda x: x))

print(count_characters("Elephant"))
