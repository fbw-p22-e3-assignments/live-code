class BricksAndWaterPython:
    def __init__(self) -> None:
        pass

    def how_much_water(self, towers: list) -> int:

        N = len(towers)

        left = [max(towers[:n]) for n in range(1, N + 1)]
        right= [max(towers[n:]) for n in range(0, N )]
        print(left)
        print(right)
        print(towers)

        sum_of_water = 0
        for i in range(0, len(towers)-1):
            sum_of_water += min(left[i], right[i]) - towers[i]
        
        return sum_of_water


results = BricksAndWaterPython()

print(results.how_much_water([2, 6, 3, 5, 2, 8, 1, 4, 2, 2, 5, 3, 5, 7, 4, 1]))