import numpy as np  
x = np.array([1,2,3,4,5,6,7,8,9,10])  # Create a 1D array
print("Original array:", x)
print("x>3",x>3)
print("x>=3",x>=3)
print("x<3",x<3)
print("x<=3",x<=3)
print("x==3",x==3)
print("x!=3",x!=3)
print("(2 * x) == (x ** 2)", (2 * x) == (x ** 2))  # Element-wise comparison
print("x % 2 == 0", x % 2 == 0)  # Check if elements are even
print("\n Working with 2D arrays:\n")
rng = np.random.RandomState(0)
x = rng.randint(10,size = (3,4))  # Create a 2D array with shape (3, 4)
print("Original 2D array:\n", x)
print("x > 5:\n", x > 5)  # Element-wise comparison
print("x < 5:\n", x < 5)  # Element-wise comparison
print("Count the number of True entries or values greater than 5 : ",np.count_nonzero(x > 5))  # Count the number of True entries
print("Another way to count the number of True entries or values greater than 5 : ",np.sum(x > 5))  # Count the number of True entries
print("Count the number of False entries or values less than 5 : ",np.count_nonzero(x < 5))  # Count the number of False entries
print("Another way to count the number of False entries or values less than 5 : ",np.sum(x < 5))  # Count the number of False entries
print("Count the number of entries or values equal to 5 : ",np.count_nonzero(x == 5))  # Count the number of entries equal to 5
print("Another way to count the number of entries or values equal to 5 : ",np.sum(x == 5))  # Count the number of entries equal to 5
print("\n")
print("Count of values less than 5 in each row: ", np.sum(x < 5, axis=1))  # Count of values less than 5 in each row
print("Are there any values greater than 8",np.any(x > 8))  # Check if there are any values greater than 8
print("Are there any values less than 2",np.any(x < 2))  # Check if there are any values less than 2
print("Are all values greater than 0",np.all(x > 0))  # Check if all values are greater than 0
print("Are all values less than 10",np.all(x < 10))  # Check if all values are less than 10
print("Are all values equal to 5",np.all(x == 5))  #  Check if all values are equal to 5
print("Are all values equal to 5 in each row: ", np.all(x == 5, axis=1))  # Check if all values are equal to 5 in each row
print("Are all values equal to 5 in each column: ", np.all(x == 5, axis=0))  # Check if all values are equal to 5 in each column
print("\nSelecting elements based on a condition x>5 : ", x[x > 5])  # Select elements greater than 5
print("Selecting elements based on a condition x<5 : ", x[x < 5])  # Select elements less than 5
print("Selecting elements based on a condition x==5 : ", x[x == 5])