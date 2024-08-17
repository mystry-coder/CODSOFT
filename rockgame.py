from random import randrange

print("\nRock-Paper-Scissors Game")
print("***************************")
print("Game Logic:\nRock beats scissors,scissors beat paper, and paper beats rock\n")
print("1. Rock \U0001F5FF")
print("2. Paper \U0001F4C3")
print("3. Scissors \U00002702")

user_score=0;computer_score=0

while True:
    users_choice=int(input("Enter Your choice:"))
    if users_choice==1:
        user_choice_name='Rock'
    elif users_choice==2:
        user_choice_name='Paper'
    elif users_choice==3:
        user_choice_name='Scissors'
    print("User's Choice is:",user_choice_name)
    
    if users_choice == 1 or users_choice == 2 or users_choice == 3:
        computer_choice=randrange(1, 4)

        if computer_choice==1:
            computer_choice_name='Rock'
        elif computer_choice==2:
            computer_choice_name='Paper'
        elif computer_choice==3:
            computer_choice_name='Scissors'
        print("Computer's Choice is:",computer_choice_name)

        if ((computer_choice==1 and users_choice==1) or (computer_choice==2 and users_choice==2) or (computer_choice==3 and users_choice==3)):
            print("It's a tie")
        elif ((computer_choice==1 and users_choice==2) or (computer_choice==2 and users_choice==3) or (computer_choice==3 and users_choice==1)):
            print("Users wins")
            user_score+=1
        elif ((computer_choice==1 and users_choice==3) or (computer_choice==2 and users_choice==1) or (computer_choice==3 and users_choice==2)):
            print("Users loses")
            computer_score+=1
        print("User Score\U0001F3AF:",user_score)
        print("Computer Score\U0001F3AF:",computer_score)

        print("Play again? [Y/N]:")
        nextRound = input().upper()
        if nextRound == 'N':
            break

print("Adios\U0001F44B")


