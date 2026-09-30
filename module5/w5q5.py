import numpy as np

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
               [10,11,12]])

print(arr[1::2,0::2])

# 1::2 means start from 1 row and select next second row to it
# 0::2 means start from 0 column and select next second column to it