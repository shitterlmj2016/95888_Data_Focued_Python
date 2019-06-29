"""
numpy
    create arrays
    reshape arrays
    create types of arrays (empty, identity, etc.)
    boolean indexing

"""
import numpy as np
from statistics import mean, median, variance, pstdev

# create a 1-dimensional array
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12])
print(my_array)

# create a 2-dimensional array
my_2d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(my_2d_array)


# create a 3-dimensional array
my_3d_array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(my_3d_array)

# Print out memory address
print('Memory Address', my_2d_array.data)

# Print out the shape of `my_array`
print('Shape', my_2d_array.shape)

# Print out the data type of `my_array`
print('Data Type', my_2d_array.dtype)

# Print out the stride of `my_array`
print('Strides', my_2d_array.strides)


# Make the array `my_array`
my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int32)

# Print `my_array`
print(my_array, my_array.dtype)


# Create an array of ones
print(np.ones((3, 4)))

# Create an array of zeros
print(np.zeros((2, 3, 4), dtype=np.int16))

# Create an array with random values
print(np.random.random((2, 2)))

# Create a full array
print(np.full((2, 4), 8))

# Create an array of evenly-spaced values
print(np.arange(10, 25, 5))

# Create an array of evenly-spaced values
print(np.linspace(0, 2, 9))

# identity 对角为1的矩阵
print(np.identity(6))

# Import your data
x, y, z = np.loadtxt('data.txt',
                     skiprows=1,
                     unpack=True)
print(x)
print(y)
print(z)

my_array2 = np.genfromtxt('data2.txt',
                      skip_header=1,
                      filling_values=-999)
print(my_array2)

x = np.arange(0.0, 5.0, 1.0)
print(x)
np.savetxt('test.out', x, delimiter=',')

my_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Print the number of `my_array`'s dimensions
print(my_array.ndim)

# Print the number of `my_array`'s elements
print(my_array.size)

# Print information about `my_array`'s memory layout
print(my_array.flags)


# Initialize `x`
x = np.ones((3, 4))

# Check shape of `x`
print(x.shape)
print(x)

# Initialize `y`
y = np.random.random((3, 4))

# Check shape of `y`
print(y.shape)
print(y)

# Add `x` and `y`
x + y

# Initialize `x`
x = np.ones((3, 4))

# Check shape of `x`
print(x.shape)
print(x)

# Initialize `y`
y = np.arange(4)

# Check shape of `y`
print(y.shape)
print(y)

# Subtract `x` and `y`
print(x - y)

# Subtract `x` and `y`
np.subtract(x, y)

# Multiply `x` and `y`
np.multiply(x, y)

# Divide `x` and `y`
np.divide(x, y)

# Calculate the remainder of `x` and `y`
np.remainder(x, y)


# `x` AND `y`
np.logical_and(x, y)
np.logical_or(x, y)

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
my_2d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
my_3d_array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])

print(my_array[1])
print(my_2d_array[1][2])

# Select the element at row 1 column 2
print(my_2d_array[1, 2])

# Select items at index 0 and 1
print(my_array[0:2])

# Select items at row 0 and 1, column 1
print(my_2d_array[0:2, 1])

print(my_2d_array[1, 2:4])

# Select items at row 1
# This is the same as saying `my_3d_array[1,:,:]
print(my_3d_array[1, ...])

# Try out a simple example
# you select those values from your array that fulfill a certain condition.
mask = my_array < 2
print(mask)
print(my_array[mask])

# Try out a simple example
mask = my_array > 3
print(mask)
print(my_array[mask])

# Specify a condition
bigger_than_3 = (my_3d_array >= 3)

# Use the condition to index our 3d array
print(my_3d_array[bigger_than_3])

# Specify a condition
mask = (my_3d_array >= 3) & (my_3d_array < 10)

# Use the condition to index our 3d array
print(my_3d_array[mask])

# Select elements at (1,0), (0,1), (1,2) and (0,0)
print(my_2d_array[[1, 0, 1, 0], [0, 1, 2, 0]])

# What the second part, namely, [:,[0,1,2,0]], is tell you that you want to keep all the rows of this result, but that you want to change the order of the columns around a bit. You want to display the columns 0, 1, and 2 as they are right now, but you want to repeat column 0 as the last column instead of displaying column number 3. This will give you the following result:
print(my_2d_array[[1, 0, 1, 0]])


# Transpose Your Arrays
my_2d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Print `my_2d_array`
print(my_2d_array)

# Transpose `my_2d_array`
print(np.transpose(my_2d_array))

# Or use `T` to transpose `my_2d_array`
print(my_2d_array.T)

x = my_2d_array

# Print the shape of `x`
print(x.shape)
print(x)

print(np.resize(x, (3, 4)))
print(np.resize(x, (2, 6)))


# Flatten `x`
z = x.ravel()

# Print `z`
print(z)

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# Append a 1D array to your `my_array`
new_array = np.append(my_array, [7, 8, 9, 10, 11, 12])

# Print `new_array`
print(my_array)
print(new_array)


# Append an extra column to your `my_2d_array`
# Note how, when you append an extra column to my_2d_array, the axis is specified.
# Remember that axis 1 indicates the columns, while axis 0 indicates the rows in 2-D arrays.
new_2d_array = np.append(my_2d_array, [[7], [8], [9]], axis=1)

# Print `new_2d_array`
print(new_2d_array)

# Insert `5` at index 1
np.insert(my_array, 1, 5)
print(my_array)


# Delete the value at index 1
np.delete(my_array,[1])

my_resized_array = np.array([[91, 92, 93, 94],
                             [91, 92, 93, 94],
                             [91, 92, 93, 94]])
print(my_resized_array)
# Stack arrays row-wise
print(np.r_[my_resized_array, my_2d_array])


# Stack arrays horizontally
print(np.hstack((my_resized_array, my_2d_array)))


# Stack arrays column-wise
print(np.column_stack((my_resized_array, my_2d_array)))


