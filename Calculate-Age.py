import time
from calendar import isleap

def judge_leap_year(year):
    return isleap(year)

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year else 28

name = input("input your name: ")
age = int(input("input your age: "))

localtime = time.localtime()

year = age
month = year * 12 + localtime.tm_mon

begin_year = localtime.tm_year - year
day = 0

for y in range(begin_year, localtime.tm_year):
    day += 366 if judge_leap_year(y) else 365

leap_year = judge_leap_year(localtime.tm_year)

for m in range(1, localtime.tm_mon):
    day += month_days(m, leap_year)

day += localtime.tm_mday

print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
