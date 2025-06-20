#creating a rank 1 numpy array
import numpy as np

arr1 = np.array([1,2,3,4])
print("Array 1",arr1)

#creating a rank 2 numpy array
arr2 = np.array([['a','a','a'],['b','b','b'],['c','c','c']])
print("Array 2",arr2)

#array form tuple
arr3 = np.array((1,1,1))
print("Array 3",arr3)

print("\n______________________________________\n")

#Accessing and slicing 
#arr[start_row:end_row, start_col:end_col:step]

arr4 = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [-8,-7,-6,-5],
                 [-4,-3,-2,-1]])

print("Array 4:",arr4)
print("Array4 values of 1st and 2nd row are:\n",arr4[1:3,:])
print("Array4 values of 1st two rows and colums 0 and 2: \n",arr4[:2,::2])