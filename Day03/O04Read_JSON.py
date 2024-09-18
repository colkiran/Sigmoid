import json
JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile)

for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("-" * 60)
empdata = '{"name" :"Mike", "age": 34, "desig": "MGR", "City": "Hyderabad"}'
print(empdata)
print(type(empdata))

res = json.loads(empdata)
print(res)

for k, v in res.items():
    print(k, "=>", v)
