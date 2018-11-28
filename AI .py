import random
from random import randint
winner = input ("input number of times for game: ")
winner = int (winner)
player_win = 0
computer_win = 0
while player_win <  winner and computer_win < winner :
    
    print (f"player score{player_win} and  computer score {computer_win}")
    rand_choice = randint(0,2)
    player =   input("p make your move").lower()
    if player == "quit" or player == "q":
        break
    print (player)
    if rand_choice == 0:
                computer = "rock"
                print (computer)
    elif rand_choice == 1 :
                computer = "paper"
                print (computer)
    else:
        computer ="scissors"
        print (computer)
    if player != "" or computer != "" :
        if player == "scissors" and  (computer != "scissors" and computer != "paper") :
                    print ("computer wins")
                    computer_win += 1
        elif player == "scissors" and computer == "scissors":
                    print ("it's a tie :((")
        elif player == "scissors" and computer == "paper":
                    print ("player wins these round ")
                    player_win += 1
        if player == "rock" and  (computer != "rock" and computer != "scissors") :
                    print ("computer w        ins")
                    computer_win += 1
        elif player== "rock" and  computer == "rock":
                    print ("it's a tie :((")
        elif player == "rock" and computer == "scissors" :
                    print ("player wins these round ")
                    player_win += 1
        if player == "paper" and  (computer != "paper" and computer != "rock") :
                    print ("computer wins")
                    computer_win += 1
        elif player== "paper" and computer == "paper":
                    print ("it's a tie :((")
        elif player == "paper" and computer == "rock" :
                    print ("player wins these round ")
                    player_win += 1
    else :
                print  ("no selection")
    if player_win == winner:
        print ("player won the game")
    elif  player_win == computer_win:
        print ("its a tie")
    else:
        print ("computer won the game")
print (f"final scores :player ={player_win} and computer = {computer_win}  ")
                            
                