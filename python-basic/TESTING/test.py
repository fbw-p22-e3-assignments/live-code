a = {
    'a': 1,
    'b': 2,
    'c': 3,
        }

b = [1,2, {'c':2}]

# print(a.get('e'))
# print(a.get('e', 80))
# print(b[len(b)])

class A:
    def __init__(self, name):
        print('From class A')
        self.name = name

class B(A):
    def __repr__(self):
        return f"{self.name}"
    def __str__(self):
        return f"bla"

b = B('test')
# print(B.mro())
print(b)


