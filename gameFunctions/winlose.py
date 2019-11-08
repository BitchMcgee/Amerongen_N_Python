from random import randint
from gameFunctions import gameVars

def winorlose(status):
	print("You", status, "! Can You do this all day?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		
		#reset the game and start all over again
		gameVars.player_lives = 3
		gameVars.computer_lives = 3
		gameVars.player = False
		gameVars.computer= gameVars.choices [randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. better luck next time!")
		exit()
	else:
		print("That's a yes or no question.")
		#recursion => calling a function from inside itself
		winorlose(status)