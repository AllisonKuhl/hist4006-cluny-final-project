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
		
	def getName(self):
		return self.__name
	
	def setSins(self,sins):
		self.__sins = sins
		
	def decreaseHealth(self, num):
		self.__sickliness += num
		
	def addPopularity(self, num):
		self.__popularity += num
	
	def die(self):
		self.alive = False;
	
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
			print("Good work! Your penance decreases by", penance + ".")
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
		
		
