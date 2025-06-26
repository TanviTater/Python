#For DatFrames
import numpy as np
import pandas as pd
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'Area' : area,'Population' : pop})
print("Data -> ")
print(data)
print("\nAccessing Individual Series : ")
print("Area -> \n",data['Area'])
print("\nPopulation -> \n",data['Population'])
print(data.Area is data['Area'])
print("\n-----------------Modifying Data -----------------\n")
data['Density'] = data['Population']/data['Area']
print("Updated Data -> \n",data)
print("\n-----------------DataFrame as two-dimensional array -----------------\n")
print(data.values)
print("Transpose of data -> \n",data.T)
print("\nData of the 0th row -> ",data.values[0])
print("\nData of the Area of all -> \n",data['Area'])
print("\n-----------------Using Indexers-----------------\n")
print("Using iloc : \n",data.iloc[:4, :2])
print("Using loc : \n",data.loc[:'Florida',:'Population'])
print("Accessing based on condition : \n",data.loc[data.Density>100,['Population','Density']])
print("\n-----------------Modifying Values-----------------\n")
data.iloc[0,2]=90
print("Updated Data -> \n",data)
print("\n-----------------while indexing refers to columns, slicing refers to rows-----------------\n")
print("Example -> \n",data['Texas' : 'New York'])
print("\nExample2 -> \n",data[1:3])