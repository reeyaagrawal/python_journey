import numpy as np

arr=np.array([[1,2,3],
              [24,15,26],
              [7,8,9],
               [10,11,12]])

# case 1
result1=arr[:,np.argsort(arr[1,:])]
print(result1)

print()

# case2

result2=arr[np.argsort(arr[:,1]),:]
print(result2)

