import activityClass

liturgy = activityClass.Prayer()
sleep = activityClass.Sleep()
dinner = activityClass.Eat()	
chapter = activityClass.Chapter()

divineHours = ["nocturnes", "matins", "prime", "terce", "sext", "nones", "vespers", "compline"]	

freeTime =  activityClass.Activity("free time.","","", "You have some free time now. Better enjoy it!")

class Time():
	def __init__(self):
		self.day = 1
		self.totalTurns = 0
		self.turns = 0
		self.activityIndex = 0
		self.activities = ["nocturnes", "free time", "matins", "sleep", "prime", "free time", "terce", "chapter meeting", "free time", "sext", "nones", "dinner", "sleep", "free time", "vespers", "compline"]
		
	def getCurrentActivityName(self):
		return self.activities[self.activityIndex]
	
	def getCurrentActivityClass(self):
		
		activity = self.activities[self.activityIndex]
		
		if activity in divineHours:
			return liturgy
		
		elif activity == sleep.name:
			return sleep
			
		elif activity == dinner.name:
			return dinner
			
		elif activity == "free time":
			return freeTime
			
		elif activity == "chapter meeting":
			return chapter
	
		else:
			return ""
		
	def getCurrentActivityType(self):
	
		activity = self.activities[self.activityIndex]
		
		if activity in divineHours:
			return "liturgy"
			
		else:
			return activity.name
		
	def resetTurn(self):
		self.turns = -1
		if self.activityIndex < len(self.activities):
			self.activityIndex += 1
		
	def endTurn(self, player):
		
		print("INDEX = ", self.activityIndex)
		print("DAY NUMBER = ", self.day)
		
		self.totalTurns += 1
		self.turns += 1
		if self.turns > 15:
			self.turns = 0 
			
			if self.getCurrentActivityName() != "free time":
				next = input("Woops! You've missed " + self.getCurrentActivityName() + "!")
				player.increaseSins("skipping")
			
			self.activityIndex += 1
			
			
		if self.activityIndex >= len(self.activities)-1:
			print("You have finished the day. Let's begin the next!")
			self.day += 1
			self.activityIndex = 0
			self.turns = 0
			
