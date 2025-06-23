import numpy as np
np.random.seed(0) # Set seed for reproducibility
x1 = np.random.randint(10, size=6)  # Create a 1D array with 6 random integers from 0 to 9
x2 = np.random.randint(10, size=(3, 4))  # Create a 2D array with shape (3, 4)
x3 = np.random.randint(10, size=(3, 4, 5))  # Create a 3D array with shape (3, 4, 5)
print("x3 ndim: ", x3.ndim) # Number of dimensions
print("x3 shape:", x3.shape) # Shape of the array
print("x3 size: ", x3.size) # Total number of elements
print("x3 dtype:", x3.dtype)  # Data type of the array
print("x3 itemsize:", x3.itemsize)  # Size of each element in bytes
print("x3 nbytes:", x3.nbytes)  # Total number of bytes consumed
#In general, we expect that nbytes is equal to itemsize times size.