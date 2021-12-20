import datetime

t=datetime.time(22,56,44)
print(t)
print("Hour : ", t.hour)
print("Minute : ", t.minute)
print("Second : ", t.second)

print("==============================")

d = datetime.date.today()
print(d)
td = datetime.timedelta(days=2)
print(td)

d2 = d+td
print("After adding two days :",d2)
print("d2-d",d2-d)
print("d2>d",d2>d)

d1 = datetime.date.today()
t1 = datetime.time(12,44,56)
print("Date and Time : ",d1, t1)
