def input_string():
        n=input("Enter the string")
        for i in range(len(n)):
                for j in range(len(n)):
                      if i==j :
                           print(n[i],end=' ')
                      elif i+j==len(n)-1:
                           print(n[i],end=' ')
                      else:
                         print(end=' ')
                print("\r")
if __name__=='__main__':
        input_string()
        
