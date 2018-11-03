#To sum the N no. of natural numbers
x=int(input("Enter the N number of natural number"))
i=1
sum=0
while i<=x:
    sum+=i
    i+=1
print("The sum of the first ",x,"natural no. is",sum)