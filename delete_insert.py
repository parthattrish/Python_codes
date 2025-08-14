#to delete or insert the data in data frames:
import pandas as pd
var2 =pd.DataFrame({"a":[1,2,3,4,5],
                   "b":[54,3,42,9,8],
                   "c":[23,73,45,24,5]})
print(var2)
#inserting the data
#var2.insert(index,"column name",data to be inserted)
var2.insert(1,"new",[9,8,7,6,5])
print("the data after insertion is :\n",var2)
#for deleting we use pop function or delete function
'''it returns the set of values to be deleted and the deletetion also takes place!'''
print("the print function returns :")
x=var2.pop("b")
print(x)
print("dataframe after deleting the value:")
print(var2)
#by delete function
del var2["a"]
print(var2)