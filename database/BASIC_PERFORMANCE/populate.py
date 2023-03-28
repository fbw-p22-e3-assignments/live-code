import random

numbers = [*range(1,10_001)]

random.shuffle(numbers)

def gen_data(table_name):
    print(f'insert into {table_name} values')
    count = 1
    for i in numbers:
        if count == len(numbers):
            print(f'({i});')
        else:
            print(f'({i}),')
        count += 1

gen_data('tenk1')
gen_data('tenk2')
gen_data('tenk3')