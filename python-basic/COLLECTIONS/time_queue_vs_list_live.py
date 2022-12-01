import timeit
def time_it(N):
    setup_queue = f"from collections import deque;dq = deque(range({N},0,-1))"
    fifo_queue = "dq.appendleft(None); dq.pop()"

    queue_time = timeit.repeat(setup = setup_queue,
             stmt = fifo_queue,
             repeat = 3,
             number = 1000)

    queue_mean = sum(queue_time) / len(queue_time)

    setup_list = f"l = list(range({N}, 0,-1))"
    fifo_list = "l.append(None);l.pop(0)"

    list_time = timeit.repeat(setup = setup_list,
             stmt = fifo_list,
             repeat = 3,
                number = 1000)

    list_mean = sum(list_time) / len(list_time)

    return queue_mean, list_mean

x = [10, 100, 1000, 10000, 100000]

#result = []

# for N in x:
#      result.append(time_it(N))

result = [ time_it(N) for N in x ]

queue_r = [t[0] for t in result]
list_r = [t[1] for t in result]

print('RESULT:', result)
print('')
print('queue:', queue_r)
print('list:', list_r)

import matplotlib.pyplot as plt

plt.plot(x, list_r, marker='o', label='list O(N)')
plt.plot(x,queue_r, marker='o', label="queue O(1)")
plt.legend()
plt.xlabel('N element in sequence')
plt.ylabel('time')

plt.show()
