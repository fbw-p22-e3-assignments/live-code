swap_list = [23, 65, 19, 90]

def swap(arr, x,y):
    arr[x-1], arr[y-1] = arr[y-1], arr[x-1]
    return arr

print(swap(swap_list, 1, 3))
