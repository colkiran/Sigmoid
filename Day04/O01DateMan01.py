
from datetime import datetime

dt = datetime.now()
print(f"Current Date and Time :{dt}")

print("-" * 60)
print(f"Day :", dt.strftime("%a"))
print(f"Day :", dt.strftime("%A"))

print("-" * 60)
print(f"Month :", dt.strftime("%b"))
print(f"Month :", dt.strftime("%B"))

print("-" * 60)
print(f"Date :", dt.strftime("%d"))
print(f"Date :", dt.strftime("%D"))
print(f"Date :", dt.strftime("%x"))

print("-" * 60)
print(f"Year :", dt.strftime("%y"))
print(f"Year :", dt.strftime("%Y"))

print("-" * 60)
print(f"Time :", dt.strftime("%T"))
print(f"Time :", dt.strftime("%X"))

print("-" * 60)
dt1 = dt.strftime("%d-%m-%y")
print(f"dt1 :{dt1}")

print("-" * 60)
dt2 = dt.strftime("%d-%m-%Y")
print(f"dt2 :{dt2}")

print("-" * 60)
dt3 = dt.strftime("%d-%b-%Y")
print(f"dt3 :{dt3}")

print("-" * 60)
dt4 = dt.strftime("%d-%B-%Y")
print(f"dt4 :{dt4}")

print("-" * 60)
print(f"dt1 :{type(dt1)}")
print(f"dt2 :{type(dt2)}")
print(f"dt3 :{type(dt2)}")
print(f"dt2 :{type(dt2)}")

