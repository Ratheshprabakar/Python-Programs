#Python program to print the yearly calender for particular year
import calendar
def main():
	x=int(input("Enter the year"))
	for i in range(1,13):
		print(calendar.month(x,i))
if __name__=='__main__':
	main()
