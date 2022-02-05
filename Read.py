from csv_ical import Convert
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from Main import *

g = open('schedule.ics','rb')

cal = Veronica('9:00:00', "17:30:00")
def calc_duration(start, end): 
    return end - start

gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        event = component.get('summary')
        description = component.get('description')
        location = component.get('location')
        start = component.get('dtstart').dt
        end = component.get('dtend').dt
        print(str(start) + ',' + str(end))
        timezone = component.get('dtstamp').dt
        until = component.get('rrule')['UNTIL']
        byDay = component.get('rrule')['BYDAY']
        duration = calc_duration(start, end)
        preferance_list = []
        isFlexible = False
        rec_perday = 0
        cal.add_task(event, description, duration, byDay, rec_perday, preferance_list, isFlexible, location, timezone, start, end )
        
        # print(duration)


# let's create random flex tasks: 
# task: gym
tzone = '20220205T044210Z'
cal.add_task("gym", "get ripped", "2:0:0", ["Mo", "Tu", "We"], 1, [('8:30:00', '9:30:00')], True, "gym", "")
cal.add_task("Eat", "Stay Alive", "3:0:0", ["Mo", "Tu", "We"], 3, [('8:30:00', '9:30:00')], True, "gym", "")

# print(cal.get_task("flex"))
# print(cal.get_task("inflex"))
# print()
# for elem in cal.get_task("inflex"): 
#     print(elem)
#     print()

print(cal.get_len_tasks("flex"))
g.close()

