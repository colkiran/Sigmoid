
import time
from datetime import datetime
import pytz

curtime = time.localtime()
print(f"curtime :{curtime}")
print("Time is :", time.strftime("%H : %M :%S", curtime))

print("-" * 60)
tm1 = "9:32:56"
tm2 = "18:45:10"

print(f"tm1 :{tm1}")
print(type(tm1))

print("-" * 60)
print(f"tm2 :{tm2}")
print(type(tm2))

print("-" * 60)
time01 = datetime.strptime(tm1, "%H:%M:%S")
print(f"Login time :{time01}")
print(type(time01))

print("-" * 60)
time02 = datetime.strptime(tm2, "%H:%M:%S")
print(f"Logoff time :{time02}")
print(type(time02))

res = time02 - time01
print(f"res :{res}")

