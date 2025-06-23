import numpy as np
grid = np.arange(1,10).reshape(3, 3)  # Create a 2D array (3x3)
print("Original grid:\n", grid)

# 1D -> 2D array conversion
x1 = np.array([1, 2, 3])
print("Row vector via reshape:", x1.reshape((1,3))) # row vector via reshape
print("Row vector via newaxis:", x1[np.newaxis, :])  # row vector via newaxis
print("Column vector via reshape:", x1.reshape((3,1)))  # column vector via reshape
print("Column vector via newaxis:", x1[:, np.newaxis])  # column vector via newaxis 