from unittest import mock
from my_main import greeting

def test_greeting_returns_upper_str():
    assert greeting('bob') == f"Hello bob,I'm BOB"

def test_greeting_with_mock():
    with mock.patch('my_main.my_module') as mock_my_main:
        mock_my_main.upper.return_value = 'Doe'
        assert greeting('bob') == f"Hello bob,I'm Doe"
        mock_my_main.upper.assert_called_once
        mock_my_main.upper.assert_called_with('bob')
