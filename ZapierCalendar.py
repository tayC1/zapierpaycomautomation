import calendar 
from datetime import datetime, timedelta

today = datetime.today()
weekday = today.weekday() #monday = 0, Sunday = 6

#find last day of month 
last_day = calendar.monthrange(today.year, today.month)[1]
last_day_date = datetime(today.year, today.month, last_day)
last_day_weekday = last_day_date.weekday()

#adjust if weekend 
if last_day_weekday >=5: 
    offset = last_day_weekday - 4 #sends back to Friday 
    last_workday = last_day_date -timedelta(days=offset)
else:
    last_workday = last_day_date    

#same for the fifteenth

fifteenth = datetime(today.year, today.month, 15)
fifteenth_weekday = fifteenth.weekday()

if fifteenth_weekday >=5:
    offset = fifteenth_weekday -4 #will send back to Friday 
    fifteenth_workday = fifteenth-timedelta(days=offset)
else:
    fifteenth_workday = fifteenth

#check if period matches either 
is_last_day_of_period = today.date()==last_workday.date() or today.date() == fifteenth_workday.date()

output ={'run_zap': is_last_day_of_period} 