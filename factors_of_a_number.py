#Python programs to Find Factors of Number
def main():
	x=int(input("Enter the number"))
	print("The Factors of",x,"is given by")
	for i in range(1,x+1):
		if (x%i==0):
			print(i)
if __name__=='__main__':
	main()

