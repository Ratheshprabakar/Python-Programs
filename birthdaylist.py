#Python program to display,Creation of a birthday app
def main():
        birthdaylist={}
        while(1):
                print("---Birthday Details---")
                a=int(input("1.Birthday List\n2.Add new details\n3.Exit\n"))
                if a==1:
                        if(len(birthdaylist.keys())==0):
                                print("No details found")
                        else:
                                x=input("Enter the name\t")
                                if x in birthdaylist:
                                        print("Name:",x,"\nBirthday:",birthdaylist[x])
                                else:
                                        print("Data not found in list\n")
                elif a==2:
                        x=input("Enter the name\t")
                        y=input("Enter the Date of birth (dd/mm/yy)\t")
                        birthdaylist[x]=y
                elif a==3:
                        break;
if __name__=='__main__':
        main()
                        
                               
                                        
