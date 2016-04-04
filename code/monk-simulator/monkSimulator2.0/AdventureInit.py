from roomClass import Room
import activityClass
from npc import Player
import dialogues

class Abbey():
	def __init__(self):
		
		
		#creates each room
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
		hall2 = Room("hall", "You are in a hallway.")
		calefactorum = Room("calefactorm", "As you enter the room, you are suprised by the emenating heat. There is a large fire burning in the room.")
		chapter = Room("chapter", "You are in chapter. This is where the monks meet to discuss important matters of business.")
		
		#upstairs
		dormitory = Room("dormitory", "You are in the dormitory. The room is filled with simple cots.")
		latrines2 = Room("latrines", "You are in the latrines. It's kinda smelly.")
		passage3 = Room("passage","You are in a hallway.")
		abbatialPalace = Room("abbatialPalace", "You enter a large and luxurious quater. This is where the abbot lives!")
		guestRoom = Room("guest room", "Visitors stay in this room. Connected are its own kitchen and cellar, but you are not allowed to go in.")
		childDormitory = Room("child dormitory", "You are in the children's dormitory. This is where the child oblates sleep.")
		
		
		
		#connects rooms to each other
		church.addRooms(None, None, galilee, None)
		galilee.addRooms(church, None, narthex, None)
		narthex.addRooms(galilee, None, None, None)
		passage1.addRooms(chapel, cloister, court, galilee)
		court.addRooms(passage1, atrium, None, None)
		chapel.addRooms(None,None,passage1,None)
		atrium.addRooms(cloister, None, None, court)
		cloister.addRooms(None,hall,atrium, passage1)
		hall.addRooms(hall2,refectory,cellar,cloister)
		hall2.addRooms(chapter, calefactorum, hall, passage2)
		cellar.addRooms(hall,kitchen,None,cellar)
		kitchen.addRooms(refectory,None,None,cellar)
		refectory.addRooms(calefactorum,noviceCloister,kitchen,hall)
		passage2.addRooms(infirmary,hall2,cloister,church)
		infirmary.addRooms(None,None,passage2,cemetary)
		cemetary.addRooms(None, infirmary, None, None)
		noviceCloister.addRooms(None, novitiat, None, refectory)
		novitiat.addRooms(latrines1,None, None, noviceCloister)
		latrines1.addRooms(None, None, novitiat, None)

		#add stairs
		hall2.stairs = dormitory
		dormitory.stairs = hall2

		
		#second floor
		dormitory.addRooms(None,latrines2,childDormitory,passage3)
		latrines2.addRooms(None,None, None, dormitory)
		childDormitory.addRooms(dormitory, None, None, None)
		passage3.addRooms(None, dormitory,abbatialPalace,None)
		guestRoom.addRooms(None, abbatialPalace,None,None)
		abbatialPalace.addRooms(None, abbatialPalace, None, None)
		
		#room activities
		church.addActivity("liturgy", True)
		novitiat.addActivity("sleep", True)
		refectory.addActivity("dinner", True)
		
		
		self.startRoom = novitiat
		
		
		
		#add people
		
		
		
		
		
		
		
	
	
