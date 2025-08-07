#Create random (randint-Function) array numpy elements!
import numpy as np
arr=np.random.randint(5,20,8) #(min,max,total_number)
print("Print the random numpy elements :",arr)
print("type of :",type(arr))
print("Dimensions of :",arr.ndim)
print("Data-type :",arr.dtype)