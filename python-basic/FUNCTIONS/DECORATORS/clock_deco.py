import time

def clock(fun):
    def clocked():      ####inner function
        t0 = time.time()
        result = fun()  ### fun is the free variable of the closure
        elapsed = time.time() - t0
        print("{elapsed}s func --> {result}".format(elapsed=elapsed, result=result))
        return result
    return clocked # return the inner function to replace the decorated function

def snooze():
    return 'Hello'

snooze = clock(snooze)

snooze()

@clock
def snooze():
    return 'Hello'

snooze()