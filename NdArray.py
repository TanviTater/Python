import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
b = np.array([3.14,6,9])
print(b)
c = np.array([1, 2, 3], dtype=np.float32)  # Specify float32 type
print(c)
d = np.array([list(range(i, i+3)) for i in [2, 4, 6]])
print(d)


print('\n\n')
print(np.zeros(10,dtype = 'int'))  # Create a length-10 integer array filled with zeros
print(np.ones((3,5), dtype = 'float'))  # Create a 3x5 float array filled with ones
print(np.full((3,5),3.14)) # Create a 3x5 float array filled with 3.14
print(np.arange(0, 20, 2))  # Create an array with values from 0 to 20 with a step of 2
print(np.linspace(0, 1, 5))  # Create an array with 5 evenly spaced values between 0 and 1
print(np.random.random((3,3)))  # Create a 3x3 array with random floats between 0 and 1
print(np.random.normal(0, 1, (3, 3)))  # Create a 3x3 array with random floats from a normal distribution with mean 0 and std dev 1
print(np.random.randint(0, 10, (3, 3)))  # Create a 3x3 array with random integers between 0 and 10
print(np.eye(3))  # Create a 3x3 identity matrix
print(np.empty((2, 3)))  # Create an empty array with shape (2, 3), values are uninitialized