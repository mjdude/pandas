import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a' : 10, 'b' : 20, 'c' : 30}

print(pd.Series(data = my_data))
print(pd.Series(data = my_data, index=labels))

# passing in a numpy array into panda series is essentially the same as passing
# passin in a python list

print( pd.Series(arr, labels))

# Panda series can even hold functions or references to functions
ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])

print(ser1)

ser2 = pd.Series([1,2,5,4], ['USA','Germany', 'Italy', 'Japan'])

print(ser2)
