# importing the module
import numpy as np

# Create initial array of shape (2, 6)
arr = np.arange(1, 13).reshape(2, 6)
print('Original Array:')
print(arr)

# Append a row of shape (1, 6) — row-wise (axis=0)
col1 = np.arange(10, 16).reshape(1, 6)
print('\nRow to be appended:')
print(col1)

arr = np.append(arr, col1, axis=0)
print('\nArray after appending row:')
print(arr)

# Append columns — so need shape (3, 6), because arr now has 3 rows
col = np.arange(20, 38).reshape(3, 6)
print('\nColumns to be appended:')
print(col)

arr_col = np.append(arr, col, axis=1)
print('\nArray after appending columns:')
print(arr_col)

# Append more rows — arr_col has shape (3, 12), so new rows need 12 columns
row = np.arange(100, 124).reshape(2, 12)
print('\nRows to be appended:')
print(row)

arr_row = np.append(arr_col, row, axis=0)
print('\nFinal array after appending rows:')
print(arr_row)

#hstack()
a = np.array([[1,3,5],[2,4,6]])
b = np.array([[1,2,3],[4,5,6]])

print("hstack array: \n",np.hstack((a,b)))

#Vstack()
a = np.array([ 1, 2, 3] )
print ("1st Input array : \n", a) 

b = np.array([ 4, 5, 6] )
print ("2nd Input array : \n", b) 

res = np.vstack((a, b))
print ("Output vertically stacked array:\n ", res)

#stack 
a = np.linspace(1,20,9,dtype=np.int32).reshape(3,3)
b = np.linspace(5,25,9,dtype=np.int32).reshape(3,3)

print("Axis 0 Stack:\n",np.stack((a,b),axis=0))
print("Axis 1 Stack:\n",np.stack((a,b),axis=1))

#Reshape 

a = np.linspace(10,50,25,dtype=np.int32)
print("Original array a:\n",a)
a = a.reshape(5,5)
print("Reshaped array of 5*5:\n",a)