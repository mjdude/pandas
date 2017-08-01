import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'] )

print(df)

booldf = df > 0

print(booldf)

print(df[df>0])

print(df['W'] > 0)

print(df[df['W'] > 0])

# This ...

resultdf = df[df['W'] > 0]
print('resultdf X ')
print(resultdf['X'])

# is the same as this

print('result df in one step')

print(df[df['W'] > 0]['X'])