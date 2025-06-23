import numpy as np
print("Splitting arrays : \n")
x = [1, 2, 3, 99, 99, 3, 2, 1]
print("Original array:", x)
x1 , x2 ,x3  = np.split(x,[3,5]) # Split x into three parts at indices 0->3 and 3->5 and 5->rest
print("x1:", x1)
print("x2:", x2)
print("x3:", x3)
print("\n\n")
grid = np.arange(16).reshape((4,4)) # Create a 4x4 grid
print("Grid:\n", grid)
upper , lower = np.vsplit(grid,[2]) # Split grid vertically into two parts at index 2
print("Upper part:\n", upper)
print("Lower part:\n", lower)
left , right = np.hsplit(grid,[2]) # Split grid horizontally into two parts at index 2
print("Left part:\n", left)
print("Right part:\n", right)