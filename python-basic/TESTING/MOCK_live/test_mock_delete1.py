import unittest
from unittest import mock
from delete import rm
import os

class RmTestCase(unittest.TestCase):

    # @mock.patch('delete.os')
    @mock.patch('delete.os')
    def test_rm(self, mock_os):
        #try to delete
        rm('somefile.txt')
        rm('somefile.txt')
        mock_os.remove.assert_called_with("somefile.txt")
        # self.assertEqual(mock_os.remove.call_count,2)
        assert mock_os.remove.call_count == 2


if __name__=='__main__':
    import delete
    import os
    print(os)
    print(delete.os)