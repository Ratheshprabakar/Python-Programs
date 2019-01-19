#Program to count no. of vowels in the string
def main():
	x=input("Enter a string")
	b={'a','e','i','o','u'}
	for i in b:
	    y=x.count(i);
	    if(y>0):
	       print(i,"present",y,"times")
if __name__=='__main__':
	main()
