import pandas as pd
d={"a":[1,2,3,4,5],
   "b":[6,7,8,9,10]}
var=pd.DataFrame(d)
print("SHOWING THE DATAFRAME CREATED:")
print(var)
print(type(var))
#if we want to see only column a then:
var2=pd.DataFrame(d,columns=["a"])
print("only showing the desired COLUMNS(a):")
print(var2)