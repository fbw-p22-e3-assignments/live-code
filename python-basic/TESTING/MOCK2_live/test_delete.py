from delete2 import rm
from unittest import mock

def test_rm():
   with mock.patch('delete2.os') as mock_os:
    mock_os.path.isfile.return_value = True
    rm('foo')
    mock_os.remove.assert_called_with('foo') 
    # assert False