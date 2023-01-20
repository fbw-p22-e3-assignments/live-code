class Dollar:
    def __init__(self, num):
        self.amount = num
        

    def times(self, factor):
        return Dollar(factor * self.amount)

class Money:
    def __init__(self, num, currency) -> None:
        self.amount = num
        self.currency = currency

    def times(self, factor):
        return Money(factor * self.amount, self.currency)

    def divide(self, value):
        return Money(self.amount / value, self.currency)