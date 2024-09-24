
import  pandas as pd


movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv", index_col="movie_title")

print("=" * 40)

print(movie)

print("=" * 40)

print(movie.dtypes.value_counts())


