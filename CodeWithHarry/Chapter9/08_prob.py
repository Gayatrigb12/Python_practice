import random

def game():
    print("You are playing game ..")
    score = random.randint(1,100) # random score 
    print(f"your score {score}")
    with open("score.txt") as f:
        high_score = f.read()
        if(high_score!=""):
            high_score = int(high_score) # file read in form of string for that use int 
        else:
            high_score = 0
    if(score > high_score or high_score==""):
        # write hiScore in file 
        with open("score.txt" , "w") as f:
            f.write(str(score))# writting score in file
            
    return score

game()