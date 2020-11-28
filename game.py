
from random import randint
# arrays are indexed (their conetnts get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 1
computer_lives = 1

total_lives = 1

#define win or lose function
def winorlose(status):
	#print("inside winorlose function; status is: ", status)

	print("You", status, "Do you want to play again?")
	choice = input("Yes / No? ")

	if choice == "No" or choice == "no":
		print("===============================================================================")
		print("You chose to quit! Better luck next time!")
		print("======================================Goodbye==================================")
		exit()
	elif choice == "Yes" or choice == "yes":
		#reset player live and computer lives
		#set player to False -> loop restart
		global player_lives
		global computer_lives
		global player
		player_lives = 1
		computer_lives = 1
		player = False

	else:
		print("Make a valid choice - Yes or No ")
		choice = input ("Yes/No: ")

#True and False are Boolen data types -> they are the equivalent of on or off, 1 or 0
player = False

while player is False: 
	print("====================* A Classic Rock, Paper, Scissor Game *====================")
	print("Computer Lives:", computer_lives, "/", total_lives)
	print("Player Lives:", player_lives, "/", total_lives)
	print("===============================================================================")

	print("Choose your weapon wisely! or type quit to exit\n")
	print("===============================================================================")

	#this is player choice
	player = input("Choose rock, paper or scissors: \n")

	#if want to quit
	if player == "quit":
		print("You chose to quit")
		exit()

	# player = True ->it has value now

	#this is AI choice (random pick)
	computer = choices[randint(0, 2)]

	#check to see what the user input
	print("user chose: "+ player)

	#validate that the random choice worked for the AI
	print("computer chose: "+ computer)

	if (computer == player):
	    print("Tie!")
	elif (computer == "rock"): 
		if (player == "scissors"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	elif (computer == "paper"): 
		if (player == "rock"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1
		
	elif (computer == "scissors"): 
		if (player == "paper"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	if player_lives == 0:
		winorlose("lost")
		
	if computer_lives == 0:
		winorlose("won")
		

	print("Player has", player_lives, "lives left")
	print("Computer has", computer_lives, "lives left")

	#make loop keep running by setting player back to False
	# unset, so that the loop condition will evaluate to True
	player = False


     

     



