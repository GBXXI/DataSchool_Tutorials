
# %% codecell
import pandas as pd
# %% codecell
df_orders = pd.read_table('http://bit.ly/chiporders')
df_orders.columns
# %% markdown
# In order to use a string method to pandas we have to specify the stirng with the .str attribute.

# %% codecell
df_orders['item_name'].str.upper()

# %% markdown
# Using the .contains method to find a substring.
# %% codecell
df_orders['item_name'].str.contains('Salsa')

# %% markdown
# Chaining string methods. Since it returns a series.
# %% codecell
df_orders['choice_description'].str.replace('[', '').str.replace(']', '')

# %% markdown
# Using RegEx.
# %% codecell
df_orders['choice_description'].str.replace('[\[\]]', '')
