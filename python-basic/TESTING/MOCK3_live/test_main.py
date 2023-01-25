from unittest import mock
from main import greeting

# def test_greeting():
#     assert greeting('bob') == "Hello bob, I'm BOB" 


def test_greeting_with_mock():
    with mock.patch('main.my_module') as mock_my_module:
        mock_my_module.upper.return_value = "BOB"
        # mock_my_module.upper.return_value = "BOB"
        mock_my_module.lower.return_value = "bob"
        assert greeting('bob') == "Hello bob, I'm BOB"
        
    # greeting('bob')
        # assert False