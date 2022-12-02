r = list(zip(range(3), 'ABC', [0.0, 1.1, 2.2], strict=True))
list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], strict=True))

print(r)