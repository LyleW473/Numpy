import numpy as np

# ---------------------------------
# Accessing items / information

# All items must be the same / homogenous
my_numpy_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(my_numpy_array)
print(my_numpy_array[0])
print(my_numpy_array[2][-1])
print(my_numpy_array[2][0])

# Number of dimensions
print(my_numpy_array.ndim)

# Shape of the array / matrix
print(my_numpy_array.shape)

# Total number of items inside the matrix
print(my_numpy_array.size)

# The type of the element in the matrix / array
print(my_numpy_array.dtype, my_numpy_array.dtype.name)

# The size in bytes of each element in the array
print(my_numpy_array.itemsize)

# Sequences of sequences are converted to 2 dimensional arrays
my_numpy_array = np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15)])
print("My array", my_numpy_array)

# Converts all items in the array to the same type
my_numpy_array = np.array([(1.5, 2, 3, 4, 5), (6.5, 7, 8, 9, 10), (11.5, 12, 13, 14, 15)])
print(my_numpy_array, my_numpy_array.dtype)

# Can specify what type
my_numpy_array = np.array([(1.5, 2, 3, 4, 5), (6.5, 7, 8, 9, 10), (11.5, 12, 13, 14, 15)], dtype = int)
print(my_numpy_array, my_numpy_array.dtype)

my_numpy_array = np.array([(1.5, 2, 3, 4, 5), (6.5, 7, 8, 9, 10), (11.5, 12, 13, 14, 15)], dtype = str)
print(my_numpy_array, my_numpy_array.dtype, my_numpy_array.dtype.name)
