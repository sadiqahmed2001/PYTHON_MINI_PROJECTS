import random

target=random.randint(1,100)

while True:  
    userchoice=int(input("guess the target or quite(00): "))
    if (userchoice==00):
        print("user want to quite the game")
        break
#    userchoice=int(userchoice)
    if(userchoice==target):
        print("successfull: your guess is corerct!!!")
        break
    elif(userchoice<target):
        print("your number is too small. take a bigger guess...")
    else:
        print("your number is too big, take a smaller number: ")
   
print("----GAME OVER---")