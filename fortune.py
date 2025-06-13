import random
def get_ans(answerNum):
    if(answerNum ==1):
        return "Yes , definitely"
    elif(answerNum ==2):
        return "It is decidedly so" 
    elif(answerNum ==3):
        return "Without a doubt"
    elif(answerNum ==4):    
        return "Reply hazy, try again"  
    elif(answerNum ==5):
        return "Ask again later"    
    elif(answerNum ==6):
        return "Better not tell you now"    
    elif(answerNum ==7):
        return "My sources say no"
    elif(answerNum ==8):
        return "Outlook not so good"
    elif(answerNum ==9):
        return "Very doubtful"
    else:
        return "Error: Invalid answer number"
r = random.randint(1,9)
fortune = get_ans(r)
print(fortune)