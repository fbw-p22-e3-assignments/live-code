from delete import rm
from unittest import mock

@mock.patch('delete.os')
def test_rm(mock_os):
    mock_os.path.isfile.return_value = True
    rm('foo')

    # assert mock_os.remove.call_count == 2
    # assert mock_os.path.isfile.call_count == 1
    mock_os.remove.assert_called_with('foo')

def test_rm2():
    with mock.patch('delete.os') as mock_os:
        mock_os.path.isfile.return_value = True
        rm('foo')
        mock_os.remove.assert_called_with('foo')

class TestDelete:
    @mock.patch('delete.os')
    def test_rm(self, mock_os):
        mock_os.path.isfile.return_value = True
        rm('foo')
        mock_os.remove.assert_called_with('foo')

    def test_rm2(self):
        with mock.patch('delete.os') as mock_os:
            mock_os.path.isfile.return_value = True
            rm('foo')
            mock_os.remove.assert_called_with('foo')


