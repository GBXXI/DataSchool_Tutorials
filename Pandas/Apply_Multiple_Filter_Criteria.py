
# %% codecell
import pandas as pd
# %% codecell
df_movies = pd.read_csv('http://bit.ly/imdbratings')

# %% markdown
# In pandas dataframe the and keyword is & symbol and the or keyword is | symbol.
# %% codecell
df_movies
# %% codecell
df_movies[(df_movies['duration'] >= 210) & (df_movies['genre'] == 'Adventure')]
df_movies[(df_movies['duration'] >= 210) | (df_movies['genre'] == 'Adventure')]

# %% markdown
# Assigning our criteria to a filtered dataframe.

# %% codecell
df_and_fltr = df_movies[(df_movies['duration'] >= 210) & (df_movies['genre'] == 'Adventure')]
df_and_fltr

df_or_fltr = df_movies[(df_movies['duration'] >= 210) | (df_movies['genre'] == 'Adventure')]
df_or_fltr

# %% markdown
# Assigning multiple criteria via a list
# %% codecell
crtr_list = ['Crime', 'Drama', 'Action']

df_movies['genre'].isin(crtr_list)
