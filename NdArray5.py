import numpy as np
np.random.seed(0) # Set seed for reproducibility
x2 = np.random.randint(10, size=(3, 4))  # Create a 2D array with shape (3, 4)
print("original array:\n", x2)
x2_sub = x2[:2, :2]  # Create a subarray from the original array
print("sub array:\n", x2_sub)
x2_sub[0, 0] = 99  # Modify an element in the subarray
print("After modifying the subarray:")
print(x2_sub)
print("Original array after modifying the subarray:")
print(x2)  # The original array is also modified because the subarray is a view 

print("\n\n")
# Create a copy of the subarray to avoid modifying the original array
x2_sub_copy = x2_sub.copy() 
print("Subarray copy before modification:\n", x2_sub_copy)
x2_sub_copy[0, 0] = 88  # Modify an element in the copied subarray
print("After modifying the subarray copy:")
print(x2_sub_copy)  
print("Original array after modifying the subarray copy:")
print(x2)  # The original array remains unchanged because the subarray copy is independent