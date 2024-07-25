import numpy as n
# What is Numpy

# NumPy, which stands for "Numerical Python," is a popular Python library for numerical and scientific computing.
#  It provides support for working with large, multi-dimensional arrays and matrices of data,
#  along with a collection of mathematical functions to operate on these arrays.

# NumPy is a fundamental library for data manipulation and analysis in Python and is widely used in various fields such as data science,
#  machine learning, scientific research, and engineering
#python visulation Notepad

# Create a NumPy ndarray Object

# NumPy is used to work with arrays. The array object in NumPy is called ndarray. We can create a NumPy ndarray object by using the array() function.

# Dimensions in Arrays

# 1) 0-D Arrays

# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

# 2) 1-D Arrays

# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

# These are the most common and basic arrays.

# 3)2-D Arrays

# An array that has 1-D arrays as its elements is called a 2-D array.

# These are often used to represent matrix or 2nd order tensors.

# 4) 3-D arrays

# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

# These are often used to represent a 3rd order tensor.

# Ln 2879, Col 80

# Rain showers Tomorrow
# #-------------------------------------------------------------------------------------
# a = np.array(42)
# b = np.array([1,2,3,4,5])
# c = np.array([[1,2,3],[4,5,6]])
# d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# print(a)
# print(b)
# print(c)
# print(d)
# print(a.shape)
# print(b.shape)
# print(c.shape)
# print(d.shape)
#----------------------------------------------------------------------------------
#Example with bool
# arr = np.array([True,False,True],dtype=np.bool)
# print(arr)
#-------------------------------
#object: Generic python object type
#Example with object
# arr=np.array(['apple',2,3,5],dtype=np.object_)
# print(arr)
#---------------------------
#example with string
# arr=np.array(['hello word'],dtype=np.str_)
# print(arr)
#--------------------------------------------------------
# l=[12,34,54,65,34,65]

# arr=np.array(l)
#------------------------------

# arr=np.zeros((5,3))+9
# print(arr)
# arr[:,:] = 9
# print("modify array")
# print(arr)
# #--------------------------------------------

# arr=np.ones((5,3))+1
# print(arr)
# #-----------------------------------------------------
# arr=np.array([[10,20,30],[10,20,30],[10,20,30]])
# print(arr)
#-------------------------------------------------
# rand=np.random.rand(2,3)
# print(rand)
#_-----------------------------------------------------------
# rand=np.random.randint(0,10,2)
# print(rand)
#------------------------------------------
# rand=np.random.randint(0,100,12)

# print(rand)
#=-------------------------------------
# reshape function in NumPy allows you to change the shape (dimensions) of an array without changing Is data. This can be useful when you want to rearrange the way data is organized in an array, such as Onverting a 1-dimensional array into a 2-dimensional matrix or vice versa, or changing the size of a multi-dimensional array while maintaining the total number of elements.

# arr=arr.reshape(3,-1)
# print(arr)
# print("Array values is ",arr[0][1])
# print("Array values is ",arr[1][0])
# print(arr.shape)
# arr=arr.reshape(-1,4)
# print(arr)
# arr=arr.reshape(2,-1)
# print(arr)

# That means if you start with the same seed and use the same sequence of random number generation operations, you will get the same sequence of random numbers every time. This can be useful in situations where you need predictable random numbers for debugging, testing, or simulations.
#----------------------------------------------------------------------
# n.random.seed(134567)
# arr=n.random.randint(1,500,30).reshape(6,5)
# print(arr)
# print(arr[2:,2:])
# print(arr[3:5,2:4])
#------------------------------------------------------------
ar=n.array([1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33])
slicing=ar[4:9]
print("new slicing",slicing)
print("new array",ar)
print(type(slicing))
print(type(ar))
slicing[:]=0
print("old slicing",slicing)
print("old arr",ar)
#---------------------------------------------------------------

