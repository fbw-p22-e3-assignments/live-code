# import unittest
# from BLA import rm

#WITHOUT MOCK
# class RmTestCase(unittest.TestCase):
#     def test_rm(self):
#         # create a file
#         open('somefile.txt', 'a')
#         # try to delete it
#         rm('somefile.txt')
#         # check file if still exist
#         self.assertFalse(os.path.isfile('./somefile.txt'), 'failed to remove the file')

from delete import rm
from unittest import mock
import unittest
#WITH MOCK
class RmTestCase(unittest.TestCase):

    @mock.patch('delete.os')
    def test_rm(self, mock_os):
        # rm('somefile.txt')
        self.assertTrue(mock_os.remove.call_count)
        # mock_os.remove.assert_called_with("somefile.txt")

if __name__ == '__main__':
    unittest.main()
