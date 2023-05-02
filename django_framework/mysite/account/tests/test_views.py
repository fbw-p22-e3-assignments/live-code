from django.test import TestCase

class TestPostModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("SetUpTestData for views")
        pass
    
    def setUp(self):
        print("Run once for every test method for views")
        pass
    
    def test_false_is_false(self):
        print("It actually is false in views")
        self.assertFalse(False)
        
    def test_one_plus_one_is_true(self):
        print("1 + 1 = 2, in views")
        self.assertEqual(1 + 1, 2)