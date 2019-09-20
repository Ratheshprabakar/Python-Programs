#Python program to make a Simple calculator
def main():
	x=int(input("Enter your choice\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
	number1=int(input("Enter the First number\t"))
	number2=int(input("Enter the Second number\t"))
	operations(number1,number2,x)
def operations(number1,number2,x):
	if x==1:
		print("The Sum of two numbers are\t",number1+number2)
	elif x==2:
		if number2>=number1:
			print("The Difference between two numbers are\t",number2-number1)
		else:
			print("The Difference between two numbers are\t",number1-number2)
	elif x==3:
		print("The Product of two numbers are\t",number1*number2)
	elif x==4:	
		print("The division of two numbers are\t",number1//number2)
	else:
		print("\nInvalid Choice\n")
if __name__=='__main__':
	main()

