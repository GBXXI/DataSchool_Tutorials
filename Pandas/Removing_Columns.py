
# %% codecell
import pandas as pd
# %% codecell
df_ufo = pd.read_csv('http://bit.ly/uforeports')

# %% markdown
# In order to remove a column from out dataframe we use the .drop method. We also have to specify the axis attribute. Axis 1(or axis='columns') is our columns axis and Axis 0(or axis='index') is our rows axis. We use the inplace attribute if we permanently
# %% codecell
df_ufo.drop('Colors Reported', axis=1)

# %% markdown
# Dropping multiple columns by passing a list.
# %% codecell
df_ufo.drop(['City', 'State'], axis='columns', inplace=True)

# %% markdown
# Since we know that axis 0 refers to our row, we can remove rows by specifing their index in the dataframe.
# %% codecell
df_ufo.drop([0,1], axis=0, inplace=True)
df_ufo
