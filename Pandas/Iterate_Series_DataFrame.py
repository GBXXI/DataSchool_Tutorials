
# %% codecell
import pandas as pd
# %% codecell
df_movies = pd.read_csv('http://bit.ly/imdbratings')
df_movies.columns

# %% markdown
# Iterating through a Series, can be done as in a python list.
# %% codecell

for element in df_movies['title']:
    print(element)

# %% markdown
# Iterating through a DataFrame we use the iterrows method.
# %% codecell

for index, row in df_movies.iterrows():
    print(index, row['title'], row['content_rating'])
