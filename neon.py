#Python program to check whether a number is neon or not
def main():
	sum=0
	n=int(input("Enter a number"))
	square_value=pow(n,2)
	x=str(square_value)
	for i in x:
		sum=sum+int(i)
	if sum==n:
		print(n,"is a neon number")
	else:
		print(n,"is not a neon number")
if __name__=='__main__':
	main()
