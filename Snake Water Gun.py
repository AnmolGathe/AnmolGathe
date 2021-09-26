import random as random
rand=random.randint(1,3)

def game(dice,you):
    print(dice)
    if(you==dice):
        return None
    
    elif(dice=='s'):
     if(you=='w'):
         return False
     elif(you=="g"):
         return True
    
    elif(dice=='w'):
     if(you=='g'):
         return False
     elif(you=="s"):
         return True   
    
    elif(dice=='g'):
     if(you=='s'):
         return False
     elif(you=="w"):
         return True       
         

    
print("\t\t-----------Welcome to the game-----------\t\t")

your=input("Your Turn: Snake(s) Water(w) Gun(g)?\t\t")
you=str.lower(your)

print("Computer's Choosed-\t",end="")
if(rand==1):
    dice='s'
elif(rand==2):
     dice='w'
else:
    dice='g'

ak=game(dice,you)
if(ak==None):
    print("\t\t!!!Game Draw!!!\t\t")
elif(ak==True):
    win="!!!You Win!!!"
    print(win)
else:
    lose="!!!Better Luck Next Time!!!"
    print(lose)  #str.center(lose) not working
