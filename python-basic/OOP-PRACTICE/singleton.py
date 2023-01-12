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
    def __init__(self):
        self._instance = self
        self.emploees = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Warehoues, cls).__new__(cls)
        cls._instance.emploees += 1
        return cls._instance

    def __str__(self):
        return f"Number of employees: {self.emploees}"

w = Warehoues()
w2 = Warehoues()
print(w)
print(w2)

