
# %% codecell
import pandas as pd
import numpy as np
# %% codecell
df_drinks = pd.read_csv('http://bit.ly/drinksbycountry')
df_drinks.dtypes
# %% markdown
# In order to get only the numerical series from our dataframe, we use the .select_dtypes method and for the include argument we use the .number method from the numpy library.
# %% codecell
df_drinks.select_dtypes(include=[np.number])
