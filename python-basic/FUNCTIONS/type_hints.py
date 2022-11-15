

def show_count(count:int, singular:str, plural: str = '') ->str:
    if count == 1:
        return f"1 {singular}"
    count_str = str(count) if count else 'no'
    if plural:
        return f"{count} {plural}"
    return f"{count_str} {singular}s"

print(show_count(99, 'bird'))
print(show_count(1, 'bird'))
print(show_count(0, 'bird'))

print(show_count(2, 'child', 'children'))
print(show_count(1, 'child', 'children'))
print(show_count(0, 'child', 'children'))


# def double(x: dict)->int:
#     return x * 2


# print(double({1: 'bla'}))

from typing import Union
def parse_token(token: str) -> float:
    if token.isnumeric():
        return int(token)
    return 2.2

print(parse_token('123'))
print(parse_token('abc'))