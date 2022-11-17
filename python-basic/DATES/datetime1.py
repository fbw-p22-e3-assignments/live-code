import datetime

dt = datetime.datetime.now()

# from datetime import datetime

# dt = datetime.now()

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta)
# print(delta.total_seconds())

datetime_string = "Oct 21, 2019"
dt = datetime.datetime.strptime(datetime_string, '%b %d, %Y')
# print(type(dt))
# print(type(dt.strftime('%m %Y %d')))