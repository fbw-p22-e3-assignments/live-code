import timeit

my_results = timeit.repeat(setup = '',
             stmt = 'list(range(1000)) ',
             repeat = 3,
             number = 1000)

print(my_results)