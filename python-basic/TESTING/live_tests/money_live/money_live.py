class Dollar:
    def __init__(self, value):
        self.amount = value

    def times(self, num):
        return Dollar(num * self.amount) #Dollar
        # return num * self.amount  #Interger

    def __repr__(self):
        return self.amount 

class Money:
    def __init__(self, value, currency):
        self.amount = value
        self.currency = currency

    def times(self, num):
        return Money(num * self.amount, self.currency) 

    def __repr__(self):
        return str(self.amount) 
    