from gameComponents import gameVars
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
		gameVars.player_lives = 3
		gameVars.computer_lives = 3
		gameVars.player = False

	else:
		print("Make a valid choice - Yes or No ")
		choice = input ("Yes/No: ")