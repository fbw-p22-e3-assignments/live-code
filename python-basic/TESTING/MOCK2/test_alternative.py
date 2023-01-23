from unittest import mock
import unittest
from delete import rm
import os


class RmTestCase(unittest.TestCase):

    def test_rm(self):
        with mock.patch('delete.os') as mock_os:
            # mock_os.remove.side_effect = lambda x: f"rm {x}"
            print(rm('somefile.txt'))
            # print(rm('somefile.txt'))
            assert mock_os.remove.call_count == 1
            mock_os.remove.assert_called_with('somefile.txt')

