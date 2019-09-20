#Python program to Find the factorial of a number
def  main():
	x=1
	a=int(input("Enter a number"))
	for i in range (1,a+1):
		x=x*i
	print("The factorial of",a,"is",x)
if __name__=='__main__':
	main()
