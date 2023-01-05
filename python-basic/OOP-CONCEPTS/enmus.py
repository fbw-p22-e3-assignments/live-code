from enum import Enum
from datetime import datetime

class Weekday(Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6

    @classmethod
    def from_date(cls, date):
        return cls(datetime.weekday())

Weekday(1)

Weekday.MON

Weekday['MON']

Weekday.MON.value

Weekday.from_date(datetime.now())
