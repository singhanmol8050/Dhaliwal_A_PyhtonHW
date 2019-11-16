from gameFunctions import gameVars

# What are you trying to compare inside de function? 
# you will need to pass those things in as arguments
# inside de round brackets
def comparechoices():
	if player == "quit":
		exit()
	elif player == "even":
		if gameVars.computer == "1":
			print("You lose!", gameVars.computer, "1 is not even", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "1 is even", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "odd":
		if gameVars.computer == "2":
			print("You lose!", gameVars.computer, "2 is not odd", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "2 is odd", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")