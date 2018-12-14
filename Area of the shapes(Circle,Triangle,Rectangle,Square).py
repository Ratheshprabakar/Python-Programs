#Python program to calculate the area of square,rectangle,triangle,circle
import math
def square(size):
    return size*size
def circle(radius):
    return (math.pi)*radius*radius
def triangle(breadth,height):
    return (1/2)*breadth*height
def rectangle(length,breadth):
    return length*breadth
def main():
    x=int(input("THE AREA OF THE SHAPES\n1.Square\n2.Rectangle\n3.Triangle\n4.Circle\nEnter your choice\t"))
    if(x==1):
        size=int(input("Enter the size of the square"))
        y=square(size)
        print("The Area of the square is\t",round(y,2))
    elif(x==2):
        length=int(input("Enter the Length of the rectangle\t"))
        breadth=int(input("Enter the Breadth of the rectangle\t"))
        y=rectangle(length,breadth)
        print("The Area of the rectangle is\t",round(y,2))
    elif(x==3):
        breadth=int(input("Enter the Breadth of the triangle\t"))
        height=int(input("Enter the Height of the triangle\t"))
        y=triangle(breadth,height)
        print("The Area of the Triangle is\t",round(y,2))
    elif(x==4):
        radius=int(input("Enter the radius of the circle\t"))
        y=circle(radius)
        print("The Area of the Circle is\t",round(y,2))
    else:
        print("Invalid Choice\t")
if __name__=='__main__':
    main()
    