#dictionary in series
import pandas as pd
d={
   " hero": ["aaloo","poori","kajukatli"],
   "tillu":["teeka",1,23,3]
}
a=pd.Series(d)
print(a)