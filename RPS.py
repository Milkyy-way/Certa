import random

#user will choose the option and that option will go in variable
#computer will generate one option
#user and computer option will be compared
#result will be displayed
#ask the user if he want to play again or not
#exit if not run the game again if yes
while True:
    computer_choice=["rock","paper","scissors"]
    

    def situation(computer_action, user_option):
        if computer_action==user_option:
            print("Its a draw")
        elif computer_action == "rock" and user_option == "scissors":
            print("Computer wins")
        elif computer_action == "paper" and user_option == "rock":
            print("Computer wins")
        elif computer_action == "scissors" and user_option == "paper":
            print("Computer wins")
        else:
            print("User Wins")
    def validate():

        user = input("Enter a choice (Rock, Paper, Scissors):")
        user_choice = user.lower()
        count=0
        for value in range(len(computer_choice)):
            if user_choice == computer_choice[value]:
                break
            else:
                count =count+1
        if count<3:
            print("entered input is valid")
            return user_choice
        else:
            print("Entered choice is not valid Please try again")
            validate()
            
                
        
            

 
    
    user_option=validate()
    
    computer_action=random.choice(computer_choice)
    print("Computer has choosen: "+computer_action)

    situation(computer_action, user_option)



    extra_game=input("Do you want to play again: Y/N")

    if extra_game.lower() != "y":
        break



