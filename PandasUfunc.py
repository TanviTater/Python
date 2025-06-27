import numpy as np
import pandas as pd
rnd = np.random.RandomState(42)
ser = pd.Series(rnd.randint(0,10,4))
print("THe series is : \n",ser)
df = pd.DataFrame(rnd.randint(0,10,(3,4)) , columns = ['A','B','C','D'])
print("The datafRame is : \n",df);
print("\n---------------Applying UFunctions ---------------------\n")
print("Exponentiation :\n",np.exp(ser));
print("Trigonometric function : \n",np.sin(df * np.pi / 4));
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')
print("Population/Area : \n",population/area)
print("Understanding its index : ", area.index.union(population.index))
print("\nUnderstanding NaN -> Not A Number \n")
A = pd.Series([2,4,6],index=[0,1,2])
B = pd.Series([1,3,5],index=[1,2,3])
print("A -> ",A)
print("B -> ",B)
print("Addition of A and B -> \n",A+B)
print("\n PLacing 0 in places of Nan \n");
print(A.add(B,fill_value=0))
print("\n---------------Index Alignment in DataFrames ---------------------\n")
a= pd.DataFrame(rnd.randint(1,20,(2,2)),columns=list('AB'));
b = pd.DataFrame(rnd.randint(1,10,(3,3)),columns = list('BAC'));
print(a)
print(b)
print(a+b)
print("Filling the NaN Values ")
fill = a.stack().mean();
print(a.add(b,fill_value=fill))
print("\n---------------UFunc Diff in NumPy and Pandas--------------------\n")
X = rnd.randint(10,size=(3,4));
print(X)
print("Row-Wise Subtraction : X-X[0]\n",X-X[0])
print("\n IN Pandas")
df = pd.DataFrame(X,columns=list('ABCD'))
print(df)
print("Row-Wise Subtraction : df-df.iloc[0]\n",df-df.iloc[0])
print("Column-wise Subtraction : df.subtract(df['R'],axis = 0)\n",df.subtract(df['B'],axis = 0))
halfRow =df.iloc[0,::2]
print("halfRow  : \n",halfRow)
print("df-halfRow : \n",df-halfRow)