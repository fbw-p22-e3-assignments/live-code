list2 = [0,1,2,3,4]

import math

def exp(x):
    return math.exp(x)

def twice(x):
    return 2 * x

def filter_helper(item):
    return item % 2 == 0

filtered_list = (filter(filter_helper, list2))

# print(list(map(exp, filter(filter_helper, list2))))
print(list(map(twice, filtered_list)))

print([twice(x) for x in list2 if x % 2 == 0])
