from random import randint

#this is you	
class Character:
	def __init__(self, name):
		self.name = name
		self.sins = 20
		self.holiness = 0
		self.sinsList = []
	

	
	def increaseSins(self, sinName):
			self.sins += 1
			self.sinsList.append(sinName)
			print("Your sin has increased by", 1, "for:", sinName + ".")
			print("You currently have",  self.sins, "sins.")
	
		
	def confessSin(self, sin):
		if sin in self.__sinsList:
			index = self.__sinsList.index(sin)
			self.__sinsList.pop(index)
			print("Ah, I see... ")
			
		elif sin == 'exit':
			print("You should think more carefully next time about what you've done wrong.")
			
		elif sin in sinDict:
			print("But you haven't done that!")
	
		else:
			print("I don't understand that!")
			
	def getHintSins(self):
		print("Have you forgotten the time you did this:", self.__sinsList[0] + "?")
			
	def increaseHoliness(self):
		self.holiness += 1
		self.sins -= 1
		print("Good work! Your holiness has increased by 1.")
