#Python program to check whether the year is leap or not using inbuilt function
import calendar
def main():
	x=int(input("Enter the year"))
	if calendar.isleap(x):
		print(x,"is leap year")
	else:
		print(x,"is not a leap year")
if __name__=='__main__':
	main()
	
