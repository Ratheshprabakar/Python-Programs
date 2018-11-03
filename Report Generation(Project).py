def adding_report(b):
    total=0
    if(b.lower()=="t"):
        x=0
        while(x!="q"):
            x=input("Enter a integer or Q to stop")
            if(x.isdigit()):
                total+=int(x)
            elif x.lower()!="q":
                print(x,"is invalid")
            else:
                break
        return total
    elif b.lower()=="a":
        x=0
        while x!="q":
            x=input("Enter a integer ot Q to stop")
            if(x.isdigit()):
                print(x)
                total+=int(x)
            elif x.lower()!="q":
                print(x,"is invalid")
            else:
                break

        return total

b=input("Enter the type of A for all details & T for total ")
if (b.lower()=="t"):
    y=adding_report(b)
    print("TOTAL\n",y)
elif b.lower()=="a":
    z=adding_report(b)
    print("TOTAL\n",z)
else:
    print("Enter the valid symbol")

