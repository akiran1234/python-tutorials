# modules
# json, csv, logging, datetime, os, sys,random,

# pickling is the process of writing the state of an object to file and writing back from file to object is un pickiling.
# import pickle;


print(format(12, "08b")) # creating whole number to binary, 08b leading zero and total length 8.
print(int('1111',2))     # creating binary number to whole number.
print(abs.__doc__)       # doc string used against a fuction to get the info.

# n+nn+nnn
n=5
n1=n
n2=int("{0}{0}".format(n))
n3=int("{0}{0}{0}".format(n))
print(n1,n2,n3,n1+n2+n3)
