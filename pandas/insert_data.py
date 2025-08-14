#to insert a new dataset in dataframe by copying from another colmn upto a certain index :
import pandas as pd
var=pd.DataFrame({"a":[1,2,3],
                  "b":[4,5,6],
                  "c":[7,8,9]})
print("before adding data :")
print(var)
var["new"]=var["a"][:2]
print("after adding data,the data is added upto index 1 :\n")
print(var)
