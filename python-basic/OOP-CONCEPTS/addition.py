import itertools

class Vector:
    def __init__(self, components):   
        self._components = components

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        return str(tuple(self))


    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0)
        return Vector(a + b for a,b in pairs)

    def __radd__(self, other):
        print('BLA')
        # return self + other  #just delegates to __add__

v1 = Vector(range(1,4))
print((1,2) + v1)