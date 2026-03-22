import random
import datetime
from datetime import timedelta

today = datetime.date.today()

dates = []  
for i in range(10):

    days_ago = random.randint(0, 1825)
    random_date = today - timedelta(days=days_ago)
    dates.append(random_date.strftime("%Y-%m-%d"))

date_objects = []
for date_str in dates:
    date_objects.append(datetime.datetime.strptime(date_str, "%Y-%m-%d").date())

print("Разница между датами:")
for i in range(len(date_objects) - 1):
    date1 = date_objects[i]
    date2 = date_objects[i + 1]
    diff = abs((date2 - date1).days)
    print(f"Разница между {date1} и {date2}: {diff} дней")
