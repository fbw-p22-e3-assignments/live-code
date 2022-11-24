def decorator(func):
    def inner(n):
        return f"<p>{func(n)}</p>"
    return inner

@decorator
def getName(name):
    return name

print(getName('John'))


def decorator(func):
    def inner(*args):
        return f"<p>{func(*args)}</p>"
    return inner

@decorator
def getName(name):
    return name

print(getName('John'))