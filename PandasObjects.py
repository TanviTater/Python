# series ,dataframe and index
import pandas as pd
import numpy as np
print("A Pandas Series is a one-dimensional array of indexed data")
data = pd.Series([1,2,3,4,5])
print("Series:\n", data)
print("\nAs we see in the output, the Series wraps both a sequence of values and a sequence of indices, which we can access with the values and index attributes.\n")
print("Values:\n", data.values)
print("Index:\n", data.index)
print("Value at index 2:", data[2])  # Accessing value at index 2
print("Slicing Series:\n", data[1:4])  # Slicing the Series
print("\nThe index need not be an integer, but can consist of values of any desired type")
data2 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print("Series with custom index:\n", data2)
print("Value at index 'c':", data2['c'])  # Accessing value at index 'c'
print("Slicing Series with custom index:\n", data2['b':'d'])
print("\nWe can even use non-contiguous or non-sequential indices")
data3 = pd.Series([1,2,3,4,5],index=[0,2,4,6,8])
print("Series with non-contiguous index:\n", data3)
print("\n Series as a dictionary\n")
population_dict = {
    'California': 38332521,
    'Texas': 26448193,  
    'Florida': 19552860,
    'New York': 19651127,
    'Illinois': 12882135
}
population_series = pd.Series(population_dict)
print("Population Series:\n", population_series)
print("Population of Texas:", population_series['Texas'])  # Accessing value by key
print("Population of California and Florida:\n", population_series[['California', 'Florida']])  # Accessing multiple values
print("Population from California to Florida:\n", population_series['California':'Florida'])  # Slicing by index
print("\nConstructing pandas Objects from NumPy arrays\n")
# Creating a Series from a NumPy array
array_data = np.random.randint(1,10,size = 5)  # Random integers between 1 and 10
series_from_array = pd.Series(array_data)   
print("Series from NumPy array:\n", series_from_array)
print("\n Creating Series Objects \n ")
#pd.Series(data ,index = Index)
print(pd.Series([1,2,3] , index = ['A','B','C']))
print(pd.Series(5,index=[100, 200, 300]))  # Single value with custom index
print(pd.Series({2:'a', 1:'b', 3:'c'}))
print(pd.Series({2:'a', 1:'b', 3:'c'} ,index = [3,2]))