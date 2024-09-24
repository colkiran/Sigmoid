
import pandas as pd
movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv")

print(movie.isnull().head())

print("=" * 40)

print(movie.isnull().sum().head())

print("=" * 40)

print(movie.isnull().sum().sum())

print("=" * 40)

print(movie.isnull().any().any())

print("=" * 40)
print(movie.isnull().dtypes.value_counts())

print("=" * 40)

# print(movie[['color', 'movie_title', 'color']].max())

print(movie.select_dtypes(['object']).fillna('').min())


print("=" * 40)
print(movie.select_dtypes(['object']) \
.fillna('') \
.min())