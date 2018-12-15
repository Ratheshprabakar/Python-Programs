#Python program to assign grade to mark
def grade(mark):
    assert mark>=0 and mark<=100
    if (mark>=90):
        return 'O'
    elif(mark>=80):
        return 'A+'
    elif(mark>=70):
        return 'A'
    elif(mark>=55):
        return 'B+'
    elif(mark>=45):
        return 'B'
    else:
        return "You are Fail"
def main():
    mark=int(input("Enter the Mark\t"))
    x=grade(mark)
    if(x!="You are Fail"):
        print("The Mark is\t",mark,"\nThe Grade is\t",x)
    else:
        print(x)
if __name__=='__main__':
    main()
    