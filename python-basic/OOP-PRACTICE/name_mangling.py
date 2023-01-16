class Test:
    def __init__(self):
        self.__number = 0
    def __neg__(self):
        pass


instance = Test()
print(instance._Test__number)
print(-instance)


