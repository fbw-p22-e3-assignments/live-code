class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self._instance = self
        self.name = name





# x = Singleton('x')
# y = Singleton('y')
# print(x.name)
# print(y.name)

class Warehoues:
    _instance = None
    def __init__(self):
        self.emploees = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __str__(self):
        return f"Number of employees: {self.emploees}"

# w = Warehoues()
# w2 = Warehoues()
# print(w)
# print(w2)
# print(w is w2)
print(Warehoues.__mro__)

