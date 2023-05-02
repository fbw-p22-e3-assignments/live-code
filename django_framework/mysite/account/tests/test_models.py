from django.test import TestCase

class TestPostModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("SetUpTestData")
        pass
    
    def setUp(self):
        print("Run once for every test method")
        pass
    
    def test_false_is_false(self):
        print("It actually is false")
        self.assertFalse(False)
        
    def test_one_plus_one_is_true(self):
        print("1 + 1 = 2")
        self.assertTrue(1 + 1, 2)
        