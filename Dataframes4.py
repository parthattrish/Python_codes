#DataFrames by series
import pandas as pd
'''creating a series in the dictionaries and then passing it to dataframes:'''
sr={"s":pd.Series([1,2,3,4,5]),
   "p":pd.Series([4,3,2,6,2])}
var=pd.DataFrame(sr)
print(var)
print(type(var))