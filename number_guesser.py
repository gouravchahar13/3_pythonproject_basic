import random as r


n=int(input("enter the range of number till u want to guess the number\t"))

random_number=r.randint(0,n)

user_input=int(input("enter the number to guess"))
  
if user_input==random_number :
        print(" Congratulations !!! You have guessed the number correctly")

elif user_input <random_number :
        print("you have entered the number greater than the expected value")
        
else:
        print("you have entered the number less than the expected value")
    

    
