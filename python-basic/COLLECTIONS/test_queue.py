import timeit

def time_it(N):
    setup_queue=f"from collections import deque;dq = deque(range({N}, 0, -1))"
    fifo_queue = "dq.appendleft(None); dq.pop()"

    queue_time= timeit.repeat(setup = setup_queue, 
                     stmt = fifo_queue,
                     repeat = 3,
                     number = 1000)

    queue_mean = sum(queue_time) /len(queue_time)


    setup_list=f"l = list(range({N}, 0, -1))"
    fifo_list = "l.append(None); l.pop(0)"

    list_time = timeit.repeat(setup = setup_list, 
                     stmt = fifo_list,
                     repeat = 3,
                     number = 1000)

    list_mean = sum(list_time) /len(list_time)

    return queue_mean, list_mean

x = [10, 100, 1000, 10000, 100000]

result_list = [time_it(N) for N in x]

import matplotlib.pyplot as plt

queue_r = [t[0] for t in result_list]
list_r = [t[1] for t in result_list]

plt.plot(x, list_r, label="list O(N)")
plt.plot(x, queue_r, label="queue O(1)")
plt.legend()
plt.xlabel("N")
plt.ylabel("time")
plt.show()
