
import pandas as pd

movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv")

actor_fb = movie['actor_1_facebook_likes']
director = movie['director_name']

print("=" * 40)
print(director.value_counts().head(3))

print("=" * 40)
print(actor_fb.isnull().sum())

print("=" * 40)
print(actor_fb.dtypes)

print("=" * 40)
print(actor_fb.fillna(0)\
                .astype(int)\
                .head(3))



