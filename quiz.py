print("Kaun banega crorepati me aapka swagat hai")
confirmation=input("Do you want to play?")
a=confirmation.upper()
if a!="YES":
    print("thank you for your time")
    quit()
else:
    print("ok lets play :)")
    name=input("Enter your name")
    print(f"the game is on {name}")
    q=["what does cpu stand for?","what is the capital of india?","india is in which continent?"]
    a=["CENTRAL PROCESSING UNIT","DELHI","ASIA"]
    score=0
    total_q=len(q)
    for i in range(1,len(q)+1):
        print(f"the {i} question on your screen is \t")
        print(q[i-1])
        answer=input("Enter your answer")
        final_answer=answer.upper()
        if final_answer==a[i-1]:
            print("The answer is correct")
            score+=1
        else:
            print("the answer is incorrect")
    print("the next question on your screen is:",end="\t")
print(f"the game is over you hae got {score} answers correct out of {total_q} thus the percentage of correct answers are {(score/total_q)*100}")

