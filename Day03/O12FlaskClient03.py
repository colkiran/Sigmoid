
import json
import requests

print("get".center(60, "-"))

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/pepsi")

res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("=" * 60)

print("put".center(60, "-"))
response = requests.put(BASE + "getproduct/coke", data= {'cat': "beverage"})
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print('=' * 60)
print("patch".center(60, "-"))
data = {"price": 5000}
response = requests.patch(BASE + "getproduct/coke", json=json.dumps(data))
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("=" * 60)

print("post".center(60, "-"))
fanta = {"item": '150 ml bottle', "price": 20, "qty": 300}

response = requests.post(BASE + "getproduct/fanta", json = json.dumps(fanta))
res = response.json()

for ky, info in res.items():
    print(str(ky).upper())
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("=" * 60)
print("delete".center(60, "-"))

response = requests.delete(BASE + "getproduct/thumbs_up")
res = response.json()

for ky, info in res.items():
    print(str(ky).upper())
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)


