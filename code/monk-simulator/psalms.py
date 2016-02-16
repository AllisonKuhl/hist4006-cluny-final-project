
def getPsalms():  #function that gets a list of all the psalms. You must have a text file of all the psalms in the same directory for it to work however.

	psalms = [] #list that will hold all the psalms
	verses = [] #list that holds each chapter of the psalms, verse by verse

	psalmstxt = open('psalms.txt', 'r') #opens text file with all the psalms

	for line in psalmstxt: #reads each line

		end = len(line) - 1 #each verse is a line. This is the index of the end of the verse.

		if ":1 " in line: #looks at the verse of the psalm. ex: 121:4
		#if it is the 1st verse, then it must be a new psalm!
			
			psalms.append(verses) #since a new psalm is beginning, we append the old one to the master list
			verses = [] #resets verses since it's beginning again
			
			#gets rid of the verse numbers at the beginning of the line
			start = line.find(" ")  
			#adds verse to list
			verses.append(line[start+1:end])
			
		else:
			start = line.find(" ")
			verses.append(line[start+1:end])
			

	psalmstxt.close() #gotta remember to close those files!


	return psalms #returns list of all psalms.
	
	
def say_psalms(number,boolPrompt, psalmsArray): #arguments: number of psalms, whether you want a prompt, and the array with all the psalms

	print("Please say psalm number", str(number) + ".\n")

	for line in psalmsArray[number]: #goes through the given psalm line by line.
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
	
	get_number = int(input("Which psalm would you like to say?")) #should probably add error checking for this...

	while True: 
		prompt = input("\nWould you like a prompt? Enter 1 for yes and 0 for no.")
		if prompt == '1' or prompt == '2':
			break
		else:
			print("Please enter a boolean value.")
	
	print("")
	say_psalms(get_number, int(prompt), psalmsArray)
	
	
				
main()
	
