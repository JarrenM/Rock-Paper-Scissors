# Jarren Mahmoud
# Rock Paper Scissors
#VARIABLES
import random
pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s",]

# Welcome Message
# Print the message
print("Welcome to Rock Paper Scissors")
# Prompt for player name
pName = input("What is your name?")

# Game Loop

# Final Score
def printScore():
# Write Message
	print("The score is:")
# Write player score
	print(pName + ": " + str(pScore))
# Write compute score
	print("Computer: " + str(cScore))
# Write how many ties
	print("Ties: " + str(ties))

# Game Loop
# make a forever loop
while True:
# print current score
printScore()
# Prompt for a choice 
pChoice = input("Enter r (rock), p (paper), s (scissors) or q (to quit):")
# get computers choice (random)
cHoice = random.choice(computerChoices)
# compare for player entering r 
	if pChoice == "r":
	# if computer is r
	if cChoice == "r"
		print("Computer picked rock")
		print("this is a tie")
		ties = ties + 1
	# if computer is p
	elif pChoice == "p":
		print("computer picked paper")
		print("paper covers rock")
		cScore == cScore + 1
	# if computer is s
	else:
		print("Computer picked scissors")
		print("Rock breaks scissors")
		pScore = pScore + 1 

# compare for player entering p
	elif pChoice == "p":
		pass
# compare for player entering s
	elif pChoice == "s":
		pass
# deal with player entering q
	if pChoice == "q":
		break