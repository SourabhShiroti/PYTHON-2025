import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print("Before Dimensions is :",arr.ndim)
x=arr.reshape(4,2)
print("Print the matrix reshape :",x)
print("After Dimensions of :",x.ndim)