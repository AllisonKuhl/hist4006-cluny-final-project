import psalms
import getRule
from random import randint

'''
TO-DO

- Random events
- cleaner code
- more liturgy (store each in object?)
- fine-tune dates
- add feast days and seasonal liturgy
- Add ways to decrease penance (like if you do prayers all correctly?)
- option to save or load game
- lots more stuff probably

'''

#note: main loop of game begins on line 179

#Time variables
DAYS_IN_YEAR = 12  #how many days in a year??

LENGTH_LENT = 4  #how long is lent?
LENT_MIN_START = 2 #earliest time for lent to start
LENT_MAX_START = 4 #latest time for lent to start
LENT_START = randint(LENT_MIN_START,LENT_MAX_START) #will pick a day for lent to start within those two intervals
AUTUMN_STARTS = 9  #what day does winter start?
CHRISTMAS = 11   #when is Christmas?

#the current seasons. 
#this is a dictionary that maps each season to when it begins
#you can add more if you like.
SEASONS = {0:'winter', LENT_START: 'lent', LENT_START+LENGTH_LENT:'easter', LENT_START+LENGTH_LENT+1:'summer', AUTUMN_STARTS:'autumn', CHRISTMAS: 'christmas'}

#other variables
VERSES_SAID = 5 # how many verses of the psalms should we say?


#daily schedule, feel free to change things around!
#DAY_ACTIVITIES = ['wake up', 'go to nocturnes', 'read', 'go to matins', 'sleep', 'go to prime', 'read', 'go to terce', 'go to chapter meeting', 'do work', 'go to sext', 'go to nones', 'go to dinner', 'take siesta', 'read', 'go to vespers', 'go to compline', 'sleep']


#which psalm is said during which hour. 
PSALMS_SAID = {'nocturne': 121, 'matins': 31, 'prime': 6, 'terce': 56, 'sext': 101, 'nones': 129, 'vespers': 142, 'compline': 69}


#for testing purposes... please ignore!!!
DAY_ACTIVITIES = ["wake up", "read", "sleep"]



#This section here controls time
class Time:

	'''
	Time like an ever-rolling stream
	Soon bears us all away
	We fly forgotten as a dream
	Dies at the opening day
	'''

	def __init__(self):
		self.__year = 1200
		self.__currentSeason = "winter"
		self.__totalDays = 0
		self.__daysOfYear = 0
		
		
	def newYear(self, playerObj):
		#resets the time when a new year begins
		self.__daysOfYear = 0
		self.__year += 1
		self.__currentSeason = 'winter'
		
		#sets lent to begin at a random time
		LENT_START = randint(LENT_MIN_START,LENT_MAX_START) 
		playerObj.setAge(1) #increases your age.
		
	def dayEnd(self, playerObj):
		self.__totalDays += 1
		self.__daysOfYear += 1
		
		#changes the season
		if self.__daysOfYear in SEASONS:
			self.__currentSeason = SEASONS[self.__daysOfYear]
		
		#changes the year
		if self.__daysOfYear == DAYS_IN_YEAR:
			self.newYear(playerObj)
			
	def printDate(self):
		print("The year is", self.__year, "and it is", self.__currentSeason + ".")
		#print("We are at day", self.__daysOfYear)
		
		
		
