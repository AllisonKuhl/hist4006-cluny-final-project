#class which creates non-playable characters
#will introduced specialized players later on.

class Player():

	def __init__(self,name, message):
		self.name = name
		self.meetings = 0
		self.romance = 0
		self.message = message
		
	def talkTo(self, time):
		inp = input(self.name + " says: " + self.message)
	
