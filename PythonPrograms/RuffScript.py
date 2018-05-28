l=[1,2,3,4]
print([x*x for x in l if x*x>4])


s={1,2,3,4}

s=set([j*j for j in s])
print(s)

x=set(zip(l,s))
print(x)