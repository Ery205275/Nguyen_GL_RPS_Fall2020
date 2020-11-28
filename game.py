# [] => this is an array. An array is a special type of container that can hold multiple items
from random import randint
# arrays are indexed (their conetnts get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

#this is player choice
player = input("Choose rock, paper or scissors: ")

#this is AI choice (random pick)
computer = choices[randint(0, 2)]

#check to see what the user input
print("user chose: "+ player)

#validate that the random choice worked for the AI
print("Ai chose: "+ computer)

if (computer == player):
	print("tie")

elif (computer == "rock"): 
	if (player == "scissors"):
		print("you lose!")
	else:
		print("you win!")

elif (computer == "paper"): 
	if (player == "rock"):
		print("you lose!")
	else:
		print("you win!")
