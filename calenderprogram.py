#Python program to display calender for particular month
import calendar
def main():
	x=int(input("Enter Month:\t"))
	y=int(input("Enter Year:\t"))
	print(calendar.month(y,x))
if __name__=='__main__':
	main()
