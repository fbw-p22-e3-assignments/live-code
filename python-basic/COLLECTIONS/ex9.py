def value_factory(index):
    def decorator(func):
        def inner(item):
            return func(item)[index]
        return inner
    return decorator

@value_factory(0)
def sort_helper(item):
    return item

def count_characters(string):
    dict_char = {}
    for char in string.lower():
        dict_char[char] = string.lower().count(char)
    return dict(sorted(dict_char.items(), key=sort_helper))

print(count_characters("Elephant"))
