
import pandas as pd

movies = pd.read_csv("C:\\Training\\PycharmProjects\\Sigmoid\\DataSource\\movie.csv")

idx = movies.index
col = movies.columns
data = movies.values

print("-"  * 60)

print(idx)

print("-"  * 60)

print(col)

print("-"  * 60)

print(data)

print("-"  * 60)
print(f"idx :{type(idx)}")

print("-"  * 60)
print(f"col :{type(col)}")

print("-"  * 60)
print(f"data :{type(data)}")
