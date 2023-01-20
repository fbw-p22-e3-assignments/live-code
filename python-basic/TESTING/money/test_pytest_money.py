from money import Dollar, Money

# def test_multiplication():
#     five = Dollar(5)
#     tenner = five.times(2)
#     assert 10 == tenner.amount

#CHANGE TO:
def test_multiplication_in_dollar():
    five = Money(5, 'USD')
    tenner = five.times(2)
    assert 10 == tenner.amount


def test_multiplication_in_euro():
    ten_euros = Money(10, 'EUR')
    twenty_euros = ten_euros.times(2)
    assert 20 == twenty_euros.amount
    assert "EUR" == twenty_euros.currency
    
# 20 pound / 4 = 5

def test_divsion():
    original_money = Money(20, 'pound')
    actual = original_money.divide(4)
    expected = Money(5, 'pound')
    assert actual.amount == expected.amount
    assert actual.currency == expected.currency