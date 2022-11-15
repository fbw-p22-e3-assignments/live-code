from typing import Optional
from typing import Union

def show_count(count: int, singular:str, plural: Union[str, None]=None ) -> str :
    if count == 1:
        return f"1 {singular}"
    # count_str = str(count) if count else 'no' #####shorthand if else notation
    #count_str = str(count) if count > 0 else 'no'
    #count_str ='no' if count == 0 else str(count)
    if count == 0:
        count_str = 'no'
    else:
        count_str = str(count)
    if plural:
        return f"{count_str} {plural}"
    return f"{count_str} {singular}s"

print(show_count(2, 'child', 'children'))
print(show_count(1, 'child', 'children'))
print(show_count(3, 'child'))
print(show_count(0, 'child', 'children'))

def parse_token(token: str) -> Union[str, int]:
    if token.isnumeric():
        return int(token)
    return token


def double(x: int) -> int:
    return x * 2

print((double(1+1j)))
