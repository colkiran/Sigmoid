"""
utc - universal time coordinates

"""
from datetime import datetime
import pytz
import time

curtime = time.localtime()
curclock = time.strftime("%H:%M:%S", curtime)
print(curclock)

print("-" * 60)
utc = pytz.utc
print(f"utc :{utc}")

print("-" * 60)
IST = pytz.timezone('Asia/Kolkata')
print(F"ist :{IST}")

print("-" * 60)
print("utc default format :", datetime.now(utc))

print("-" * 60)
print("ist default format :", datetime.now(IST))

print("-" * 60)
IST = pytz.timezone("Asia/Kolkata")
NYT = pytz.timezone("America/New_York")
UKT = pytz.timezone("Europe/London")
AST = pytz.timezone("Australia/Melbourne")

print("-" * 60)
print("Indian Time          :", datetime.now(IST))
print("American Time        :", datetime.now(NYT))
print("United Kingdom Time  :", datetime.now(UKT))
print("Australian Time      :", datetime.now(AST))


