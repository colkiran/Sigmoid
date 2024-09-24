
import pandas as pd
# movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv")

movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv", index_col="movie_title")

print(movie)

print("=" * 40)

idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'}
col_rename = {'director_name':'Director Name',
'num_critic_for_reviews': 'Critical Reviews'}

movie1 = movie.rename(index=idx_rename, columns=col_rename)
print(movie1)
