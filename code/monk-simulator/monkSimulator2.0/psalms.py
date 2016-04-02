'''
To - DO

decrease sins when you mess up in responsary 

'''
def getPsalms():  #function that gets a list of all the psalms. You must have a text file of all the psalms in the same directory for it to work however.

	psalms = [] #array that holds an array of each psalm
	verses = [] 

	psalmstxt = open('psalms.txt', 'r')

	for line in psalmstxt:

		end = len(line) - 1 #keeps track of the end of the psalm

		if ":1 " in line:
			
			psalms.append(verses)
			verses = []
			start = line.find(" ")
			verses.append(line[start+1:end])
			
		else:
			start = line.find(" ")
			verses.append(line[start+1:end])
			

	psalmstxt.close()


	return psalms
	
	
	
def getUserInput(line, mistakes):

	print("\n",line)
			
	yourLine = input("\n> ")

	if yourLine != line:
		print("\nYou made a mistake! The correct line is:")
		print("\n",line)
		mistakes += 1
		
	
		
	


def say_psalms(number, player, psalmsArray, howManyVerses):

	mistakes = 0

	print("Please say psalm number", str(number) + ".\n")

	for i in range(0,howManyVerses-1):
	
		line = psalmsArray[number][i]
		
		
	
		print("\n",line)
			
		yourLine = input("\n> ")

		if yourLine != line:
			print("\nYou made a mistake! The correct line is:")
			print("\n",line)
			mistakes += 1
			
		
		
	print("......\n....")
	
	line = psalmsArray[number][-1]
	
	
	print("\n",line)
			
	yourLine = input("\n> ")

	if yourLine != line:
		print("\nYou made a mistake! The correct line is:")
		print("\n",line)
		mistakes += 1
	
	

	print("\n")
	
	if mistakes > 0:
		player.increaseSins("saying the psalms incorrectly")
	else:
		print("Wow! You said it perfectly! Flawless victory!\n")
		player.increaseHoliness()
				
				


mistakes = False

def response(correctResponse, player):

	
	print('(you say: "'+ correctResponse + '")')
		
	response = input("> ")
	
	if response != correctResponse:
		mistakes = True
		


def responsary(player): 

	print("Oh Lord, open my lips!")
	
	response("And my mouth will declare your praise.", player)

	print("Make haste, O God, to deliver me.")
	
	response("Make haste to help me, O LORD!", player)
	
	gloriaPatri(player)
	
	if mistakes == True:
		player.increaseSins("messing up liturgy")
		
	
	
def gloriaPatri(player):
	
	response("Glory be to the Father", player)
	response("And to the Son", player)
	response("And to the Holy Spirit", player)
	response("As it was in the beginning", player)
	response("Is now and will be forever", player)
	response("Amen.", player)
	
		
		








				
				
				
def main():	

	psalmsArray = getPsalms()
	
	get_number = int(input("Which psalm would you like to say? "))

	while True: 
		prompt = input("\nWould you like a prompt? Enter 1 for yes and 0 for no. ")
		if prompt == '1' or prompt == '2':
			break
		else:
			print("Please enter a boolean value.")
	
	print("")
	say_psalms(get_number, int(prompt), psalmsArray, 5)
	
	
				
#main()
				


	
