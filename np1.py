import numpy as np
#Different ways of creating numpy Array

#np.array
arr1 = np.array([1,2,3,1,2,3])
print(arr1)

#np.formiter
arr2 = np.fromiter("HelloWorld",dtype='U2')
print(arr2)

#np.arange
arr3 = np.arange(10,50,5,dtype=float)
print(arr3)


#np.linspace
arr4 = np.linspace(3.5,20,5,dtype=np.int32)
print(arr4)

#np.empty
arr5 = np.empty([3,3],dtype=np.int32)
print(arr5)

#np.ones
arr6 = np.ones([4,4],dtype=np.float32)
print(arr6)

#np.zeros
arr7 = np.zeros([6,6],dtype=np.int32)
print(arr7)

#np.full
arr8 = np.full([4,5],7)
print(arr8)

print("\n__________________________________________________\n")

#Attributes
print("Shape: ",arr6.shape)
print("Dimesion: ",arr6.ndim)
print("Size: ",arr6.size)
print("Data Type: ",arr6.dtype)
print("Item Size: ",arr6.itemsize)

print("\n__________________________________________________\n")

#Random 
arr9 = np.random.rand(5,6)
print(arr9)

arr10 = np.random.randint(10,100,[5,5])
print(arr10)

#identity matrix
arri = np.eye(5)
print(arri)