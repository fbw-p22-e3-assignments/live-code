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

        temp = towers[0]
        left = list([temp])
        for i in range(1, len(towers)):
            if towers[i] > temp: 
                temp = towers[i]
                left.append(temp)
            else: left.append(temp)

        reversed_towers = list(reversed(towers)) 
        temp = reversed_towers[0]
        right = list([temp])
        for i in range(1, len(towers)):
            if reversed_towers[i] > temp: 
                temp = reversed_towers[i]
                right.append(temp)
            else: right.append(temp)
        right = list(reversed(right))



        # temp = towers[-1]
        # right = list([temp])
        # for i in range(len(towers) -2 , -1, -1):
        #     if towers[i] > temp:
        #         temp = towers[i]
        #         right.insert(0, temp)
        #     else: 
        #         right.insert(0, temp)


        sum_of_water = 0



        print(left)
        print(right)
        print(towers)

        for i in range(0, len(towers)-1):
            sum_of_water += min(left[i], right[i]) - towers[i]
        
        return sum_of_water


results = BricksAndWaterPython()

print(results.how_much_water([1, 5, 3, 7, 2]))