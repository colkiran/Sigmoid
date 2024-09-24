
import pandas as pd
movie = pd.read_csv("C:\\Training\\Dataset\\Python CSV\\movie.csv")
print(movie)

print("=" * 40)

print(movie.columns)

print("=" * 40)

disc_core = ['movie_title', 'title_year', 'content_rating', 'genres']

disc_people = ['director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name']

disc_other = ['color', 'country', 'language', 'plot_keywords', 'movie_imdb_link']

cont_fb = ['director_facebook_likes', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'cast_total_facebook_likes', 'movie_facebook_likes']

cont_finance = ['budget', 'gross']

cont_num_reviews = ['num_voted_users', 'num_user_for_reviews', 'num_critic_for_reviews']

cont_other = ['imdb_score', 'duration', 'aspect_ratio', 'facenumber_in_poster']

new_col_order = disc_core + disc_people + disc_other + cont_fb + cont_finance + cont_num_reviews + cont_other

print(set(movie.columns) == set(new_col_order))

movie1 = movie[new_col_order]
print(movie1.head())

