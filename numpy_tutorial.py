from numpy import *

# 1D-array
A = array([1,2,3,4,5,6,7,8,9,10])
A1 = array(['apple', 'banana', 'cherry'])

# 2D-array
B = array([[1,2,3,4,5],[6,7,8,9,10]])

# 3D-array
C = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Check Number of Dimensions?
print('number of dimensions array A :',A.ndim)
print('number of dimensions array A1 :',A1.ndim)
print('number of dimensions array B :',B.ndim)
print('number of dimensions array C :',C.ndim)

# Ckeck datatype of array
print('DataType of array A:',A.dtype)
print('DataType of array A1:',A1.dtype)

# Access Array Elements

# Access first element of 1D-array
print('First element of an 1D-array A:',A[0])
# Access first element of an 2D-array
print('First element of an 2D-array B:',B[0,0])
# Access third element of the second array of the first array
print('Third element of the second array of the first array:',C[0, 1, 2])
# Addition of first element of 1D-array A and 2D-array B
print('Addition of first element of 1D-array A and 2D-array B:',A[1] + B[0,0])

# Numpy array slicing [start:end:step].
# A([1,2,3,4,5])
print(A[2:5])
print(A[3:])
print(A[:3])
print(A[0::2])
# B([[1,2,3,4,5],[6,7,8,9,10]])
print(B[1,1:4])

# Creating Arrays With a Defined Data Type
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

A = array([1,2,3,4,5], dtype=float)
B = array([1, 2, 3, 4], dtype='i4')
print(A)
print(B)

# Converting data type on existing array
A = array([1.1, 2.1, 3.1])
B = A.astype('i')  #A.astype(int)
print(B)
C = array([1, 0, 3])
D = C.astype(bool)
print(D)

# NumPy Array Copy vs View
A = array([1, 2, 3, 4, 5])
B = A.copy()
C = A.view()
A[0] = 42

print(A)
print(B)
print(C)

# Check if Array Owns its Data
# The copy returns None.
# The view returns the original array.
print(B.base)
print(C.base)

# NumPy Array Shape
# The shape of an array is the number of elements in each dimension.
A = array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('array A:',A)
print('array A number of dim:',A.ndim)
print('array A data type:',A.dtype)
print('shape of array A:',A.shape)

B = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('array B:',B)
print('array B number of dim:',B.ndim)
print('array B data type:',B.dtype)
print('shape of array B:',B.shape)

C = array([1, 2, 3, 4], ndmin=5)
print('array A:',C)
print('array C number of dim:',C.ndim)
print('array C data type:',C.dtype)
print('shape of array C:', C.shape)


# NumPy Array Reshaping
A = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
E = array([1, 2, 3, 4, 5, 6, 7, 8])

# Reshape From 1-D to 2-D
B = A.reshape(4, 3)
print(B)

# Reshape From 1-D to 3-D
C = A.reshape(2,2,3)
D = A.reshape(2,3,2)
print(C)
print(D)

# Unknown Dimension
F = E.reshape(2, 2, -1)
print(F)


# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
A = array([[1, 2, 3], [4, 5, 6]])
B = A.reshape(-1)
print(B)

C = array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
D = C.reshape(-1)
print(D)

# NumPy Array Iterating
# 1D-array
A = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
for i in A:
    print(i)

# 1D-array
B = array([[1, 2, 3], [4, 5, 6]])
for i in B:
    #print(i)
    for j in i:
        print(j)

# 3D-array
C = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in C:
#     #print(x)
#     for y in x:
#         #print(y)
#         for z in y:
#             print(z)

# Iterating Arrays Using nditer()
# In basic for loops, iterating through each scalar of an array we need to use n for loops 
# which can be difficult to write for arrays with very high dimensionality.
C = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in nditer(C):
    print(x)

# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.
A = array([1, 2, 3])
for id, x in ndenumerate(A):
  print(id, x)

B = array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in ndenumerate(B):
  print(idx, x)


# Iterating Array With Different Data Types
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action,
# that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
A = array([1, 2, 3,4])

for x in nditer(A, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Iterating With Different Step Size
A = array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in nditer(A[: ,::2]):
    print(x)


# Joining NumPy Arrays
# Joining means putting contents of two or more arrays in a single array.
A = array([1, 2, 3])
B = array([7, 8, 9])
C = concatenate((A, B))
print(C)

A = array([[1, 2, 3],[4,5,6]])
B = array([[7, 8, 9],[10,11,12]])
C = concatenate((A, B), axis=1)
print(C)

# Joining Arrays Using Stack Functions
A = array([1, 2, 3])
B = array([7, 8, 9])
C = stack((A, B), axis=1)
print(C)

# Stacking Along Rows
A = array([1, 2, 3])
B = array([7, 8, 9])
C = hstack((A, B))
print(C)

# Stacking Along Columns
A = array([1, 2, 3])
B = array([7, 8, 9])
C = vstack((A, B))
print(C)

# Stacking Along Height (depth)
A = array([1, 2, 3])
B = array([7, 8, 9])
C = dstack((A, B))
print(C)


# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.
A = array([1, 2, 3, 4, 5, 6])

# Split Into Arrays
B = array_split(A, 2)
print(B)
print(B[0])
print(B[1])

# Note: We also have the method split() available but it will not adjust the elements when elements are less in source array 
# for splitting like in example above, array_split() worked properly but split() would fail.
C = array_split(A, 4)
print(C)

# Splitting 2-D Arrays
A = array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
B = array_split(A, 3)
print(B)
print(B[0])
print(B[1])
print(B[2])

A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
B = array_split(A, 3)
print(B)
print(B[0])
print(B[1])
print(B[2])

# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.
A = array([1, 2, 3, 4, 5, 4, 4])
B = where(A == 4)
print(B)

A = array([1, 2, 3, 4, 5, 6, 7, 8])
B = where(A%2 == 0)
print(B)


# Search Sorted
# Find the indexes where the value 7 should be inserted:
A = array([6, 7, 8, 9])
B = searchsorted(A, 7)
print(B)

# Search From the Right Side
# Find the indexes where the value 7 should be inserted, starting from the right:
A = array([6, 8, 9, 7, 10])
B = searchsorted(A, 7, side='right')
print(B)

# Find the indexes where the values 2, 4, and 6 should be inserted:
A = array([1, 3, 5, 7])
B = searchsorted(A, [2, 4, 6])
print(B)

# Sorting Arrays
A = array([3, 2, 0, 1])
print(sort(A))

# Sort the array alphabetically:
A = array(['banana', 'cherry', 'apple'])
print(sort(A))

# Sort a boolean array:
A = array([True, False, True])
print(sort(A))

# Sorting a 2-D Array
A = array([[3, 2, 4], [5, 0, 1]])
print(sort(A))

# Filtering Arrays
# Create an array from the elements on index 0 and 2:
A = array([41, 42, 43, 44])
x = [True, False, True, False]
B = A[x]
print(B)

# Create a filter array that will return only values higher than 42:
A = array([41,42,43,44])
filter_array = []

for i in A:
    if i>42:
        filter_array.append(True)
    else:
        filter_array.append(False)

B = A[filter_array]

print(filter_array)
print(B)

# Create a filter array that will return only even elements from the original array:
A = array([1,2,3,4,5,6,7,8,9,10])
even_no = []

for i in A:
    if i%2 == 0:
        even_no.append(True)
    else:
        even_no.append(False)

print(even_no)
print(A[even_no])

# Creating Filter Directly From Array
arr = array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:
arr = array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)