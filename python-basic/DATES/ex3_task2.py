from datetime import datetime
from dateutil import tz

moscow = tz.gettz('Europe/Moscow')
dublin = tz.gettz('Europe/Dublin')
san_francisco = tz.gettz('America/Los_Angeles')
berlin = tz.gettz('Europe/Berlin')
johannesburg = tz.gettz('Africa/Johannesburg')

moscow_meeting = datetime(2021, 8, 7, 13, 35, tzinfo=moscow) 

# from dateutil import parser
# tzinfos = {"MSK": tz.gettz('Europe/Moscow')}
# moscow_meeting = parser.parse("2021-08-07 13:35 MSK", tzinfos=tzinfos)


def getTime(date, tz):
    country = (tz.__str__()).split('/')[-1][:-2]
    return f"{country} participants will meet at: {date.astimezone(tz)}" 

print(getTime(moscow_meeting, dublin))
print(getTime(moscow_meeting, berlin))
print(getTime(moscow_meeting, johannesburg))
print(getTime(moscow_meeting, san_francisco))
print(getTime(moscow_meeting, moscow))

