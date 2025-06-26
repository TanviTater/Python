# DataSelection In Series
import pandas as pd
import numpy as np
print("Series as Dictionaries")
data = pd.Series([1,2,3,4,5],index=['a','b','c','d','e' ])
print("Data in Series:")
print(data)
print("Accessing ath element in Series:", data['a'])  # Accessing the first element
print("Checking if 'c' is in Series:", 'c' in data)  # Checking if a key exists
print("Printing the keys in Series:", data.keys())  # Printing the keys
print("Printing the values in Series:", data.values)  # Printing the values
print("Printing in the form of list: ",list(data.items()))  # Printing the items as a list of tuples
print("Slicing the Series from 'b' to 'd':", data['b':'d'])  # Slicing the Series
print("Modifying the Series by adding 10 to each element: ")
print(data+10)
print("Adding elements to the series:" )
data['f'] = 6
print(data)
print("Deleting element 'c' from the Series:")
del data['c']   
print(data)
print("Checking if 'c' is in Series after deletion:", 'c' in data)
print("\n\nSeries as  1d array\n\n")
print(data)
print("Slicing by explicit index positions:")  # Slicing by explicit index positions
print(data['a':'d'])  # Slicing by explicit index positions
print("\n IN EXPLICIT INDEX THE FINAL INDEX IS INCLUDED\n")
print("Slicing by implicit index positions:")  # Slicing by implicit index positions
print(data[1:3])
print("\n IN IMPLICIT INDEX THE FINAL INDEX IS NOT INCLUDED\n")
print("Masking the Series with a condition data[(data > 3) & (data < 5)]:")
print(data[(data>3)&(data<5)])
print("Fancy Indexing:")
print(data[['a','e']])


print("\n\n----------------INDEXERS -> loc, iloc, and ix -------------------\n")
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print("Data -> ")
print(data)
print("\nloc attribute allows indexing and slicing that always references the explicit index i.e the indexex we have typed")
print(data.loc[1])
print(data.loc[1:3])
print("\nThe iloc attribute allows indexing and slicing that always references the implicit Python-style index")
print(data.iloc[1])
print(data.iloc[1:3])
print("\nA third indexing attribute, ix, is a hybrid of the two, and for Series objects is equivalent to standard []-based indexing. The purpose of the ix indexer will become more apparent in the context of DataFrame objects, which we will discuss in a moment.\n\n")