#this is you	
class Player:
	def __init__(self, name):
		self.name = name
		self.__sins = 0
		self.__sinsList = []
		self.__penance = 0
		self.__age = 20
		self.__lifespan =  25 #randint(30,80) but 25 for testing purposes
		self.alive = True #right now you are alive
	
	def setSins(self,sins):
		self.__sins = sins
		
	
	def increaseSins(self, sins, sinName):
			self.__sins += sins
			self.__sinsList.append(sinName)
			print("Your sin has increased by", sins, "for:", sinName + ".")
			print("You currently have",  self.__sins, "sins.")
	
	def getSins(self):
		return self.__sins
		
	def getSinsListLength(self):
		return len(self.__sinsList)
		
	def confessSin(self, sin):
		if sin in self.__sinsList:
			index = self.__sinsList.index(sin)
			self.__sinsList.pop(index)
			print("Ah, I see... Almighty God will forgive this most grevious fault... But first you must do some penance.")
			print("Penance increased by 2!")
			self.__penance += 2
			
		elif sin == exit:
			print("You should think more carefully next time about what you've done wrong.")
			
		else:
			print("But you haven't done that!")
	
	def getHintSins():
		print("Have you forgotten the time you did this:", self.__sinsList[0] + "?")
		
		
	def setAge(self, age):
		self.__age += age
		
		if self.__age == self.__lifespan:
			self.alive = False
			
	def getAge(self):
		return self.__age
		
		
prompt = True

you = Player("Hugh") #creates a player object called "Hugh"
time = Time()

	
def getRule():

	ruletxt = open('rule2.txt', 'r')
	
	rule = []

	for line in ruletxt:
			rule.append(line)

	ruletxt.close()


	return rule

prayers = {'go to nocturnes': 'nocturne', 'go to matins': 'matins', 'go to prime':'prime', 'go to terce': 'terce', 'go to sext':'sext', 'go to nones': 'nones', 'go to vespers': 'vespers', 'go to compline': 'compline'}

psalmsList = psalms.getPsalms() #gets a list of all the psalms
ruleExcerpts = getRule() #gets a list that holds excerpts from the Rule of Benedict

#main part of game
while you.alive == True:
	
	time.printDate()
	
	for event in DAY_ACTIVITIES:

		print("\nThe bell rings.")
		print("DONG!", chr(7))
		
		
		while True:
		
			if prompt == True:
				print("\nIt is time to", event + ".")
			
			action = input("\n> ")
			
			if action == event:
				print("You", event + ".\n")
				break
			else:
				print("You aren't supposed to do that right now!")
				if prompt == True:
					print("You need to say:", event + ".")
				you.increaseSins(1, 'incorrect activity')
				
		
		if event in prayers:
			#print("This is a prayer.")
			whichHour = prayers[action]
			psalmNum = PSALMS_SAID[whichHour]
			psalms.say_psalms(psalmNum, prompt, psalmsList, VERSES_SAID)
			
		
			
		if event == "go to dinner":
			print("It is time to eat!")
			print("While you eat, somebody reads.")
			randInt = randint(0,len(ruleExcerpts)-1)
			print("\n",ruleExcerpts[randInt], ruleExcerpts[randInt+1], ruleExcerpts[randInt+2])
			
			action = input("> ")
			
			if action != "listen":
				print("You are supposed to listen!")
				you.increaseSins(1,"not listening to rule")
			
			print("\n",ruleExcerpts[randInt+3], ruleExcerpts[randInt+4], ruleExcerpts[randInt+5])
			
			
		if event == "go to chapter meeting":
			print("\n Do you have any sins to confess? y or n")
			
			while True:
				userInput = input("> ").lower()
				
				if userInput == 'y':
					break 
				elif userInput == 'n':
					if you.getSins() == 0:
						break
					else:
						print("I don't think that's the case... But okay...")
						break
						
				else:
					print("I don't understand that! Please type either y or n")
					
				
			if userInput == "y":
				
				
				while you.getSinsListLength() > 0:
					
					sin = input("What sins do you have to confess?")
					
					if prompt == True:
						print("Type exit to exit and hint for a hint if you can't remember what sins you've done.")
			
					you.confessSin(sin)
					
					if you.getSinsListLength() == 0:
						print("You have no more sins to confess!")
						
					if sin == 'exit':
						break
					
					if sin == "hint" and prompt == True:
						you.getHintSins()
						
			
			
	time.dayEnd(you) 
	
		
		
print("You are dead!")

next = input("That's all for now folks!")

