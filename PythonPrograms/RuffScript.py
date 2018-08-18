import pandas as pd
l=[10,20,30,40,50]
d={'name':'Kiran','id':100,'sal':1000.50}              # When dict is passed as data key values will be taken as index.

# s1=pd.Series(l,index=['a','b','c','d','e'])          # Creating Series from a list.
# print(s1)

s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])  # Passing data and index directly
#print(s2)

s3= pd.Series(5,['a','b','c','d','e'])                 # Passing constant value with index values.
print(s3)