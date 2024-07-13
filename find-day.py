import datetime

date_str = input("Enter date (YYYY-MM-DD): ")
year, month, day = map(int, date_str.split('-'))

d = datetime.date(year, month, day)
print("Day is:", d.strftime("%A"))
