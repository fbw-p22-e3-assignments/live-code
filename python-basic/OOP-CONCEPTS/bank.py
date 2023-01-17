class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount} deposited!')
            return True
        else:
            print('Error! Deposited amount must be positive!')
            return False

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            print(f'{amount} withdrawn!')
            return True
        else:
            print('Not Enough Balance or amount is negative!')
            return False


class SavingsAccount(BankAccount):
    def __init__(self, acc_num, balance, rate):
        super().__init__(acc_num, balance)
        self.interest_rate = rate

    def next_month(self):
        self.balance += (self.balance * self.interest_rate)
        print("Interest added")

    def __str__(self):
        return f"Account number: {self.acc_num}\n" \
               f"Interest rate: {self.interest_rate}\n" \
               f"Balance: {self.balance:.2f}"


class CheckingAccount(BankAccount):
    def __init__(self, acc_num, balance, no_transaction):
        super().__init__(acc_num, balance)
        self.no_transaction = no_transaction     # number of allowed transaction in a month
        self.transaction_count = 0            # transaction count

    def _utility(self, func, amount):
        if self.transaction_count < self.no_transaction:
            if func(amount):
                self.transaction_count += 1
        else:
            print('Error, Transactions Limit reached!')

    def deposit(self, amount):
        self._utility(super().deposit, amount)

    def withdraw(self, amount):
        self._utility(super().withdraw, amount)

    def next_month(self):
        self.transaction_count = 0
        print("Transaction count resetted")

    def __str__(self):
        return f"Account number: {self.acc_num}\n" \
               f"Max monthly transactions: {self.no_transaction}\n" \
               f"Current month transactions: {self.transaction_count}\n" \
               f"Balance: {self.balance:.2f}"

if __name__ == '__main__':
    acc2 = CheckingAccount(123456, 1000, 2)
    acc2.deposit(100)
    acc2.withdraw(200)
    acc2.deposit(100)
    acc2.deposit(100)
    acc2.deposit(100)
    print(acc2)



