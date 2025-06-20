import numpy as np

#Addition and subtraction on array 
a = np.array([[1,2],[2,1]])

print("Array a: \n",a)
print("Array a+1:\n",a+1)
print("Attay a-1:\n",a-1)

#adding two array
b = np.array([[2,1],[1,2]])
print("Array b:\n",b)
print("Array a+b:\n",a+b)
print("Array a+b:\n",a-b)
print("\n__________________________________________________\n")

#Data type 

a = np.array([[1,2,3],[4,5,6]])
print("Array a:\n",a)
print("Arrat a DataType: ",a.dtype)

b = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print("Array b:\n",b)
print("Arrat a DataType: ",b.dtype)

c = np.array([["a","a","a"],["a","a","a"]])
print("Array c:\n",c)
print("Array a DataType: ",c.dtype)

#addition of two array
print("array sum of a+b:\n",np.add(a,b))
#square root of an array
print("Sqrt of a:\n",np.sqrt(a))
#sum of array
print("Sum of array a:",np.sum(a))
#Transpose of array 
print("Transpose of array a:\n",a.T)
#Dot multiplication
print("Dot product of :\n",np.dot(a,b))