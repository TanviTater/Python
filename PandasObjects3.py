#index object
import pandas as pd 
import numpy as np
print("An Index object is an immutable array that holds the axis labels for a Series or DataFrame. It may contain repeated values")
print("It is used to label the rows and columns of a DataFrame or Series, providing a way to access and manipulate data efficiently.\n")
print("Creating index from a list of Integers: ")
index = pd.Index([2,5,7,9,0])
print(index)
print("Accessing 0th element in the index:",index[0])  # Accessing the first element
print("Slicing the index from 1st to 3rd element:", index[1:4])  # Slicing the index
print("Accessing elements wiith a step of 2:", index[::2])  # Accessing elements with a step of 2
print("Size , Shape , Dimensions , Datatype : ",index.size, index.shape, index.ndim, index.dtype)
print("\nCreating index from a list of Strings: ")
index_str = pd.Index(['a', 'b', 'c', 'd', 'e'])
print(index_str)
print("\n\nIndex as Ordered Set of Labels: ")  
indA = pd.Index(['a', 'b', 'c', 'd'])
indB = pd.Index(['c', 'd', 'e', 'f'])
indC = pd.Index([0,2,4,6,8])
print("Index A:", indA)
print("Index B:", indB)
print("Index C:", indC)
print("Union of Index A and B:", indA.union(indB))  # Union of two indices
print("Union of Index A and C:", indA.union(indC))  # Union of two indices
print("Difference of Index A and B:", indA.difference(indB))  # Difference of two indices
print("Difference of Index A and C:", indA.difference(indC))  # Difference of two indices
print("Intersection of Index A and B:",indA.intersection(indB))  # Intersection of two indices
print("Intersection of Index A and C:", indA.intersection(indC))  # Intersection of two indices