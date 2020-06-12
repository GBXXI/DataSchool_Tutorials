
# %% codecell
import pandas as pd
# %% codecell
df_movies = pd.read_csv('http://bit.ly/imdbratings')

# %% markdown
# First we create a filter for the values we want to have.
# %% codecell
fltr = df_movies['duration'] >= 210

df_movies[fltr]
# %% markdown
# Finding a specific column(series) where our filter is applied by using the .loc method.
# %% codecell
df_movies.loc[fltr, 'title']

# %% markdown
# Alternatively the following notations might be used.
# %% codecell
df_movies.loc[df_movies.duration >= 210, 'title']
df_movies.loc[df_movies['duration'] >= 210, 'title']
