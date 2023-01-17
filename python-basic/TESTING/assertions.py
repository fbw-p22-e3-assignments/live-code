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

import unittest

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.test = MethodsToTest()
    def test_method1(self):
        self.assertTrue(self.test.method1())
    def test_method2(self):
        self.assertFalse(self.test.method2())
    def test_method3(self):
        self.assertEqual(self.test.method3(), 'BLA')
    def test_method3b(self):
        self.assertNotEqual(self.test.method3(), 'Hello')
    def test_method4(self):
        with self.assertRaises(KeyError):
            self.test.method4()
    def test_method5(self):
        with self.assertRaises(TypeError):
            self.test.method5()

if __name__ == '__main__':
    unittest.main()
