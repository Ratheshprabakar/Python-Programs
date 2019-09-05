#Python program to check whether the number is a palindrome or not
def palindrome(a):
	if(a[::-1]==a):
		print(a,"is palindrome")
	else:
		print(a,"is not a palindrome")
def main():
	a=input("Enter a number")
	palindrome(a)
if __name__=='__main__':
	main()

