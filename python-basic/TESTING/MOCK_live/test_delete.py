import unittest
import os
from delete import rm

class RmTestCase(unittest.TestCase):
    def test_rm(self):
        #create a file
        open('somefile.txt', 'a')
        #try to delete
        rm('somefile.txt')
        file_exists = os.path.isfile('./somefile.txt')
        self.assertFalse(file_exists, 'failed to remove the file')

if __name__ == '__main__':
    unittest.main()
