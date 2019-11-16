from gameFunctions import gameVars

# What are you trying to compare inside de function? 
# you will need to pass those things in as arguments
# inside de round brackets
def comparechoices():
	if player == "quit":
		exit()
	elif player == "even":
		if gameVars.computer == "1":
			print("You lose!", gameVars.computer, "is not", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "is", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "odd":
		if gameVars.computer == "2":
			print("You lose!", gameVars.computer, "is not", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "is", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")