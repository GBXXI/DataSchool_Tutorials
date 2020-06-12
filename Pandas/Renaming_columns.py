
# %% codecell
import pandas as pd
# %% codecell
df_ufo = pd.read_csv('http://bit.ly/uforeports')
# %% markdown
# In order to see our columns name we can use the .column attribute.
# %% codecell
df_ufo.columns

# %% markdown
# Renaming columns one by one. We use the inplace attribute to affect permanently our dataframe. If we ommit it we only get a view.
# %% codecell
df_ufo.rename(columns = {'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)

# %% markdown
# Renaming columns with the use of a list.
# %% codecell
headers_list = ['city', 'colors_reported', 'shape_reported', 'state', 'time']

df_ufo.columns = headers_list
df_ufo

# %% markdown
# Renaming columns, while reading the file. We cann achive that by passing our list to the names argument. We also have to pass the header=0 argument in order to declare tha our first row will be our headers and to override the files headers if they exist.
# %% codecell
df_ufo = pd.read_csv('http://bit.ly/uforeports', names=headers_list, header=0)
df_ufo

# %% markdown
# Renaming columns with .str attribute.
# %% codecell
df_ufo.columns = df_ufo.columns.str.replace(' ', '_')
df_ufo
