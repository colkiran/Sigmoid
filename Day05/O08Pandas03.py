
import pandas as pd

mileage = {
    "kms" :[ 250, 380, 420],
    'petrol':[15, 23, 30]
}

df = pd.DataFrame(mileage)

print(df)

print("-" * 60)

print(df.loc[0])

print("-" * 60)
print(df.loc[[1, 2]])

print("-" * 60)

df1 = pd.DataFrame(mileage,  index=['day1', 'day2', 'day3'])
print(df1)

