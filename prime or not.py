#prime number or not
x=int(input("Enter a number"))
i=2
c=0
while i<x:
    if x%i==0:
        c=1
        break
    i+=1
if c==0:
    print(x,"is a prime number")
else:
    print(x,"is not a prime number")