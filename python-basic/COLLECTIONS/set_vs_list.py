import time

def timer_factor(rounds=3):
    def timer(func):
        def inner(*args, **kwargs):
            results = []
            for i in range(rounds):
                start = time.time()
                value = func(*args, **kwargs)
                elapsed_time = time.time() - start
                results.append(elapsed_time)
                print(f"Elapsed time: {elapsed_time:0.6f} seconds")
            return value, sum(results) / len(results)
        return inner
    return timer

@timer_factor(rounds=3)
def union_set(needles, haystack):
    return len(needles & haystack)

@timer_factor(rounds=3)
def union_list(needles, haystack):
    found = 0
    for needle in needles:
        if needle in haystack:
            found +=1
    
    return found

import random
sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]

needles = list(range(1000))
random.shuffle(needles)
def generate_haystack(N):
    haystack = list(range(1000, N + 500))
    # random.shuffle(haystack)
    haystack = [*haystack, *needles[:500]]
    # for i in range(500):
    #     haystack.insert(random.randrange(N - 501),needles[i])
    # for i in range(1000):
    #     removed = haystack.pop(random.randrange(N - 1))
    #     haystack.insert(random.randrange(N - 1),removed)
    return haystack

Y_set = []
Y2_list = []
for size in sizes:
    haystack = generate_haystack(size)
    print(f"**************Size: {size}**************")
    print("Set:")
    _, avg_set = union_set(set(needles), set(haystack))
    print("List:")
    _, avg_list = union_list(needles, haystack)
    print(f"Set: {avg_set:0.6f} seconds, List: {avg_list:0.6f} seconds")
    Y_set.append(avg_set)
    Y2_list.append(avg_list)

import json
with open("set_vs_list.json", "w") as f:
    json.dump({"sizes": sizes, "set": Y_set, "list": Y2_list}, f)
