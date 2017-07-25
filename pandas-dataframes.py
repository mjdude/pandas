import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'] )

print(df)

print(df['W'])
print('Type of df W', type(df['W']))

# Selecting multiple colums
print( df[['W', 'Z']])

# New column using previous colums

df['New'] = df['W'] + df['Y']
print(df)

# Removing columns , default value of axis 0 refers to the index, 1 refersd to colums

print(df.drop('New', axis=1))

# Notice original df hasnt been updated
print(df)

# Use inplace to update df
df.drop('New', axis=1, inplace=True)

print(df)

# What does the df loook like (remember its a tuple)
print(df.shape)

# ROWS
print(df.loc['A'])

# Row data type is the same as a column, its a panda Series
print('Data type of row is ', type(df.loc['A']))

# Even with labeled rows you can use index positions with iloc
# should be same as df.loc['A']
print(df.iloc[0])

# Subset of ros and columns
print(df.loc['B', 'Y'])

# If you want to select a list of subsets, pass in a list
print(df.loc[['A', 'B'], ['W', 'Y']])


