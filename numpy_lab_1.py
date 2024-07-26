import numpy as np

         
# question -1=Convert the below list into numpy array then display the array

list = [1, 2, 3, 4, 5]
array = np.array(list)
print(array)

# question -2 Convert the below list into a numpy array then display the array then display the first and last index and then
#  multiply each element by 2 and display the result.
# Input: my_list = [1, 2, 3, 4, 5)


list = [1, 2, 3, 4, 5]
array = np.array(list)
print("Array:", array)
print("First element:",array[0])
print("Last element:",array[-1])
each_array = array * 2
print("Array after multiply by 2 each elemen")
print(each_array)


# question -3  Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.



arr=np.zeros((1,10))
print("print zero in 10 time ")
print(arr)

arr = np.zeros((1,10))+1
print("print one in 10 time ")
print(arr)
arr = np.zeros((1, 5))+5
print("print five  in 5 time ")
print(arr)


# 4. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Sample Output: [[234] [567] [8910]]

arr = np.arange(2, 11).reshape(3,3)
print(arr)



