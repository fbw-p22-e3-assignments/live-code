from math import pi

#### Volume #### 
r = 5
volume_sphere = 4/3 * pi * r ** 3
print(volume_sphere)
print(' ')

#### Bookstore ####

book_price = 24.95
discount = 0.4 # 1 - 0.4 = 0.6
shipping_cost_first = 3
shipping_cost_rest = 0.75
number_of_orders = 60

total_shipping_cost = shipping_cost_first + (shipping_cost_rest * (number_of_orders - 1))    
total_cost = (book_price * (1 - discount) * 60 ) + total_shipping_cost
print(total_cost)


#### Back to breakfast

start_time = 6 * 60 + 52 # day in minutes

easy_pace = 8 + 15/60 # pace in minutes

tempo = 7 + 12/60 # tempo pace in minutes

total_time = 2 * easy_pace + 3 * tempo

end_time = start_time + total_time  # breakfast

print('daytime in minutes', end_time)
day_time = end_time / 60 # in hours
# print(day_time)

hours = int(day_time)
# print('daytime in hours', day_time)
# print('hours', hours)
# print('minutes', day_time - hours)
minutes = (day_time - hours) * 60

# print(hours, int(minutes), sep=':')

# print(int(end_time // 60), int(end_time % 60), sep=':')
print(round(end_time // 60), round(end_time % 60), sep=':')



