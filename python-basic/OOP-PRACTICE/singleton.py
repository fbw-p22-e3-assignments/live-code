class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self._instance = self
        self.name = name





x = Singleton('x')
y = Singleton('y')
print(x.name)
print(y.name)

