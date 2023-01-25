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

# @pytest.mark.parametrize('test_input,expected', [(1,1), (2,2)])
@pytest.mark.parametrize('test_input', [1])
def test_method2(test_input):
    print(test_input)
    assert test_input == 'test_input'