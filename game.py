# [] => this is an array. An array is a special type of container that can hold multiple items
from random import randint
# arrays are indexed (their conetnts get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 5
computer_lives = 5

total_lives = 5

#True anf False are Boolen data types -> they are the equivalent of on or off, 1 or 0
player = False

while player is False: 

	#this is player choice
	player = input("Choose rock, paper or scissors: ")

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
	print("Player has", player_lives, "lives left")
	print("Computer has", computer_lives, "lives left")

	#make loop keep running by setting player back to False
	# unset, so that the loop condition will evaluate to True
	player = False


     

     



