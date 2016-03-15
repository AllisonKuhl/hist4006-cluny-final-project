from random import randint


sinDict = {"murder": 100, "impure thoughts": 1, "talking": 1, "romance": 1, "kissing": 5, "sodomy": 5, "laziness": 1, "pagan literature": 1, "lying": 1, "not listening to rule": 1, "levity": 1, "skipping": 1, "sleeping": 1, "saying the psalms incorrectly": 2, "messing up liturgy": 2}

#this is you	
class Player:
	def __init__(self, name):
		self.__name = name
		self.__sins = 0
		self.__sinsList = []
		self.__penance = 0
		self.__age = 20
		self.__sickliness = 0
		self.__popularity = 0
		self.sleepiness = 0
		self.__lifespan =  25 #randint(30,80) but 25 for testing purposes
		self.alive = True #right now you are alive
		self.holiness = 0
		self.prompt = True
		self.__sick = False
		#servant girl romance
		self.romance1 = 'open'
		self.romance1lvl = 0
		self.meetings1 = 0
		#oblate boy romance
		self.romance2 = 'open'
		self.romance2lvl = 0
		self.meetings2 = 0
		
	#getters 	
	def getSickliness(self):
		return self.__sickliness;

	def isSick(self):
		return self.__sick
		
	def getName(self):
		return self.__name
		
	def getSins(self):
		return self.__sins
		
	def getSinsListLength(self):
		return len(self.__sinsList)
	
	def getAge(self):
		return self.__age
		
	def getPenance(self):
		return self.__penance
		
	def getPopularity(self):
		return self.__popularity
		
	def getSleepiness(self):
		return self.sleepiness
	
	def getLifespan(self):
		return self.__lifespan
		
	def getHoliness(self):
		return self.holiness
	
	def getSinsList(self):
		return self.__sinsList
		
	#setters
	def changeHealth(self, sickOrNot):
		self.__sick = sickOrNot
		
	
	def setAge(self, age):
		self.__age += age
		
		if self.__age == self.__lifespan:
			self.alive = False
	
	def setSins(self,sins):
		self.__sins = sins
		
	def decreaseHealth(self, num):
		self.__sickliness += num
		
	def addPopularity(self, num):
		self.__popularity += num
	
	def die(self):
		self.alive = False;
		
		
		
	#other functions
	
	def increaseSins(self, sinName):
			self.__sins += sinDict[sinName]
			self.__sinsList.append(sinName)
			print("Your sin has increased by", sinDict[sinName], "for:", sinName + ".")
			print("You currently have",  self.__sins, "sins.")
	
		
	def confessSin(self, sin):
		if sin in self.__sinsList:
			index = self.__sinsList.index(sin)
			self.__sinsList.pop(index)
			print("Ah, I see... Almighty God will forgive this most grevious fault... But first you must do some penance.")
			print("Penance increased by", sinDict[sin])
			self.__sins -= sinDict[sin]
			self.__penance += sinDict[sin]
			
		elif sin == exit:
			print("You should think more carefully next time about what you've done wrong.")
			
		elif sin in sinDict:
			print("But you haven't done that!")
	
		else:
			print("I don't understand that!")
			
	def getHintSins(self):
		print("Have you forgotten the time you did this:", self.__sinsList[0] + "?")
		
	
	def decreasePenance(self, penance):
		if self.__sins > 0:
			self.__sins -= 1;		
		if self.__penance > 0:
			print("Good work! Your penance decreases by " + str(penance) + ".")
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
		
	def talk(self):


		gossip = ["...And then I said to him, what, are you serious and I said, ya, I'm serious, and then he said...", "Well, personally I think that the habit DOES make him look fat...", "So my cousin wrote to the me the other day and...", "...twenty oxen, can you believe! TWENTY!"]
		
		hello = ["hello", "hi", "hey"]
		
		whatsUp = ["what's up?", "how are you?", "what's new", "whats new", "whats up"]
		
		replies = ["Is that so?", "Wow, that's really interesting.", "Hm.", "Please tell me more.", "No way!"]
		
		reply = replies[randint(0, len(replies)-1)]
		
		rand = randint(0,1)
		
		print("As you approach the monks you hear them say...")

		if rand == 1: #current events... will be implemented later
			print("Abbot Hugh is pretty cool isn't he!")
		else:
			print(gossip[randint(0, len(gossip)-1)])
		
		while True:
			 
			speech = input("You say....\n> ")
			speech = speech.lower()
			
			if speech in hello:
				print('Monk: \n"Hello,', self.getName() + '."')
				
			elif speech == "goodbye" or speech == "exit" or speech == "quit":
				print("Monk: \nGoodbye")
				break
			
			elif speech == "tell joke":
				print("You: \nWhat would you say to a novice who's always complaining about his itchy robe?")
				print("Monk: \nWhat?")
				print("You: \nHe has a bad habit!")
				print("Monk: \n.....")
				self.decreaseSins(5, "levity")
				#print("+ 100 sin for bad puns.")
				
			elif speech == "talk about God":
				print("You: \nSo I was thinking about this passage in Revelation the other night...")
				self.increaseHoliness(1)
				print("Monk: \n", reply)
				
			
			elif speech in whatsUp:
				print("Monk: \nI'm good, and you?")
				
			elif speech[len(speech)-1] == '?':
				print("Monk: \nI don't know.")
			
			else:
				reply = replies[randint(0, len(replies)-1)]
				print("Monk: \n", reply)
		
		self.increaseSins("talking")
