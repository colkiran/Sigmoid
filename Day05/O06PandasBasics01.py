
import pandas as pd

print(f"Version :{pd.__version__}")

mycars = {
    'cars': ['Audi', "BMW", 'Mercedes'],
    'safety_rating': [9.2, 9.0, 9.7]
}

mydf = pd.DataFrame(mycars)

print("-" * 60)
print(f"mydf :\n{mydf}")

print("-" * 60)

print(type(mydf))
