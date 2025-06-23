import numpy as np  
print("Array Slicing : accessing subarrays  and modifying elements \n")
x = np.arange(10)
print("Original array:", x)
print("Slicing the first 5 elements:", x[:5])  # First 5 elements
print("Slicing elements from index 5 to the end:", x[5:])   # Elements from index 5 to the end
print("Slicing elements from index 2 to 7:", x[2:7])  # Elements from index 2 to 7
print("Slicing elements with a step of 2:", x[::2])  # Elements with a step of 2
print("Slicing the last 3 elements:", x[-3:])  # Last 3 elements
print("Reversing the array:", x[::-1])  # Reversing the array
print("Reversed array with a step of 2:", x[::-2])  # Reversed array with a step of 2
print("Reversing the last 5 elements:", x[:-6:-1])  # Reversing the last 5 elements
print("Reversing the first 5 elements:",x[:5][::-1])  # Reversing the first 5 elements
print("Reversed every other from index 5:", x[5::-2])  # Reversed array from index 5 to the end

print("\n\n")
# 2D array slicing
x2 = np.random.randint(10, size=(3, 4))  # Create a 2D array with shape (3, 4)
print("Original 2D array:\n", x2)
print("Slicing the first row:", x2[0, :])  # First row
print("Slicing the first column:", x2[:, 0])  # First column
print("Slicing the first two rows and first three columns:\n", x2[:2, :3])  # First two rows and first three columns
print("Slicing the last two rows and last two columns:\n", x2[-2:, -2:])  # Last two rows and last two columns
print("Slicing all rows and the last column:\n", x2[:, -1])  # All rows and the last column
print("Slicing all rows and every other column:\n", x2[:, ::2])  # All rows and every other column
print("Reversing all rows and columns:\n", x2[::-1, ::-1])  # Reversing all rows and columns