
import pandas as pd
movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv")

print(movie)

print("=" * 40)

print(movie.shape)

print("=" * 40)

print(movie.size)

print("=" * 40)

print(movie.ndim)

print("=" * 40)

print(len(movie))

print("=" * 40)

# prints the count of non missing values in each column
print(movie.count())

print("=" * 40)
print(movie.min)

print("=" * 40)
print(movie.describe())

print("=" * 40)
print(movie.describe(percentiles=[0.1, 0.3, 0.99]))