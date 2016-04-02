import activityClass

liturgy = activityClass.Prayer()
sleep = activityClass.Sleep()
dinner = activityClass.Eat()	
			

divineHours = ["nocturnes", "matins", "prime", "terce", "sext", "nones", "vespers", "compline"]	

freeTime =  activityClass.Activity("free time.","","",True, "You have some free time now. Better enjoy it!")

class Time():
	def __init__(self):
		self.day = 1
		self.totalTurns = 0
		self.turns = 0
		self.activityIndex = 0
		self.activities = ["nocturnes", "free time", "matins", "sleep", "prime", "freeTime", "terce", "chapter meeting", "free time", "sext", "nones", "dinner", "sleep", "freeTime", "vespers", "compline"]
		
	def getCurrentActivityName(self):
		return self.activities[self.activityIndex]
	
	def getCurrentActivityClass(self):
		
		activity = self.activities[self.activityIndex]
		
		if activity in divineHours:
			return liturgy
		
		if activity == sleep.name:
			return sleep
			
		if activity == dinner.name:
			return dinner
			
		if activity == "free time":
			return freeTime
			
	def endTurn(self):
		
		self.totalTurns += 1
		self.turns += 1
		if self.turns > 15:
			self.turns = 0 
			self.activityIndex += 1
		if self.activityIndex >= len(self.activities)-1:
			print("The day is over!")
			
