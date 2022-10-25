from main import BricksAndWaterPython

results = BricksAndWaterPython()

def res(arr):
    return results.how_much_water(arr)

def test1():
    assert res([1,5,3,7,2]) == 2

def test2():
    assert res([5, 3, 7, 2, 6, 4, 5, 9, 1, 2]) == 14
    assert res([2, 6, 3, 5, 2, 8, 1, 4, 2, 2, 5, 3, 5, 7, 4, 1]) == 35
    assert res([5, 5, 5, 5]) == 0
    assert res([5, 6, 7, 8]) == 0
    assert res([8, 7, 7, 6]) == 0
    assert res([6, 7, 10, 7, 6]) == 0

