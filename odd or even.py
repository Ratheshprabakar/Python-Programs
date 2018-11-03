x=input("Enter your name")
vowels="a,e,i,o,u"
c=0
d=0
for y in x:
    if(y in vowels):
        c+=1
    else:
        d+=1
print("The vowels present in",x,"is",c,"\nThe Consonants present in",x,"is",d)


