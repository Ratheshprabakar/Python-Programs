#Python Program to calculate the area of the rectangle
def rectangle(length,breadth):
    area=length*breadth
    return area
def main():
    length=int(input("Enter the length\t"))
    breadth=int(input("Enter the breadth\t"))
    x=rectangle(length,breadth)
    print("The Area of the rectangle is",round(x,2))
if __name__=='__main__':
    main()