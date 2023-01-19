class MethodsToTest:
    def __init__(self) -> None:
        pass
    def method1(self):
        return True
    def method2(self):
        return False
    def method3(self):
        return 'BLA'
    def method4(self):
        d = {'a':1, 'b':2}
        d['c']  #KeyError
    def method5(self):
        set() + 1 #TypeError 


import unittest

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.test = MethodsToTest()
    
    def test_method1(self):
        self.assertTrue(self.test.method1(), 'TEST FAILED')

    def test_method2(self):
        self.assertFalse(self.test.method2())
    
    def test_method3(self):
        self.assertNotEqual(self.test.method3(), 'BLA1', 'FAIL:IS EQUAL')

    def test_method4(self):
        self.assertIn(self.test.method3(), 'BLA1', 'FAIL:A is not in B')

    def test_method5(self):
        if self.test.method3() == 'BLA':
            pass
        else:
            self.fail('FAILED')

    def test_method6(self):
        with self.assertRaises(KeyError):
            self.test.method4()

    def test_method7(self):
        with self.assertRaises(TypeError):
            self.test.method5()

if __name__ == '__main__':
    unittest.main()