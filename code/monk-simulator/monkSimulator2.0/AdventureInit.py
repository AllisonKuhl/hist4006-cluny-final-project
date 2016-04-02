from roomClass import Room
import activityClass
from npc import Player

class Abbey():
	def __init__(self):
		
		church = Room("church", "You are in the sanctuary of the church. It's superflous heights and vapid flourishes are astounding. This is the currently the biggest church in Europe!")
		galilee = Room("galilee", "You are in the galilee of the church. This is the front part of the church.")
		narthex = Room("narthex", "This is the entrance of the church.")
		passage1 = Room("passage", "You are in a long passageway.")
		court = Room("court", "You are in the abbot's court.")
		chapel = Room("chapel", "You find yourself in a small chapel.")
		atrium = Room("atrium", "You are in an atrium.")
		cloister = Room("cloister", "You are in the cloister. This is heart of the abbey!")
		hall = Room("hall", "You are in a hallway.")
		cellar = Room("cellar", "You are in the cellar. It is full of delicious looking food.")
		kitchen = Room("kitchen", "You are in the kitchen.")
		refectory = Room("refectory", "You are in the refectory. This is where the monks eat.")
		passage2 = Room("passage", "You are in a long passageway.")
		infirmary = Room("infirmary", "You are in the infirmary. It's pretty big!")
		cemetary = Room("cemetary", "You are in the cemetary. Spooky! Everyone wants to be buried here.")
		noviceCloister = Room("novice cloister", "You are in the cloister. This one is for novices.")
		novitiat = Room("novitiat", "You are in the novice's dormitory. The room is filled with simple cots.")
		latrines1 = Room("latrines", "You are in the latrines. It's kinda smelly.")
		
		church.addRooms(None, None, galilee, None)
		galilee.addRooms(church, None, narthex, None)
		narthex.addRooms(galilee, None, None, None)
		passage1.addRooms(chapel, cloister, court, galilee)
		court.addRooms(passage1, atrium, None, None)
		chapel.addRooms(None,None,passage1,None)
		atrium.addRooms(cloister, None, None, court)
		cloister.addRooms(None,hall,atrium, passage1)
		hall.addRooms(None,refectory,cellar,cloister)
		cellar.addRooms(hall,kitchen,None,cellar)
		kitchen.addRooms(refectory,None,None,cellar)
		refectory.addRooms(None,noviceCloister,kitchen,hall)
		passage2.addRooms(infirmary,hall,cloister,church)
		infirmary.addRooms(None,None,passage2,cemetary)
		cemetary.addRooms(None, infirmary, None, None)
		noviceCloister.addRooms(None, novitiat, None, refectory)
		novitiat.addRooms(latrines1,None, None, noviceCloister)
		latrines1.addRooms(None, None, novitiat, None)




		church.addActivity("liturgy", True)
		novitiat.addActivity("sleep", True)
		refectory.addActivity("dinner", True)
		
		
		
		cloister.addPeople([Player("Gerald", "Peace be with you, brother."),Player("Carolus", "Bah! This abbey's getting worse and worse everyday! Back in MY day, being a monk actually meant something special. Kids these days are far too lax!"), Player("Shulk", "I'm really feeling it!")])
		
		church.addPerson(Player("Adelmus","The construction of this church began under Abbot Hugh. It sure is impressive, isn't it?"))
		
		court.addPerson(Player("Henry", "I'm just visiting the abbey. I decided to donate some land. Don't forget to pray for me!"))
		
		passage1.addPerson(Player("Matthew", "Monks shouldn't be talking. Remember that the tongue is a fire, a world of iniquity."))
		
		chapel.addPeople([Player("Drogo","Did you know? This used to be part of the old church.")])
		
		galilee.addPerson(Player("Aethelred","I travelled a long way to visit this church."))
		
		latrines1.addPerson(Player("Paulus","Um....A little privacy please!!???"))
		
		
		self.startRoom = novitiat
		
		
		
	
	
