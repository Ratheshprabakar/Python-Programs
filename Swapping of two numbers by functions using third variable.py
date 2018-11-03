#swapping of two numbers
a=int(input("Enter the number for a"))
b=int(input("Enter the number for b"))
def before_swap(a,b):
    print("The value of a and b before swapping",a,b)
def after_swap(a,b):
    c=a
    a=b
    b=c
    print("The value of a and b after swapping",a,b)
before_swap(a,b)
after_swap(a,b)
