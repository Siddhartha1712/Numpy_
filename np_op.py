import numpy as np

#iterations
a = np.linspace(10,50,12,dtype=np.int32).reshape(2,3,2)
print("Original Array of Dimension 3: ",a)

#iterate using for and in
print("Sinle loop iteration using 'in'")
for x in a:
    print(x)
print("two loop iteration using 'in'")
for x in a:
    for y in x:
        print(y)
print("Three loop iteration using 'in'")
for x in a:
    for y in x:
        for z in y:
            print(z)

#iteratio nditer
print("Iteration using nditer")
for x in np.nditer(a):
    print(x)

#iteration using ndenumerate
print("Iteration using ndenumerate")
for i,x in np.ndenumerate(a):
    print(i,x)


#Array Split
print("________________________________________________")

a = np.linspace(20,40,10,dtype=np.int32)
print("Original Array:\n",a)

ab = np.array_split(a,4)
print("Array_split: \n",ab)

print("Printing split array using loop")
for x in ab:
    print(x)

#Array  join
a = np.linspace(1,10,9,dtype=np.int32).reshape(3,3)
b = np.linspace(10,20,9,dtype=np.int32).reshape(3,3)

print("Array a:\n",a)
print("Array b:\n",b)

print("Concatination of array by axis 0(row):\n",np.concatenate((a,b),axis=0))
print("Concatination of array by axis 1(column):\n",np.concatenate((a,b),axis=1))