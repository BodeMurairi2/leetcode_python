#!/usr/bin/python3
import datetime
import time

date = datetime.date.today()
now_time = time.time()
print(date)
print(now_time)
after_time = time.time()

start_time = input("Enter time in HH:MM")
end_time = input("Enter time in HH:MM")
time_start = datetime.datetime.strptime(start_time, "%H:%M")
time_end = datetime.datetime.strptime(end_time, "%H:%M")
print(start_time)
print(time_start)