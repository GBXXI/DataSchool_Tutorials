
# %% markdown
# Series is called a column, usually in a dataframe.
# %% codecell
import pandas as pd
# %% codecell
df_ufo = pd.read_csv('http://bit.ly/uforeports')
df_ufo
# %% markdown
# Using bracket selection, is case-sensitive.
# %% codecell
df_ufo['City']

# %% markdown
# Using dot notation. Dot notation, cannot be used if the column header has spaces and if the column name has class attribute(or method) names such as head, shape etc.
# %% codecell
df_ufo.City

# %% markdown
# Creating a new series in our dataframe can be done just by naming the series that we want inserted.
# %% codecell
df_ufo['Location'] = df_ufo['City'] + ', ' + df_ufo['State']
df_ufo.head()
