from unittest import mock

import pytest
import requests


def get_python():
    r = requests.get("https://python.org")
    if r.status_code == 200:
        return 'Python' in r.text
    else:
        raise Exception("Wrong status code")

def test_get_python_with_valid_status_code():
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Python is wicked awesome!'
        get_python()
        assert mock_get.called
        assert mock_get.called_once
        # assert get_python() == True
        assert mock_get.call_count
        # assert mock_get.call_args == mock.call('https://python.org')
        # assert mock_get.call_args_list == [mock.call('https://python.org')]
        mock_get.assert_called_once_with('https://python.org')

def test_get_false_python_with_valid_status_code():
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'NOPE'
        assert not get_python() 
        assert mock_get.call_count == 1
        mock_get.assert_called_once_with('https://python.org')
        
def test_get_python_with_invalid_status_code():
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        with pytest.raises(Exception):
            get_python()
        assert mock_get.call_count == 1
        mock_get.assert_called_once_with('https://python.org')



if __name__ == "__main__":
    print(get_python())
