import random as r
user_wins=0
computer_wins=0
while True:
    user_input=input("enter your choice rock or paper or scissor type Q to quit").upper()
    if user_input=="Q":
        break
    else:
        if user_input not in ["ROCK","PAPER","SCISSOR"]:
            print("the input is invalid! Please type again")
            continue
        else:
            choice=["ROCK","PAPER","SCISSOR"]
            r1=r.randint(0,2)
            computer_choice=choice[r1]

            if user_input=="ROCK" and computer_choice=="SCISSOR":
                user_wins+=1
                print(f"You beat the machine !! :)")
            elif user_input=="PAPER" and computer_choice=="ROCK":
                user_wins+=1
                print(f"You beat the machine !! :)")
            elif user_input=="SCISSOR" and computer_choice=="PAPER":
                user_wins+=1
                print(f"You beat the machine !! :)")
            elif user_input==computer_choice:
                print("it is a draw!!")
            else:
                print("You lost!!:(")
                computer_wins+=1
                
print(f"you have won {user_wins} time the computer has won {computer_wins} times")

print("GOODBYE!!! SEE U NEXT TIME")
quit()
