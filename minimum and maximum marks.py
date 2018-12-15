#Python program to calculate minimum and maximum of three marks
def minimum(x,y,z):
    p=min(x,y,z)
    return p
def maximum(x,y,z):
    q=max(x,y,z)
    return q
def main():
    x=int(input("Enter a mark1\t"))
    y=int(input("\nEnter mark2\t"))
    z=int(input("\nEnter mark3\t"))
    maximum_value=maximum(x,y,z)
    minimum_value=minimum(x,y,z)
    print("\nThe maximum mark obtained is\t",maximum_value,"\nThe Minimum mark obtained is\t ",minimum_value)
if __name__=='__main__':
    main()