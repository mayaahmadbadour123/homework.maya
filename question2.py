binary_number=[]
num=int(input("enter decimal number:"))
n=num
while n!=0:
    remind=n%2
    binary_number.append(remind)
    n=n//2
    binary_number.reverse()
    x=" "
    for i in binary_number:
        x=x+str(i)
print(x)
