import unittest
from money_live import Money

class TestMoney(unittest.TestCase):
    # FIRST CYCLE OF TDD
    def test_multiplication_in_dollar(self):
        five = Money(5, 'Dollars')
        # tenner_int = five.times(2)
        # tenner = Dollars(tenner_int)
        tenner = five.times(2)
        # return True if 10 == tenner.amount else False
        self.assertEqual(10, tenner.amount)
    
    # SECOND CYCLE OF TDD
    def test_multiplication_in_euro(self):
        ten_euro = Money(10, 'EUR')
        twenty_euros = ten_euro.times(2)
        self.assertEqual(20, twenty_euros.amount)
        self.assertEqual('EUR', twenty_euros.currency)
        self.assertTrue('10', twenty_euros.__repr__())

# unittest.main()