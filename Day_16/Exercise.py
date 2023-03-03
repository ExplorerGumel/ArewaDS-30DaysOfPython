## 1
# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
today = datetime.now()
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
timestamps = today.timestamp()

print('today is:',today, '\n', 'Day:',day,'\n','Month:',month,'\n','Year:', year)

## 2
#Format the current date using this format: "%m/%d/%Y, %H:%M:%S") 
format_today = today.strftime('%m/%d/%Y, %H:%M:%S')
print(format_today)

## 3
#Today is 5 December, 2019. Change this time string to time.
today = '5 December, 2019'
to_date = datetime.strptime(today, '%d %B, %Y')
print(to_date)

## 4
# Calculate the time difference between now and new year.

today = datetime(year = 2023, month = 2, day = 24)
new_year = datetime(year = 2024, month = 12,day=31)
difference = new_year - today
print(difference)

# 5
## Calculate the time difference between 1 January 1970 and now.
now = datetime(year = 2023, month = 2, day = 24)
given = datetime(year = 1970, month = 1, day=1)

difference = now - given
print(difference)