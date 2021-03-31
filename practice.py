from datetime import date
import datetime
import calendar

year =  date.today().year
month = date.today().month
dt= date(year,month,1)
first_week = dt.isoweekday()
saturday4 = 28-first_week
dt=date(year,month,saturday4)
print(dt.year,dt.month,dt.day)

def findDay(date):
    born = datetime.datetime.strptime(date,'%Y%m%d').weekday()
    return (calendar.day_name[born])

date = '20210330'
print(findDay(date))

if 20210330%5 ==0:
    print(date)
