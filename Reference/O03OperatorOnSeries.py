
import pandas as pd

movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv")

print(movie.head())

print("=" * 40)

imdb_scr = movie['imdb_score']
print(f"IMDB_SCORE :{imdb_scr}")

print("=" * 40)

print(f"imdb_scr + 1 :{imdb_scr + 1}")

print("=" * 40)

print(f"imbd_scr * 2.5 :\n {imdb_scr * 2.5}")

print("=" * 40)

print(f"imbd_scr // 7 :\n {imdb_scr // 7}")

print("=" * 40)

print(f"imdb_scr > 7 :\n {imdb_scr > 7}")

print("=" * 40)

director = movie['director_name']

print("=" * 40)

print(f"imdb_scr + 1 :\n {imdb_scr.add(1)}")

"""
>>> imdb_score.add(1)               # imdb_score + 1
>>> imdb_score.mul(2.5)             # imdb_score * 2.5
>>> imdb_score.floordiv(7)          # imdb_score // 7
>>> imdb_score.gt(7)                # imdb_score > 7
>>> director.eq('James Cameron')    # director == 'James Cameron'
"""
