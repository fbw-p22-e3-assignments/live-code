def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        print(series)
        total = sum(series)
        return total / len(series)
    return averager

# avg = make_averager()
# print(make_averager()(10))
# print(avg(11))
# print(avg(12))
# print(avg(13))
# print(avg(13))

def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        nonlocal count, total
        count = count + 1
        total = total + new_value
        return total / count
    return averager
    
avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(13))
