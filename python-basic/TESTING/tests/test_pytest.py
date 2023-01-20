class MethodsToTest:
    def method1(self):
        return True
    def method2(self):
        return False
    def method3(self):
        return 'BLA'
    def method4(self):
        d = {'a': 1, 'b': 2}
        d['c'] #KeyError
    def method5(self):
        set() + 1 #TypeError

import pytest

my_lib = None

test = MethodsToTest()
# @pytest.mark.skip('Do not run this')
def test_methods1():
    assert test.method1()
# @pytest.mark.skipif(my_lib is None, reason='mylib is not available')
def test_methods2():
    assert not test.method2()
def test_methods3():
    assert test.method3() == 'BLA'
    pytest.skip('Will not run')
@pytest.mark.bla_test
def test_methods4():
    assert test.method3() != 'BLA1'
def test_methods5():
    assert test.method3() in 'BLA1'
def test_methods5():
    with pytest.raises(KeyError):
        test.method4() 
def test_methods6():
    with pytest.raises(TypeError):
        test.method5() 
    