import random

numbers = [*range(1,10_001)]

random.shuffle(numbers)

print('insert into tenk1 values')
count = 1
for i in numbers:
    if count == len(numbers):
        print(f'({i});')
    else:
        print(f'({i}),')
    count += 1
