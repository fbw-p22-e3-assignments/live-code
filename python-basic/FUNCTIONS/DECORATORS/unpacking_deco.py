def decorate(func):
            def inner(*args, w3):
                #print(args)
                # print(w3)
                return f'deco {func(*args)}'
            return inner

@decorate
def test(w1, w2, w3='bla'):
    return w1 + ' ' + w2 + ' ' + w3

print(test('hello', 'world', w3='again'))  ## inner('hello', 'world', we)

# def inner(*args, w3):
#     # print(args)
#     # print(w3)
#     return f'deco {(args)}'
