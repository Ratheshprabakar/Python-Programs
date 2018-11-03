#Concatnation of two strings
#To find the number of characters in the concatenated string
first_string=input("Enter the 1st string")
second_string=input("Enter the 2nd string")
two_string=first_string+second_string
print(two_string)
c=0
for k in two_string:
    c+=1
print("No. of charcters in string is",c)
