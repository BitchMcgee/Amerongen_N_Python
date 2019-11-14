# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars, compare
gameVars.computer=gameVars.choices[randint(0,2)]
while gameVars.player is False:
	print("===*===*===*===*===*===*===*===*===*===*===*===*===*===\n")
	print("Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("===*===*===*===*===*===*===*===*===*===*===*===*===*===\n")
	print("Select Your Avenger!\n")
	gameVars.computer=gameVars.choices[randint(0,2)]
	player=input("choose cap spidey or stark: \n")
	print("Oponent:", gameVars.computer, "Hero:", player)
	
	compare.compareChoices(player)
	
	
	#compare.compareChoices(gameVars.player)
	if gameVars.player_lives is 0:
	 	winlose.winorlose("have been defeated")
	elif gameVars.computer_lives is 0:
		winlose.winorlose("are victorious")
else:
	player = False
	gameVars.computer=gameVars.choices[randint(0,2)]


