import unittest #this package is needed for the TestCase superclass
from money import Dollar, Money

class TestMoney(unittest.TestCase):
    #1. FIRST CYCLE
    def test_multiplication(self): 
    #Import add test in front of test's name
        five = Dollar(5)
        tenner = five.times(2)
        self.assertEqual(10, tenner.amount)
        # Comparing actual value with expected value
        # in an assertEqual statement

    # SECOND CYCLE
    def test_multiplication_in_euro(self):
        ten_euros = Money(10, 'EUR')
        twenty_euros = ten_euros.times(2)
        self.assertEqual(20, twenty_euros.amount)
        self.assertEqual("EUR", twenty_euros.currency)
    

if __name__=='__main__':
    unittest.main()