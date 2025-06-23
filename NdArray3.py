import numpy as np  
x1 = np.random.randint(10, size=6)  # Create a 1D array with 6 random integers from 0 to 9
x2 = np.random.randint(10, size=(3, 4))  # Create   a 2D array with shape (3, 4)
x3 = np.random.randint(10, size=(3, 4, 5))  # Create a 3D array with shape (3, 4, 5)

print(x1)
print("Array indexing : accessing single elements")
print("Access the first element:", x1[0])  # Access the first element
print("Access the second element:", x1[1])  # Access the second element
print("Access the last element:", x1[-1])  # Access the last element

print("\n\n\n")
print(x2)
print("Array indexing : accessing elements in a 2D array")
print("Access the element at row 0, column 0:", x2[0, 0])  # Access the element at row 0, column 0
print("Access the element at row 1, column 2:", x2[1, 2])  # Access the element at row 1, column 2
print("Access the last row, last column:", x2[-1, -1])  # Access the last row, last column
print("Modifying element at row 0, column 0 to 99")
x2[0, 0] = 99
print("After modification:")
print(x2)