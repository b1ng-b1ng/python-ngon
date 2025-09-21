import pandas as pd
print(pd.__version__)
s = [1,2,3]
sp = pd.Series(s,index=["a","b","c"])
print(sp)