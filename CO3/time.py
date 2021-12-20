import time

print("Current time in sec : ",time.time())
print("Current time : ",time.ctime())
print("Current time after 30 sec : ",time.time()+30)
t = time.localtime()
print("Time : ", t)
print("Current Year :", t.tm_year)
print("Current Month :", t.tm_mon)
print("Current Day :", t.tm_mday)
print("Current Hour :", t.tm_hour)
print("Current Weekday :", t.tm_wday)
print("Day of year :", t.tm_yday)
