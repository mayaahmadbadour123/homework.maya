nam= ['maya badour','ali mohamad','roaa badour','ghaith badour','zohor']
name4= input("enter name:")
if (name4 in nam):
    print('grad')
else:
    print('not grad')
    
mk=[m for m in range(1001) if m%2==1]
print(mk)


l=['Network','Math','Proramming','Physics','Music']
x=l[2:4]
print(x)


x=1
b=(x:x**2 for x in range(1,11,1))
print(b)