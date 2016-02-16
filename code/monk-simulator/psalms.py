
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
	
	
	

	

def say_psalms(number,boolPrompt, psalmsArray):

	print("Please say psalm number", str(number) + ".\n0")

	for line in psalmsArray[number]:
		if boolPrompt == 1:
			print("\n",line)
		
		while True:
			yourLine = input("\n> ")

			if yourLine == line:
				break
			else:
			
				print("You made a mistake! The correct line is:")
				print("\n",line)

				
				
def main():	

	psalmsArray = getPsalms()
	
	get_number = int(input("Which psalm would you like to say?"))

	while True: 
		prompt = input("\nWould you like a prompt? Enter 1 for yes and 0 for no.")
		if prompt == '1' or prompt == '2':
			break
		else:
			print("Please enter a boolean value.")
	
	print("")
	say_psalms(get_number, int(prompt), psalmsArray)
	
	
				
main()
	
