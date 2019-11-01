# import the random package so we can generate a random AI choice
from random import randint

# 'basket' of choices
choices=["rock","paper","scissors"]

#let the AI make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we don't have to keep restarting
player=False

while player is False:
	player=input("choose Rock, Paper or Scissors: \n")
	
	#start doing some logic and condition checking
	print("computer:", computer, "player:", player)

	# always check a breaking condition first
	if player==computer:
		print("tie, nobody wins")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if computer == "Paper":
			print("You lose!", computer, "covers", player, "\n")
		else:
			print("You won!", player, "smashes", computer, "\n")
	elif player == "paper":
		if computer == "Scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			print("You won!", player, "covers", computer, "\n")

	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			print("You won!", player, "cuts", computer, "\n")	
	

	player = False
	computer=choices[randint(0,2)]

