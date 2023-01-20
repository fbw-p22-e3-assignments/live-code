
from money_live import Dollar, Money

#5 Dollars * 2 = 10 Dollars
def test_multiplication():
    five = Dollar(5)
    tenner = five.times(2)
    assert 10 == tenner.amount

def test_multiplication_in_euro():
    ten_euro = Money(10, 'EUR')
    twenty_euros = ten_euro.times(2)
    print(str(twenty_euros))
    assert 20 == twenty_euros.amount
    assert 'EUR' == twenty_euros.currency
    assert '20' == str(twenty_euros)
    