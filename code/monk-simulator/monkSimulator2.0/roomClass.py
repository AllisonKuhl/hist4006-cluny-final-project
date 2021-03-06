from activityClass import Activity
class Room():

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.north = None
		self.east = None
		self.south = None
		self.west = None
		self.stairs = None
		self.people = [] 
		self.objects = []
		self.activity = ""
		self.certainTime = False
		self.visited = False


	def addRooms(self, north, east, south, west):
		self.north = north
		self.east = east
		self.south = south
		self.west = west
	
	def addActivity(self,activity, certainTimes):
		self.activity = activity
		self.certainTime = certainTimes
		
	def addPeople(self, people):
		self.people = people
		
	def addPerson(self,person):
		self.people.append(person)
		
	def removePerson(self, person):
		self.people.remove(person)
	
	def addObject(self, object):
		self.objects.append(object)	
	
	def addStairs(self, room):
		self.stairs = room
		
	def getDescription(self): #returns string representation of room
		
		description = ""
		
		if self.visited == False:
			description += self.description
		else:
			description += "You are in the " + self.name + "."
		
		if self.north != None:
			description += " The " + self.north.name + " is to the north."
		if self.east != None:
			description += " The " + self.east.name + " is to the east."
		if self.south != None:
			description += " The " + self.south.name + " is to the south."
		if self.west != None:
			description += " The " + self.west.name + " is to the west."
			
		for object in self.objects:
			description += " " + object.description
			
		if self.stairs != None:
			description += " There is a staircase in this room."
		
		for person in self.people:
			description += " " + person.name + " is here."
		

		return description
		
		
