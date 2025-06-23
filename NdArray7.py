import numpy as np 
print("Concatenation\n")
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
x3 = np.array([7,8,9])
print("x1:", x1)
print("x2:", x2)
print("x3:", x3)
print("Concatenating x1 and x2 : " , np.concatenate([x1,x2]))  # Concatenate x1 and x2
print("Concatenating x1, x2 and x3 : " , np.concatenate([x1,x2,x3]))  # Concatenate x1, x2 and x3
grid = np.array([[1,2,3],[4,5,6]])
print("Grid:\n", grid)
print("Concatenating along axis 0:\n", np.concatenate([grid, grid], axis=0)) #axis=0 → Vertical stacking (adding rows): Think "Down the rows"
print("Concatenating along axis 1:\n", np.concatenate([grid, grid], axis=1)) #axis=1 → Horizontal stacking (adding columns): Think "Across the columns"
print("\n\n")
#For working with arrays of mixed dimensions, it can be clearer to use the np.vstack (vertical stack) and np.hstack (horizontal stack) functions:
#  Use np.vstack - x1 will be reshaped automatically

#vstack()	Number of columns must match
#vstack()	Stack vertically (add rows)
result_vstack = np.vstack([x1, grid])
print("Using np.vstack to stack arrays vertically:\n", result_vstack)

#  Use np.hstack - reshape x1 to (3,1) and transpose grid to (3,2)
#hstack()	Number of rows must match
#hstack()	Stack horizontally (add columns)
x1_reshaped = x1.reshape((3, 1))
grid_transposed = grid.T  # Transpose grid from (2,3) to (3,2)
result_hstack = np.hstack([x1_reshaped, grid_transposed])
print("Using np.hstack to stack arrays horizontally:\n", result_hstack)