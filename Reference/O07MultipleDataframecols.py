
import pandas as pd

movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv", index_col="movie_title")

print(movie.select_dtypes(include=['int']).head())

print("=" * 40)

print(movie.select_dtypes(include=['number']).head())

print("=" * 40)

print(movie.filter(like='facebook').head())

print("=" * 40)

print(movie.filter(regex="\d").head())

