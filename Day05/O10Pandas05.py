
import pandas as pd

movie = pd.read_csv("C:\\Training\\PycharmProjects\\Sigmoid\\DataSource\\movie.csv")

print(movie.head)
print("-"  * 60)

# print the count of rows starting from 0
index = movie.index
print(f"index :{index}")

print("-"  * 60)
# all column names
columns = movie.columns
print(f"columns :{columns}")

print("-"  * 60)
# print the value of each row from the db
data = movie.values
print(f"data :{data}")

print("-"  * 60)
# print the indexes
print(f"indexes :{index.values}")

print("-"  * 60)
# print all the column names
print(f"columns :{columns.values}")

print("-"  * 60)
# print the datatype of each column
print(f"dtype :{movie.dtypes}")

print("-"  * 60)
# print the summarized info of count of each datatype used in DB
print(f"dtype count :{movie.dtypes.value_counts()}")

print("-"  * 60)
# printing a column from the db
print(movie['director_name'])

print("-"  * 60)
director = movie['director_name']
actor_fb = movie['actor_1_facebook_likes']

# top 5 rows from the columsn
print(director.head())
print("-"  * 60)

print(actor_fb.head())
print("-"  * 60)
print(f"Director :{director.count()}")
print(f"Actor :{actor_fb.count()}")

print("-"  * 60)
print(f"Actor Min:{actor_fb.min()}")
print(f"Actor Max:{actor_fb.max()}")
print(f"Actor Mean:{actor_fb.mean()}")
print(f"Actor Median:{actor_fb.median()}")
print(f"Actor std:{actor_fb.std()}")
print(f"Actor sum:{actor_fb.sum()}")

