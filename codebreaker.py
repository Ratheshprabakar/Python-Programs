#Python program - CODEBREAKER
#This is a game with three possibilities ---Nope--Close--Match--- 
import random
def main():
   #x=str(random.randint(100,101))
    x=str(100)
    number=str(input("Welcome to CODEBREAKER !!! The three digit value is generated, make a guess"))
    if(x==number):
        print("Congratulations!!Your guess may wrong but not this time, NUMBER MATCH")
    else:
        count =0
        for i in x:
            if i in number:
                count=count+1
                print(i)
        if count ==3:
            print("Almost correct guess but position mismatch, CLOSE")
        else:
            print("OOPS!! Your guess is wrong at this time TRY AGAIN!!","The correct number is",x)
if __name__ =='__main__':
    main()
