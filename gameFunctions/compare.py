from random import randint
from gameFunctions import gameVars

def compareChoices(player):
	if player==gameVars.computer:
		print("Tie. No matter who wins or loses, trouble still comes around.")

	elif player == "quit":
		print("The world needs you. And you walk out on us.")
		exit()

	elif player == "cap":
		if gameVars.computer == "spidey":
			print("Round lost!", gameVars.computer, "shield-webs", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("Round won!", player, "deflects", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
	elif player == "spidey":
		if gameVars.computer == "stark":
			print("Round lost!",gameVars.computer, "de-suits", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("Round won!", player, "shield-webs", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "stark":
		if gameVars.computer == "cap":
			print("Round lost!", gameVars.computer, "deflects", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("Round won!", player, "de-suits", gameVars.computer, "\n")	
			gameVars.computer_lives = gameVars.computer_lives -1