
import pandas as pd
college = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\data\\college.csv")

print(college)

print("=" * 40)

college_ugds = college.filter(like='UGDS_')
print(college_ugds.head())

print("=" * 40)

import pandas as pd

# creating a dataset
df = pd.DataFrame([[1, 2, 3], [4, 5, 6],
                   [7, 8, 9], [10, 11, 12]],
                  columns=['a', 'b', 'c'])

# viewing the dataFrame
print(df)

# finding mean by rows
print(df.mean(axis='rows'))

print(df.mean(axis='columns'))

