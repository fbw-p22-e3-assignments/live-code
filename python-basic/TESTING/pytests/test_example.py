import pytest

@pytest.mark.skip  # Skip test 
def test_skip_func():
    assert False

controller = None

@pytest.mark.skipif(controller is None, reason='controller give False')
def test_skip_with_con():
    assert True

@pytest.mark.bla_test
def test_method1():
    assert True

@pytest.mark.parametrize('test_input,expected', [(1,1), (2,2)])
def test_method2(test_input, expected):
    print(test_input, expected)
    assert test_input == expected