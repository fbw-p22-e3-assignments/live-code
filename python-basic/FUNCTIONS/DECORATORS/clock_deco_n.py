import time

def clock(fun):
    def clocked(n):      ####inner function
        t0 = time.time()
        result = fun(n)  ### fun is the free variable of the closure
        elapsed = time.time() - t0
        print("{elapsed}s func --> {result}".format(elapsed=elapsed, result=result))
        return result
    return clocked # return the inner function to replace the decorated 


def snooze(s):
    time.sleep(s)

snooze = clock(snooze)

snooze(1)