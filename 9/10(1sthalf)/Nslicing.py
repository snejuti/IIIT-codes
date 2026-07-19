#1D
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5]) #1,2,3,4,5,6,7

print(arr[4:]) #1,2,3,4,5,6,7

print(arr[:4]) #1,2,3,4,5,6,7

#2D
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4]) #1,2,3,4,5,6,7
print(arr[0:2,2]) #1,2,3
print(arr[0:2,1:4]) #1,2,3,4,5,6,7