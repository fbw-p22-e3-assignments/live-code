def binary_searche(l, item):
    n = 0
    while len(l) > 1:
        n += 1
        # print()
        print(f"**************{n}. Iteration:**************")
        # print(*l)
        # print(f"length of list: {len(l)}")
        middle = len(l) // 2
        if item == l[middle] or item == l[0]:
            return True, n, item
        elif item < l[middle]:
            l = l[:middle]
        elif item > l[middle]:
            l = l[middle:]
    return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

# print(binary_searche(l, 3))
# print(binary_searche(l, 57))
print(binary_searche(l, 100))
# print(binary_searche(range(1,1001,8), 998))
# for size in [100,1_000, 10_000, 100_000]:
#     print(max([binary_searche(range(1,size + 1), i) for i in range(1, size + 1)]))
#     print(max([binary_searche(range(1,size + 1), i) for i in range(1, size + 1)]))


results = []
sizes = [100, 1_000, 10_000, 100_000, 1_000_000]
for size in sizes:
    _, steps, *rest = binary_searche(range(1,size + 1), size)
    results.append(steps)

import matplotlib.pyplot as plt

def plot(sizes, results):
    plt.plot(sizes, results, marker='x', label='binary search')
    plt.xlabel('size of list')
    plt.ylabel('steps')
    plt.legend()
    plt.title("Big O of Binary Search")
    # plt.xscale('log')
    plt.show()

plot(sizes, results)
print([*zip(sizes, results)])
