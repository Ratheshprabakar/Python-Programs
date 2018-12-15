#Python program to check password authentication access
def authentication(password):
    if(password=="rathesh"):
        print("Password Match!!You are allowed to access the file")
    else:
        print("Password mismatch")
def main():
    password=input("Enter the password\t")
    authentication(password)
if __name__=='__main__':
    main()