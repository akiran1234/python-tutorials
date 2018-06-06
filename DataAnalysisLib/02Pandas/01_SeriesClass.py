# Pandas
#
import numpy as np
import pandas as pd



# Panda Series will take two args data and label(Index) as inputs and displayed at the output.

l1=[10,20,30,40,50]
lab=['a','b','c','d','e']


# print(pd.Series(l1,lab))   # Here l1 is data and lab is label which will be displayed as index.
# print(pd.Series(l1))       # Always label i.e is index is displayed as first column. If label is not provided it will display default index.
# print(pd.Series(data=lab)) # Data field is assigned with lab then it displayed default index.

a1=np.array([1,2,3,4,5])
a2=np.array([6,7,8,9,10])
loc1=['hyd','blr','del','pune','chn']
loc2=['rjy','vjw','hyd','blr','del']

s1=pd.Series(a1,loc1)
s2=pd.Series(a2,loc2)

print("Series1=",s1,sep='\n')
print("Series2=",s2,sep='\n')

# Operations on Series; s1+s2, s1-s2, s3*s4 so on and so forth ..

print(s1+s2) # It will check for the matching labels and it will do sum and for non matching it will result Null(NaN)

