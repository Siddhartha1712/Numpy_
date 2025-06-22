import numpy as np

#SEARCH

#____WHERE _____
#searching using where
a = np.random.randint(10,30,size=(3,3))
print("Original array:\n",a)

x = np.where(a>10)
print("x :\n",x)

#search even index using where
a = a.reshape(-1)
print("Array a: \n",a)
x = np.where(a%2==0)
print("X :\n",x)

#_____SearchSorted_____
a = np.linspace(1,10,8,dtype=np.int32)
print("Original array :",a)
x = np.searchsorted(a,[5,6,7])
print("x :",x)