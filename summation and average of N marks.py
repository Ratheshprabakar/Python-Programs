#Python program for sum and average of N numbers
def summation(n):
    total_marks=0
    for i in range(1,n+1):
        marks=int(input("Subject Mark=\t"))
        total_marks+=marks
    return total_marks
def average(total_marks,n):
    average=total_marks/n
    return average
def main():
    n=int(input("Enter No. of subjects\t"))
    x=summation(n)
    y=average(x,n)
    print("\nThe Sum of",n,"subject is:\t",x,"\nThe Average of",n,"subject is:\t",round(y,2))
if __name__=='__main__':
    main()

    