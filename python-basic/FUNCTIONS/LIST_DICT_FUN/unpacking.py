lax_coordinates = [33.9425, -118.408056]

# Unpacking
latitude, longitude = lax_coordinates

a, b, *rest = [1, 2, 3, 4, 5]
a, *rest, b = [1, 2, 3, 4, 5]
*rest, a, b = [1, 2, 3, 4, 5]
a, b, *rest = "Hello"
a, b, *rest = "PY"


# print(*range(3, 6), *[1,2], sep=', ')  # 3 4 5


#unpacking dicts

a, b, *rest = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(a, b, rest)

def dump(a, b, c=1, d=2, *args, **kwargs):
    print(a, b, c, d, args, kwargs)

def dump2(*args):
    print(type(args))
    print(args[0])
    print(*args)

# dump(**{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

dump2(*[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
