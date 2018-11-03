#To find whether the number is +ve,-ve or 0
x=int(input("Enter a number"))
def check_num(x):
    if x>0:
        print("The",x,"is positive")
    elif x<0:
        print("The",x,"is negative")
    else:
        print("The",x,"is zero")
check_num(x)
