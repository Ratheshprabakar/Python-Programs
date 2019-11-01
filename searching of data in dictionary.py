def main():
  d={"1718131":"Rathesh P","1718133":"Shakthi Prasath M","1718101":"Aarthi S V"}
  a=input("Enter the Register number\t")
  for i in d:
    if (a==i):
      print("Welcome",d[i])
    else:
      print("Oops!! Enter the valid register number")
if __name__=='__main__':
  main()
