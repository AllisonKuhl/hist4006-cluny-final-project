from roomClass import Room
from npc import Player

#this file builds the abbey and populates it with objects and people

class Abbey():
	def __init__(self):
		church = Room("church", "You are in the sanctuary of the church. It's superflous heights and vapid flourishes are astounding. This is the currently the biggest church in Europe!")
		galilee = Room("galilee", "You are in the galilee of the church. This is the front part of the church.")
		narthex = Room("narthex", "This is the entrance of the church.")
		passage1 = Room("passage", "You are in a long passageway.")
		court = Room("court", "You are in the abbot's court.")
		chapel = Room("chapel", "You find yourself in a small chapel.")
		atrium = Room("atrium", "You are in an atrium.")
		cloister = Room("cloister", "You are in the cloister, the heart of the abbey.")
		
		church.addRooms(None, None, galilee, None)
		galilee.addRooms(church, None, None, narthex)
		narthex.addRooms(galilee, None, None, None)
		passage1.addRooms(chapel, cloister, court, galilee)
		court.addRooms(passage1, atrium, None, None)
		chapel.addRooms(None,None,passage1,None)
		atrium.addRooms(cloister, None, None, court)
		cloister.addRooms(None,None,atrium, passage1)
		
		cloister.addPeople([Player("John", "Peace be with you, brother."),Player("Carolus", "Bah! This abbey's getting worse and worse everyday! Back in MY day, being a monk actually meant something special. Kids these days are far too lax!"), Player("Shulk", "I'm really feeling it!")])
		
		church.addPerson(Player("Adelmus","The construction of this church began under Abbot Hugh. It sure is impressive, isn't it?"))
		
		court.addPerson(Player("Henry", "I'm just visiting the abbey. I decided to donate some land. Don't forget to pray for me!"))
		
		passage1.addPerson(Player("Matthew", "You shouldn't be talking. Remember that the tongue is a fire, a world of iniquity."))
		
		chapel.addPeople([Player("Drogo","Did you know? This used to be part of the old church."), Player("Marius","Those who dig a hole will fall into it. That's what the Bible says.")])
		
		galilee.addPerson(Player("Aethelred","I travelled a long way to visit this church."))
		
		
		
		self.startRoom = cloister
	
