import numpy as np
arr=np.array([1,2,3,4,6,7,8])
x=np.searchsorted(arr,5)

print("It return index value where insert new data :",x)