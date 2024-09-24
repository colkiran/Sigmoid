
import pandas as pd

movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv")
movie['has_seen'] = 0

print(movie)
print("=" * 40)

print("=" * 40)
movie['actor_director_facebook_likes'] = (movie['actor_1_facebook_likes']
                        + movie['actor_2_facebook_likes'] +
                        movie['actor_3_facebook_likes'] +
                        movie['director_facebook_likes'])

print(movie)

print("=" * 40)

print(movie['actor_director_facebook_likes'].isnull().sum())

print("=" * 40)

movie['actor_director_facebook_likes'] = movie['actor_director_facebook_likes'].fillna(0)
print(movie)

print("=" * 40)


movie['is_cast_likes_more'] = \
    (movie['cast_total_facebook_likes'] >=
     movie['actor_director_facebook_likes'])

print(movie)

print("=" * 40)

print(movie['is_cast_likes_more'].all())

print("=" * 40)

movie = movie.drop('actor_director_facebook_likes', axis='columns')

print(movie)
