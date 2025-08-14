#sum of 2 lists and error(difference btwn array and series)
import pandas as pd
a=[1,3,2,3,]
b=[2,5,6,4,3]
x=pd.Series(a)
y=pd.Series(b)
print(x)
print(y)
print(x+y)
'''here the data in a is less than that of b so NaN is shown at those respective points where as in case of
arrays it gives error'''
