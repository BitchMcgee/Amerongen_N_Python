from random import randint
# 'basket' of choices
choices=["cap","spidey","stark"]

player_lives = 5
computer_lives = 5

total_lives = 5
#let the AI make a choice
computer=choices[randint(0,2)]
#player=input
#set up a game loop here so we don't have to keep restarting
player=False