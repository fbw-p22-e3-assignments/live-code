from delete import rm 
from unittest import mock

# @mock.patch('delete.os')
# def test_rm(mock_os):
#     rm('foo')
#     assert mock_os.remove.call_count == 1
#     mock_os.remove.assert_called_with("foo")

def test_rm():
    with mock.patch('delete.os') as mock_os:
        rm('foo')
        assert mock_os.remove.call_count == 1
        mock_os.remove.assert_called_with("foo")