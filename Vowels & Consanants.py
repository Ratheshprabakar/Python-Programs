#To find the no. of vowels and consonants in a string
x=input("Enter your name")
vowels="praveen"
c=0
d=0
for y in x:
    if(y in vowels):
        c+=1
    else:
        d+=1
print("The alphabet is present in praveen ",x,"is",c,"\nThe alphabet is not present in praveen ",x,"is",d);


