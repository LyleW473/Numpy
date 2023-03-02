import numpy as np

# ---------------------------------
# Creating arrays

# Creating an array of only zeros, specifying the shape (i.e. number of rows and columns) and the type all items should be (by default it is float64)
my_numpy_array = np.zeros((3, 4), dtype = np.int16)
print(my_numpy_array)

# Creating an array of only ones
my_numpy_array = np.ones((4, 3), dtype = int)
print(my_numpy_array)

# Creating an array with random contents
my_numpy_array = np.empty((5, 2))
print(my_numpy_array)


# Creating arrays that are "LIKE" other arrays

# All zeroes
my_numpy_array = np.zeros_like([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
print(my_numpy_array)

# All ones
my_numpy_array = np.ones_like([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
print(my_numpy_array)

# Random values
my_numpy_array = np.empty_like([[1.2, 2.0, 3.0, 4.0, 5.0], [2.4, 3.0, 4.0, 5.0, 6.0]])
print(my_numpy_array)

# Filled with the specified value
my_numpy_array = np.full_like([[1.2, 2.0, 3.0, 4.0, 5.0], [2.4, 3.0, 4.0, 5.0, 6.0]], fill_value = 0, dtype = int)
print(my_numpy_array)

# Creating a sequnce of numbers using arange (Exclusive of the end number)
my_numpy_array = np.arange(0, 11, 2) # Start, End, Step
print(my_numpy_array)

# Allows use of floats
my_numpy_array = np.arange(0, 1.1, 0.1)
print(my_numpy_array)

# Better to use linspace for floating point arguments (Due to finite floating point precision) (Inclusive of end number)
my_numpy_array = np.linspace(0, 4, 9) # Start, End, Number of numbers starting from 0 to 5
print(my_numpy_array)