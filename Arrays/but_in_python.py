# Python List 
numbers = [1,2,3,4,5]
mixed = [1,"two", 3.0, True]

zeros = [0] * 10

import array

# 'i' = signed integer, 'd' = double (float)
int_array = array.array("i", [1, 2, 3, 4, 5])
float_arr = array.array("d", [1.5, 2.5, 3.5])

# Access and append
print(int_array[0])  # 10
int_array.append(50)

import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4])

# 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Common initializers
zeros_2d = np.zeros((2, 3))  # 2x3 array of 0.0
ones_1d = np.ones(5)  # length-5 array of 1.0
step_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]