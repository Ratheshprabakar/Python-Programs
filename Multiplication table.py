#To display the multiplication table
x=int(input("Enter the table no. you want to get"))
y=int(input("Enter the table limit of table"))
print("The Multiplication table of",x,"is:")
i=1
while i<=y:
    print(i,"*",x,"=",x*i)
    i+=1
