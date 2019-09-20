# Python program to Find Numbers divisible by Another number
def main():
	x=int(input("Enter the number"))
	y=int(input("Enter the limit value"))
	print("The Numbers divisible by",x,"is")
	for i in range(1,y+1):
		if i%x==0:
			print(i)
if __name__=='__main__':
	main()
	
