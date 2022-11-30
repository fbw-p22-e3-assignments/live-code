A = ['x', 'y', 'z']
B = [1, 2, 3]

def cartasian_prod(A,B):
    result = []
    for item1 in A:
        for item2 in B:
            result.append((item1, item2))
    return result

print(cartasian_prod(A, B))
