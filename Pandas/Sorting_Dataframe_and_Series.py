
# %% codecell
import pandas as pd
# %% codecell
df_movies = pd.read_csv('http://bit.ly/imdbratings')
# %% codecell
df_movies.head()

# %% markdown
# Sorting a Series in a descending order.
# %% codecell
df_movies['title'].sort_values(ascending=False)

# %% markdown
# Sorting a dataframe.
# %% codecell
df_movies.sort_values('duration')

# %% markdown
# Sorting a dataframe by the values of two series.
# %% codecell
df_movies.sort_values(['content_rating', 'duration'], ascending=[True, False])
