from delete import rm
from unittest import mock

def myPatchWrapper(module_to_patch):
    def myPatch(func):
            def inner():
                with mock.patch(module_to_patch) as mock_os:
                    func(mock_os)
            return inner
    return myPatch

@myPatchWrapper('delete.os')
def test_rm(mock_os):
    mock_os.path.isfile.return_value = 0
    rm('foo')
    mock_os.remove.assert_called_with('foo')
