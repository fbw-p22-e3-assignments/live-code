import unittest
from unittest import mock
from delete import rm


class RmTestCase(unittest.TestCase):

    def test_rm(self):
        with mock.patch('delete.os') as mock_os:
            rm('somefile.txt')
            mock_os.remove.assert_called_with("somefile.txt")