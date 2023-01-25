from main import len_joke, get_joke

from unittest.mock import patch, MagicMock

@patch('main.get_joke')
def test_len(mock_get_jokes):
    mock_get_jokes.return_value = 'test'
    assert len_joke() == 4

@patch('main.requests')
def test_get_joke(mock_requests):
    mock_requests.get.return_value.status_code = 200
    mock_requests.get.return_value.json.return_value = {'value': {'joke':'test'}}
    get_joke()
    print('MOCK FROM TEST',mock_requests.get())
    print(dir(mock_requests.get))
    # assert get_joke() == 'test'
    assert False

@patch('main.requests')
def test_get_joke2(mock_requests):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'value': {'joke':'test'}}
    mock_requests.get.return_value = mock_response
    assert get_joke() == 'test'


    

