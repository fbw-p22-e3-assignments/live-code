a = {
    'a': 1,
    'b': 2,
    'c': 3,
        }

b = [1,2, {'c':2}]

print(a.get('e'))
print(a.get('e', 80))
print(b[len(b)])
