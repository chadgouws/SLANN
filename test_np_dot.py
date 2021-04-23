import numpy as np
import pandas as pd

y = np.array([[1],
              [0],
              [0],
              [1]])
x = np.array([[1],
              [1],
              [0],
              [0]])
z = np.array([[0],
              [1],
              [1],
              [0]])
w = np.array([[0],
              [0],
              [1],
              [1]])

df = pd.DataFrame()
print(df)
print('\n')
df = df.append(pd.DataFrame(y).T, ignore_index=True)
print(df)
print('\n')
df = df.append(pd.DataFrame(x).T, ignore_index=True)
print(df)
print('\n')
df = df.append(pd.DataFrame(z).T, ignore_index=True)
print(df)
print('\n')
df = df.append(pd.DataFrame(w).T, ignore_index=True)
print(df)
