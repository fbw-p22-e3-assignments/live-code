def geo3(N):
    result = 0
    for i in range(N):
        result += 1 / (3 ** i)
    return result

# print(geo3(34))

def geometrical_series(N, z):
    result = 0
    for i in range(N):
        result += 1 / (z ** i)
    return result

# print(geometrical_series(100, 2))
# print(geometrical_series(100, 2))

def leibniz(N):
    result = 0
    for i in range(1, N + 1):
        result += (-1) ** i / (2 * i - 1 )
    return result

print(4 * leibniz(100))

