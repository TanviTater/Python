import numpy as np
a =np.array([1,2,3])
b = np.array([4,5,6])
print("a = ", a)
print("b = ", b)
print("a + b = ", a + b)  # Element-wise addition
print("a + 5 = ",a+5)  # Broadcasting addition
c = np.arange(3)
d = np.arange(3)[:, np.newaxis]  # Convert c to a column vector
print("c = ", c)
print("d = \n", d)
print("c + d = \n", c + d)  # Broadcasting addition with a row vector and a column vector
print("\n")
print("Broadcasting examples : \n")
print("\nExample 1: \n")
M = np.ones((2, 3))  # Create a 2x3 matrix of ones
print("M = \n", M)
print("M + a = \n", M + a)  # Broadcasting a 1D array to a 2D matrix
print("\nExample 2: \n")
A = np.arange(3).reshape((3, 1))  # Create a 3x1 column vector
B = np.arange(3)  # Create a 1D array
print("A = \n", A)
print("B = \n", B)
print("A + B = \n", A + B)  # Broadcasting addition
print("\nExample 3: IT WILL GIVE ERROR \n")
C = np.ones((3, 2))  # Create a 3x2 matrix of ones
D = np.arange(3)  # Create a 1D array
print("C = \n", C)
print("D = \n", D)
try:
    print("C + D = \n", C + D)  # This will raise an error due to shape mismatch
except ValueError as e:
    print("Error:", e)