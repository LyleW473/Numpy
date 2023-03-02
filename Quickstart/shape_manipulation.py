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
array_1 = new_array.ravel()
print(array_1)

array_2 = new_array.flatten()
print(array_2)


view = array_2[8:]
print("Before", array_2, view)
view[0] = 99
print("After", array_2, view)


# Stacking different arrays
"""
- Arrays must be of the same shape / size
"""

a = np.arange(10).reshape(2, 5)
b = np.arange(11, 21).reshape(2, 5)
print(a)
print(b)

c = np.hstack((a, b)) # Stacks horizontally
print(c)

d = np.vstack((a, b)) # Stacks vertically
print(d)

array = np.r_[1:4, 5, 4]
print(array)

second_array = np.r_[np.array([1, 2, 3]), -1, -2, np.array([4, 5, 6])] # Stacks based on row with indexing
print(second_array)

new_array = np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])] # Stacks based on column
print(new_array)

# Splitting an array into multiple arrays
"""
- "hsplit", "vsplit" and "array_split" all return views into the original array

- array_split allows "indices_or_sections" (a parameter) to be an integer that does not equally divide the axis
- array_split also performs the same functionality as hsplit and vsplit if the axis is provided, horizontal split by default (axis = 0)
"""

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

a = np.hsplit(my_array, 5) # Splits my_array into 5
print(a)

my_array = np.array(([3, 6, 9, 12, 15], [2, 4, 6, 8, 10], [1, 2, 3, 4, 5], [0, 0, 1, 1, 2])) 
b = np.vsplit(my_array, 2) # Splits array into 2
print(b)

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

c = np.array_split(my_array, 3) # Splits my_array into 3 regardless of whether 
print(c)

# These two perform the same functionality
print(np.array_split(my_array, 2, axis = 0)) 
print(np.hsplit(my_array, 2))