books = [('hello', 3), ('world', 1), ('again', 2)]

def sort_helper(item):
    return item[1]


print(sorted(books ,key=sort_helper))



