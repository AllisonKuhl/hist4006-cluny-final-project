from random import randint
import psalms
import getRule
import randomEvents

'''
TO-DO

- more random events
 -add romance
- more liturgy 
- fine-tune dates
- add feast days and seasonal liturgy
- Add more ways to decrease penance (like if you do prayers all correctly?)
- option to save or load game
- romance subplots
- lots more stuff probably

'''



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
VERSES_SAID = 3 # how many verses of the psalms should we say?


#daily schedule, feel free to change things around!
DAY_ACTIVITIES = ['wake up', 'go to nocturnes', 'have free time', 'go to matins', 'sleep', 'go to prime', 'have free time', 'go to terce', 'go to chapter meeting', 'do work', 'go to sext', 'go to nones', 'go to dinner', 'take siesta', 'have free time', 'go to vespers', 'go to compline', 'sleep']


#which psalm is said during which hour. 
PSALMS_SAID = {'nocturnes': 121, 'matins': 31, 'prime': 6, 'terce': 56, 'sext': 101, 'nones': 129, 'vespers': 142, 'compline': 69}


#for testing purposes... please ignore!!!
#DAY_ACTIVITIES = ["wake up", "read", "sleep"]



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
		self.__name = name
		self.__sins = 0
		self.__sinsList = []
		self.__penance = 0
		self.__age = 20
		self.__health = 20
		self.__popularity = 0
		self.sleepiness = 0
		self.__lifespan =  25 #randint(30,80) but 25 for testing purposes
		self.alive = True #right now you are alive
		self.holiness = 0
		self.prompt = True
		
	def getName(self):
		return self.__name
	
	def setSins(self,sins):
		self.__sins = sins
		
	def addHealth(self, num):
		self.__health += num
		
	def addPopularity(self, num):
		self.__popularity += num
	
	
	def increaseSins(self, sins, sinName):
			self.__sins += sins
			if sinName not in self.__sinsList:
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
	
	def getHintSins(self):
		print("Have you forgotten the time you did this:", self.__sinsList[0] + "?")
		
		
	def setAge(self, age):
		self.__age += age
		
		if self.__age == self.__lifespan:
			self.alive = False
			
	def getAge(self):
		return self.__age
		
		
	def decreasePenance(self, penance):
		if self.__penance > 0:
			print("Your penance decreases by", penance + ".")
			self.__penance -= penance
			self.holiness += penance/2
		elif self.__penance <= 0:
			self.holiness += penance
			
		
	def increaseHoliness(self, num):
		self.holiness += num

	def changeSleepiness(self, num):
		if num < 0:
			if self.sleepiness > 0:
				self.sleepiness += num
		else:
			self.sleepiness += num
		
		

class Activity():
	def __init__(self,name, location):
		self.__name = name
		self.__correctAction = "go to " + name
		self.location = location

	
	def go_to(self, playerObject):
	
		if playerObject.prompt == True:
			print("Now it is time to", self.__correctAction)
	
		while True:
			user_input = input("> ")
			if user_input == self.__correctAction:
				print("You", self.__correctAction + ".")
				break
			else:
			
			#else if in....good action list, do correct response, etc.....
				print("Now's not the time for that!")
				playerObject.increaseSins(1, 'incorrect action')
				
				
	def do_action(self, player):
		print("You are in the", self.location + ".")
			
	def getName(self):
		return self.__name
		
	def random_events(self, player):
		randomEvents.normalRandomEvents(player)

	
				
class Prayer(Activity):
	def __init__(self, name, psalmNumber):
		Activity.__init__(self, name, "church")
		self.__psalmNumber = psalmNumber
		#self.__psalms = psalms
		
	def setPsalmNumber(self, newNumber):
		self.__psalmNumber = newNumber
		
	def do_action(self, player):
		print("You arrive in the chapel and prepare to say the liturgy.")
		psalms.say_psalms(self.__psalmNumber, player, psalmsList, VERSES_SAID)

		

class FreeTime(Activity):  #needs editing!!!
	def __init__(self):
		Activity.__init__(self, "free time", "dormitory")
		self.action = "read"
	
	def go_to(self, playerObject):
	
		if playerObject.prompt == True:
			print("You have free time now! What would you like to do?")
			print("1. Read")
			print("2. Work")
			print("3. Sleep")
			print("4. Chat with other monks.")
		
		user_input = input("> ")	
	
		if user_input == "go read":
			print("You go study scripture.")
			PlayerObject.decreasePenance(1)
		elif user_input == "go work":
			print("You go help the monks work.")
			playerObject.decreasePenance(1)
		else:
			print("Now's not the time to do that!")
			playerObject.increaseSins(1, "incorrect activity")
	

	
