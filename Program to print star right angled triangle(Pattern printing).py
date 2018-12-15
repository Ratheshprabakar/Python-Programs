#Python program to print right angled triangle(Pattern)
def pattern(rows):
    for i in range(1,rows+1):
        print("*"*i)
def main():
    rows=int(input("Enter Number of rows"))
    pattern(rows)
if __name__=='__main__':
    main()
    
    