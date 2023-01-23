from delete import rm
from unittest import mock

@mock.patch('delete.os')
def test_rm(mock_os):
    rm('foo')
    rm('foo')
    assert mock_os.remove.call_count == 2
    # assert dir(mock_os.remove) == ['call_with']
    # assert  str(mock_os.remove.call_args_list) == "('foo')"
    mock_os.remove.assert_called_with('foo')
    # mock_os.remove.reset_mock()
    # mock_os.remove.assert_called_with('foo')


