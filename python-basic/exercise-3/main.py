class BricksAndWaterPython:
    def __init__(self) -> None:
        pass

    def how_much_water(self, towers: list) -> int:

        def get_border(items):
            temp = items[0]
            side = [temp]
            for i in range(1, len(items)):
                if items[i] > temp: 
                    temp = items[i]
                    side.append(temp)
                else: side.append(temp)
            return side

        left = get_border(towers)
        right = get_border(list(reversed(towers)))
        right = list(reversed(right))

        sum_of_water = 0

        print(left)
        print(right)
        print(towers)

        for i in range(0, len(towers)-1):
            sum_of_water += min(left[i], right[i]) - towers[i]
        
        return sum_of_water


results = BricksAndWaterPython()

print(results.how_much_water([1, 5, 3, 7, 2]))