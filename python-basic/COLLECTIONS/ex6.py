numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]

def mean(lists):
    return [sum(sub_list) / len(sub_list) for sub_list in lists]

print(mean(numbers))

def mean(input):
  column_mean = [sum(number) / len(number) for number in input]
  return str(sum(column_mean) / len(column_mean))

print(mean([[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]))
