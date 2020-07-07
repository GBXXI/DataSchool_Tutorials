
# %% codecell
import pandas as pd
# %% codecell
df_drinks = pd.read_csv('http://bit.ly/drinksbycountry')

# %% markdown
# In order to change a column(series) datatype we use the .astype method, and we cast the methods results either to the same column or to a new column.
# %% codecell
df_drinks.dtypes
# %% codecell
df_drinks['beer_servings'] = df_drinks['beer_servings'].astype(float)
# %% codecell
df_drinks['wine_servings_float'] = df_drinks['wine_servings'].astype(float)
# %% codecell
df_drinks.head()
