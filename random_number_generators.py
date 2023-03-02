import numpy as np

# --------------------------------
# Random number generators

my_random_number_generator = np.random.default_rng() # Creating the random number generator

# 3 x 4 array with random numbers between 0 and 1 ("random" is equivalent to "rand")
my_random_number_array = my_random_number_generator.random((3, 4))
print(my_random_number_array)

# 5 x 5 array with random numbers from the standard normal distribution
my_random_number_array = my_random_number_generator.standard_normal((5, 5))
print(my_random_number_array)