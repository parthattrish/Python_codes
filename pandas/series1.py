#series are the 1 d data structures in python.
import pandas as pd
x=[1,2,3,4,5]
a=pd.Series(x)
print(a)
b=pd.Series(x,index=["a","s","d","f","e"],dtype="float",name="numbers")
print(b)
print(a[2],b[0])