class Sleep(Activity):
		def __init__(self):
			Activity.__init__(self, "sleep", "dormitory")
			self.asleep = False
			
		def go_to(self, player):
			if player.prompt == True:
				print("Now it is time to sleep.")
				print("Do you sleep, or stay up praying instead?")
				
			while True:
			
				user_input = input("> ")
				
				if user_input == "sleep":
					print("You go to sleep.")
					player.changeSleepiness(-1)
					self.asleep = True
					break
					
				elif user_input == "pray":
					print("You stay up praying instead.")
					player.decreasePenance(10)
					player.changeSleepines(1)
					self.asleep = False
					break
				else:
					print("I don't understand that.")
					
		def do_action(self, player):
			if self.asleep == True:
				print("\nThe bell rings.")
				print("DONG!", chr(7))
				print("It's time to wake up! Wake up, O sleeper, arise!")
				
				while True:
					user_input = input("> ")
					
					if user_input == "wake up":
						if player.sleepiness > 3:
							print("You try and wake up, but you're too tired. Before you know it, you're drifting off to sleep.")
							player.increaseSins(5, "laziness")
						else:
							print("You wake up feeling refreshed.")
						break
						
					elif user_input == "sleep more":
						print("You sleep some more.")
						player.increaseSins(5, "laziness")
						break
		def random_events(self, player):
			randomEvents.nightRandomEvents(player)
					

class ChapterMeeting(Activity):
	def __init__(self):
			Activity.__init__(self, "chapter meeting", "chaptorium") #or wherever chapter meetings took place????
					
			
	def do_action(self, player):
	
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
				sin = input("What sins do you have to confess? \n > ")
				
				if you.prompt == True:
					print("Type exit to exit and hint for a hint if you can't remember what sins you've done.")
				you.confessSin(sin)				
				if you.getSinsListLength() == 0:
					print("You have no more sins to confess!")				
				if sin == 'exit':
					break
				
				if sin == "hint" and you.prompt == True:
					you.getHintSins()
						

class Dinner(Activity):
	def __init__(self):
			Activity.__init__(self, "dinner", "refectory") 
					
	def do_action(self):
		print("It is time to eat!")
		print("While you eat, somebody reads.")
		randInt = randint(0,len(ruleExcerpts)-1)
		print("\n",ruleExcerpts[randInt], ruleExcerpts[randInt+1], ruleExcerpts[randInt+2])
		
		action = input("> ")
		
		if action != "listen" or action != "eat":
			if action != eat:
				print("You are supposed to listen!")
				you.increaseSins(1,"not listening to rule")
		
		print("\n",ruleExcerpts[randInt+3], ruleExcerpts[randInt+4], ruleExcerpts[randInt+5])
	

				
	
psalmsList = psalms.getPsalms()

			

		
#you = Player("Hugh")


sleep = Sleep()
freeTime = FreeTime()
chapterMeeting = ChapterMeeting()
dinner = Dinner()



nocturnes = Prayer("nocturnes", PSALMS_SAID["nocturnes"])
matins = Prayer("matins", PSALMS_SAID["matins"])
prime = Prayer("prime", PSALMS_SAID["prime"])
terce = Prayer("terce", PSALMS_SAID["terce"])
sext = Prayer("sext", PSALMS_SAID["sext"])
nones = Prayer("nones", PSALMS_SAID['nones'])
vespers = Prayer("vespers", PSALMS_SAID['vespers'])
compline = Prayer("compline", PSALMS_SAID['compline'])



DAY_ACTIVITIES = [nocturnes, freeTime, matins, sleep, prime, freeTime, terce, chapterMeeting, freeTime, sext, nones, dinner, sleep, freeTime, vespers, compline, sleep]

time = Time()

name = input("What is your name? \n> ")
you = Player(name)

print("Welcome", name + "! You are now a monk.")



while you.alive == True:

	time.printDate()
	
	print("A new day begins! Early in the morning, before even the light of day has broken over the fertile plains of Burgundy, the monks of Cluny rise from their slumber to begin their daily rounds of prayer.")

	for activity in DAY_ACTIVITIES:
		
		activity.go_to(you)
		activity.random_events(you)
		activity.do_action(you)
		
	time.dayEnd(you)
	
end = input("You are dead. Thanks for playing.")

