#changing the indexes in dataframes
import pandas as pd
d={"a":[1,2,3,4,5],
   "b":[6,7,8,9,10],
    1:[2,5,7,3,5]}
var=pd.DataFrame(d,columns=["a",1],index=['a','b','c','d','s'])
print(var)
#here we printed onnly column 1 and a not including b also changed the indexes
print(var["a"][1])  #to get the value at any loctaion in the dataframe :var[column][row]