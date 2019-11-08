# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("==========================================\n")
	print("Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("==========================================\n")
	print("Choose Your Avenger!\n")
	player=input("choose cap spidey or stark: \n")
	compare.compareChoices(player)
	#gameVars.computer=compare.compareChoices(gameVars.player)
	#print("computer:", gameVars.computer, "player:", player)
	#compare.compareChoices(gameVars.player)
	if gameVars.player_lives is 0:
	 	winlose.winorlose("have been defeated")
	elif gameVars.computer_lives is 0:
		winlose.winorlose("are victorious")
	else:
		player = False
		gameVars.computer=gameVars.choices[randint(0,2)]


