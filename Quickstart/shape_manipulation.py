import numpy as np

# Reshape and resize

""" 
- Reshape returns a new array with a changed shape without changing the data
- Resize returns a new array with a changed shape and size (with possibly new data)

"""
my_numpy_array = np.arange(10).reshape((5, 2))
print(my_numpy_array, my_numpy_array.shape)

other_array = np.reshape(my_numpy_array, (10, 1))
print(other_array)

my_numpy_array = my_numpy_array.reshape(2, 5)
print(my_numpy_array)

my_numpy_array = np.arange(32).reshape(2, 8, 2)
print(my_numpy_array)

new_array = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 10, 232]))
other_array = np.resize(a = new_array, new_shape = (10, 5))
print(other_array)

# Flatten and ravel

"""
- Flatten and ravel both converts a multi-dimensional array into a one-dimensional array
- Flatten returns a flattened copy of the original array
- Ravel also returns a flattened copy of the original array but may also return a view of the original array instead of a copy
    - A "view" is a new array object that refers to the same data as the original array. This means that any changes made to the view affect the original array

"""
# array_1 = new_array.ravel()
# print(array_1)

# array_2 = new_array.flatten()
# print(array_2)


# view = array_2[8:]
# print("Before", array_2, view)
# view[0] = 99
# print("After", array_2, view)