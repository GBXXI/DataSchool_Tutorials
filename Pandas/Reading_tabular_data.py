
# %% markdown
# Reading the tabular data with the .read_table method. This method assumes the file is a tab seperated file and the first row is a header row.
# %% codecell
import pandas as pd
# %% codecell
df_orders = pd.read_table('http://bit.ly/chiporders')
# %% codecell
df.head()
# %% markdown
# Importing another table which is xor(|) seperated. To read this file correctly we have to pass the sep argument to the .read_table method.
# %% codecell
df_movieusers = pd.read_table('http://bit.ly/movieusers', sep='|', header=None)

# %% markdown
# We can add to our df custom header names by using a list of headers, and pass it as an argument to our .read_table method.
# %% codecell
column_names = ['user_id', 'age', 'gender', 'occupation', 'zip_code']

df_movieusers = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=column_names)
df_movieusers

# %% markdown
# Using the skiprows and skipfooter arguments for the .read_table method when we want to ommit irrelevant text such as comments, that is in our file, before we insert it as a dataframe.
