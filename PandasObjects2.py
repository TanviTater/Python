#Dataframes
import pandas as pd
import numpy as np
print("A Pandas DataFrame is a two-dimensional array of indexed data\n")
print("DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column names\n")
print("You can think of a DataFrame as a sequence of aligned Series objects. Here, by ALIGNED we mean that they share the same index.\n")
area_dict ={
    'California': 423967,
    'Texas': 695662,
    'Florida': 170312,
    'New York': 141297,
    'Illinois': 149995
}
population_dict = {
    'California': 38332521,
    'Texas': 26448193,
    'Florida': 19552860,
    'New York': 19651127,
    'Illinois': 12882135
}
print("area_series = ", pd.Series(area_dict))
print("\npopulation_series = ", pd.Series(population_dict))
# Creating a DataFrame from two Series
print("\n")
states = pd.DataFrame({'Population' : pd.Series(population_dict),
                      'Area' : pd.Series(area_dict)})
print("DataFrame from two Series:\n", states)
print("Index of DataFrame:\n", states.index)
print("\n\nDataFrame has a columns attribute, which is an Index object holding the column labels:\n", states.columns)
print("\nDataframe as a Specialised Dictionary\n")
print("DataFrame maps a column name to a Series of column data\n")
print("Population Series:\n", states['Population'])  # Accessing a column as a Series       
print("\nArea Series:\n", states['Area'])  # Accessing another column as a Series
print("\nAccessing multiple columns:\n", states[['Population', 'Area']])  # Accessing multiple columns
print("\nPopulation of California:", states['Population']['California'])  # Accessing value by index
print("Area of Texas:", states['Area']['Texas'])  # Accessing value by index
print("\nSlicing DataFrame:\n", states[1:3])  # Slicing the DataFrame
print("\nSlicing DataFrame by index:\n", states.loc['California':'Florida'])
print("\n Creating DataFrame Objects \n")
print("From a single Series:\n")
population_dataframe = pd.DataFrame(pd.Series(population_dict), columns=['Population'])
print(population_dataframe)
print("\n From a list of dicrtionaries:\n")
data = [{'a':i,'b':2*i}
    for i in range(5)]
print(pd.DataFrame(data))
print("\nEven if some keys in the dictionary are missing, Pandas will fill them in with NaN (i.e., not a number) values\n")
print(pd.DataFrame([{'a':1,'b':2},{'b':3,'c':4}]))
print("\nFrom a dictionary of Series Objects:\n")
print(pd.DataFrame({'Population':pd.Series(population_dict),'Area':pd.Series(area_dict)}))
print("\nFrom a 2-D NumPy Array :\n")
data_array = pd.DataFrame(np.random.rand(3,2),columns=['A','B'],index=['a','b','c'])
print(data_array)
print("From a Structured NumPy Array:\n")
A = np.zeros(3, dtype=[('a', 'i4'), ('b', 'f4' )])
print(pd.DataFrame(A))