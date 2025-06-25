import numpy as np 
rand = np.random.RandomState(42)
x = rand.randint(100,size = 10)
print("Original array:", x)
print("Elements at index 3, 5, 7 : ",x[3],x[5],x[7])  # Accessing elements at specific indices
print("Elements at index 3 , 5, 7:", x[[3, 5, 7]])  # Fancy indexing to select specific elements
indexes = [3, 5, 7]
print("Elements at indices 3, 5, 7 using fancy indexing:", x[indexes])  # Fancy indexing with a list
print("Elements at indices 3, 5, 7 using fancy indexing with a numpy array:", x[np.array(indexes)])  # Fancy indexing with a numpy array
print("\n")
print("When using fancy indexing, the shape of the result reflects the shape of the index arrays rather than the shape of the array being indexed:\n")
indexes = np.array([[3,5],
                    [7,9]])
print("Elements at indices [[3, 5], [7, 9]] using fancy indexing:\n", x[indexes])  # Fancy indexing with a 2D array
x = np.arange(12).reshape(3, 4)  # Create a 2D array
print("\nOriginal 2D array:\n", x)
row =  np.array([0, 1, 2])  # Row indices
col = np.array([1, 2, 3])  # Column indices
print("Elements at specific row and column indices using fancy indexing:\n", x[row, col])  # Fancy indexing with row and column indices
print("Elements at specific row and column indices using fancy indexing with broadcasting:\n",x[row[:, np.newaxis], col])  # Fancy indexing with broadcasting
print("Elements using broadcasting:",row[:, np.newaxis] * col)  # Fancy indexing with broadcasting
print("\n")
print("Combined Indexing:\n ")
x = np.arange(12).reshape(3, 4)  # Create a 2D array
print("Original 2D array:\n", x)
print("Elements at indices [2, 0, 1] of row 2 using combined indexing:\n", x[2, [2, 0, 1]])
print("Elements at indices [2, 0, 1] of rows 1 and 2 using combined indexing:\n", x[1:, [2, 0, 1]])
print("\n MASKING \n")
mask = np.array([1,0,1,0], dtype=bool)  # Create a boolean mask
print("Elements at masked positions:\n",x[row[:, np.newaxis], mask])