
from datetime import datetime

import dateutils
import timeutils

login_time = datetime.strptime("9:32:56", "%H:%M:%S")
logout_time = datetime.strptime("18:45:25", "%H:%M:%S")

print(f"login time :{login_time}")
print(type(login_time))

print("-" * 60)
print(f"logout time :{logout_time}")
print(type(logout_time))

print("-" * 60)
print(f"Difference in minutes :{round(dateutils.minutes(logout_time, login_time), 2)}")

print("-" * 60)
print(f"Difference in hours :{round(dateutils.hours(logout_time, login_time), 2)}")

print("-" * 60)
print(f"Difference in seconds :{round(dateutils.seconds(logout_time, login_time), 2)}")