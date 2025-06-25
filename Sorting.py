import numpy as np
def selection_sort(values):
    for i in range(len(values)):
        swap = i+np.argmin(values[i:])
        (values[i], values[swap]) = (values[swap], values[i])
    return values   
def bogo_sort(values):
    while np.any(values[:-1] > values[1:]):
        np.random.shuffle(values)
    return values
values = np.array([5, 2, 9, 1, 5, 6])   
print("Original array:", values)
sorted_values = selection_sort(values)
print("Sorted array using selection sort:", sorted_values)
sorted_values_bogo = bogo_sort(values.copy())
print("Sorted array using bogo sort:", sorted_values_bogo) 
print("Bogo sort is not efficient and may take a long time to complete for larger arrays.")
print("\n Numpy's built in sorting function :")
sorted_values_numpy = np.sort(values)
print("Sorted array using Numpy's sort:", sorted_values_numpy)  
i = np.argsort(values)
print("ArgSort function returns the indices that would sort an array:", i)
print("Values sorted using the indices returned by argsort:", values[i])
print("\nSorting using rows and columns \n")
rand = np.random.RandomState(42)
x = rand.randint(1,10, size =  (4,6))  # Create a 2D array
print("Original 2D array:\n", x)
print("sort each column of X:\n", np.sort(x, axis=0))  # Sort each column
print("sort each row of X:\n", np.sort(x, axis=1))  # Sort each row
print("\n Partial sorting \n")
print("Partial sorting is useful when you only need the top k elements of an array.\n")
k = 3  # Number of top elements to retrieve
x = np.array([5, 2, 9, 1, 5, 6])
print("Original array:", x)
print("Top 3 smallest elements are the first three elements using np.partition:", np.partition(x,k))  # Get top k elements
x = rand.randint(1, 10, size=(4, 6))  # Create a new 2D array
print("Original 2D array:\n", x)
print("Top 3 smallest elements in each row using np.partition:\n", np.partition(x, k, axis=1))  # Get top k elements in each row
print("\n The result is an array where the first two slots in each row contain the smallest values from that row, with the remaining values filling the remaining slots.\n")