from datetime import datetime
from datetime import timedelta

def leap_year(year):
    dt = datetime(year, 2, 1)
    dt += timedelta(days=28)
    print(dt)
    if dt.month == 3:
        return False
    return True

print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2018))
