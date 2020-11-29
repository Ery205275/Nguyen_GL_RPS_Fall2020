from random import randint
from gameComponents import gameVars
def comparisons():
	computer = gameVars.choices[randint(0, 2)]
	


	if (computer == gameVars.player):
		print("has equal lives with")
    

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("You lose! Be carefull!")
			gameVars.player_lives -= 1
		else:
			print("You win! Keep going!")
			gameVars.computer_lives -= 1 

	elif (computer == "paper"): 
		if (gameVars.player == "rock"):
			print("You lose! Be carefull!")
			gameVars.player_lives -= 1
		else:
			print("You win! Keep going!")
			gameVars.computer_lives -= 1
		
	elif (computer == "scissors"): 
		if (gameVars.player == "paper"):
			print("You lose! Be carefull!")
			gameVars.player_lives -= 1
		else:
			print("You win! Keep going!")
			gameVars.computer_lives -= 1
	