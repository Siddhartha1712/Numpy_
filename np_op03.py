import numpy as np

#_____Sort______

a = np.random.randint(10,50,size=10)
print("Original array: ",a)
a = np.sort(a)
print("Sorted array: ",a)

a = np.random.randint(20,40,size=(3,4))
print("Original array: \n",a)
a = np.sort(a)
print("Sorted array:\n",a)