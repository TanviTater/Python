import numpy as np  
x = np.random.randint(1, 10, size=(3, 4))  # Create a 2D array with shape (3, 4)
print("Original array:", x)
print("Mean of the array:", np.mean(x))
print("Mean of the array along axis 0:", x.mean(0))
x_centered = x-x.mean(0)
print("Centered array:", x_centered)   
print("Mean of centered array along axis 0:", x_centered.mean(0))