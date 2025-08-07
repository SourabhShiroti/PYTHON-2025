import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[2]=42

print("Print the numpy array elements :",arr)
print("Print the copy numpy array elements :",x)