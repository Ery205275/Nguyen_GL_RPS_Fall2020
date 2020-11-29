from random import randint
#re-import game variables
from gameComponents import gameVars, winlose, comparisons


while gameVars.player is False: 
	print("====================* A Classic Rock, Paper, Scissor Game *====================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("===============================================================================")

	print("Choose your weapon wisely! or type quit to exit\n")
	print("===============================================================================")

	#this is player choice
	gameVars.player = input("Choose rock, paper or scissors: \n")
	# gameVars.player = True ->it has value now

	#if want to quit
	if gameVars.player == "quit":
		print("You chose to quit")
		exit()

	#this is AI choice (random pick)
	computer = gameVars.choices[randint(0, 2)]

	#check to see what the user input
	print("user chose: "+ gameVars.player)

	#validate that the random choice worked for the AI
	print("computer chose: "+ computer)

	comparisons.comparisons()


     
	if gameVars.player_lives == 0:
		winlose.winorlose("lost")
		
	if gameVars.computer_lives == 0:
		winlose.winorlose("won")
		

	print("Player has", gameVars.player_lives, "lives left")
	print("Computer has", gameVars.computer_lives, "lives left")

	#make loop keep running by setting player back to False
	# unset, so that the loop condition will evaluate to True
	gameVars.player = False
