# import the random package so we can generate a random AI choice
from random import randint

# 'basket' of choices
choices=["cap","spidey","stark"]

player_lives = 3
computer_lives = 3

#let the AI make a choice
computer=choices[randint(0,2)]
#player=input
#set up a game loop here so we don't have to keep restarting
player=False

def winorlose(status):
	print("called win or lose", status)
	print("You", status, "! Can You do this all day?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		#reset the game and start all over again
		player_lives = 3
		computer_lives = 3
		player = False
		computer= choices [randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. better luck next time!")
		exit()
	else:
		print("That's a yes or no question.")

while player is False:
	print("==========================================\n")
	print("Computer Lives", computer_lives, "/5\n")
	print("Player Lives", player_lives, "/5\n")
	print("==========================================\n")
	print("Choose Your Avenger!\n")
	player=input("choose cap spidey or stark: \n")
	#player=input("choose Rock, Paper or Scissors: \n")
	
	#start doing some logic and condition checking
	print("computer:", computer, "player:", player)

	# always check a breaking condition first
	if player==computer:
		print("Tie. No matter who wins or loses, trouble still comes around.")

	elif player == "quit":
		print("The world needs you. And you walk out on us.")
		exit()

	elif player == "cap":
		if computer == "spidey":
			print("Round lost!", computer, "shield-webs", player, "\n")
			player_lives = player_lives -1
		else:
			print("Round won!", player, "deflects", computer, "\n")
			computer_lives = computer_lives -1
	elif player == "spidey":
		if computer == "stark":
			print("Round lost!", computer, "de-suits", player, "\n")
			player_lives = player_lives -1
		else:
			print("Round won!", player, "shield-webs", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "stark":
		if computer == "cap":
			print("Round lost!", computer, "deflects", player, "\n")
			player_lives = player_lives -1
		else:
			print("Round won!", player, "de-suits", computer, "\n")	
			computer_lives = computer_lives -1
	if player_lives is 0:
	 	winorlose("have been defeated")
	# 	print("You lost ya loser! Wanna go again?")
	# 	choice = input("Y / N?")

	# 	if choice == "Y" or choice == "y":
	# 		#reset the game and start all over again
	# 		player_lives = 5
	# 		computer_lives = 5
	# 		player = False
	# 		computer= choices [randint(0,2)]

	# 	elif choice == "N" or choice == "n":
	# 		print("You chose to quit. better luck next time!")
	# 		exit()
	# 	else:
	# 		print("Make a valid choice. Yes or NO!")

	elif computer_lives is 0:
		winorlose("are victorious")
	# 	print("You won! Would you like to play again?")
	# 	choice = input("Y / N?")

	# 	if choice == "Y" or choice == "y":
	# 		#reset the game and start all over again
	# 		player_lives = 5
	# 		computer_lives = 5
	# 		player = False
	# 		computer= choices [randint(0,2)]

	# 	elif choice == "N" or choice == "n":
	# 		print("You chose to quit. better luck next time!")
	# 		exit()
	# 	else:
	# 		print("Make a valid choice. Yes or NO!")
	else:
		player = False
		computer=choices[randint(0,2)]


