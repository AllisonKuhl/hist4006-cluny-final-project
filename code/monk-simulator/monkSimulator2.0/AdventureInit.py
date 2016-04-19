from roomClass import Room
import activityClass
from npc import Player
import dialogues
from objects import food,wine,altar,books,bed

class Abbey():
	def __init__(self):
		
		
		#creates each room
		church = Room("church", "You are in the sanctuary of the church. It's very nice. This is the currently the biggest church in Europe!")
		galilee = Room("galilee", "You are in the apse of the church. The altar is further back.")
		narthex = Room("narthex", "This is the entrance of the church.")
		passage1 = Room("passage", "You are in the galilee passageway")
		court = Room("court", "You enter the courtyard of the abbatial palace within the abbatial palace built by Saint Hugh. This open-air space is the centre of the abbatial palace, formerly the atrium to the second church of Peter and Paul (Cluny II). Around you visitors and monastic officers speak and negotiate. The possibility of failing to keep your proper monastic silence and equanimity seems greater in this mundane space.")
		chapel = Room("chapel", "You find yourself in a small chapel.")
		atrium = Room("atrium", "You are in an atrium.")
		cloister = Room("cloister", "Passing through the covered arcades surrounding the cloister, you enter into the verdant space of the cloister garden - open to the sun and the elements. You rejoice in the great vision of Saintly Odilo, who rebuilt the cloister and turned the space into a veritable new Eden. In summer time, you find nothing more enjoyable than to soak up the warmth of the sun on your face and tend the medicinal or culinary herbs that grow in their neatly arranged beds.  In winter, the rain makes it less hospitable, but the gardens still fill with greenery except from Advent until Epiphany. With books in hand, monks will often sit on the low wall in between the brilliant marble pillars supporting the open galleries running alongside the surrounding buildings. At the south-east end of the cloister a single monk looks down from the dormitory landing. In the south-west corner of the cloister is the covered washing fountain, bubbling with water fed from a nearby spring. This is where all the monks wash and cleanse themselves before mass and before entering the refectory.")
		cellar = Room("cellar", "You are in the cellar. It is full of delicious looking food.")
		kitchen = Room("kitchen", "You are in the kitchen.")
		refectory = Room("refectory", "You are in the refectory. This is where the monks eat.")
		hall = Room("hall", "You are in a hallway")
		passage2 = Room("passage", "You are in a long passageway.")
		infirmary = Room("infirmary", "You are in the infirmary. It's pretty big!")
		cemetary = Room("cemetary", "You are in the cemetary. Spooky! Everyone wants to be buried here.")
		noviceCloister = Room("novice cloister", "You are in the cloister. This one is for novices.")
		novitiat = Room("novitiat", "You are in the novice's dormitory. The room is filled with simple cots.")
		latrines1 = Room("latrines", "You are in the latrines. It's kinda smelly.")
		hall2 = Room("hall", "You are in a hallway.")
		calefactorum = Room("calefactorum", "As you enter the room, you are suprised by the emenating heat. There is a large fire burning in the room.")
		chapter = Room("chapter", "The intimate space of the Chapter room is warmed by the light coming through the raised windows – three on the north side and fourth on the east. It is in this space that the monks gather to hear the Rules of the monastery and discuss monastery business. Though empty now, soon it will be filled with all the members of the community to admit openly (or face accusations) of their failings in the monastic life.")
		
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
		cellar.addRooms(hall,kitchen,None,atrium)
		kitchen.addRooms(refectory,None,None,cellar)
		refectory.addRooms(calefactorum,noviceCloister,kitchen,hall)
		passage2.addRooms(infirmary,hall2,cloister,church)
		infirmary.addRooms(None,None,passage2,cemetary)
		cemetary.addRooms(None, infirmary, None, None)
		noviceCloister.addRooms(None, novitiat, None, refectory)
		novitiat.addRooms(latrines1,None, None, noviceCloister)
		latrines1.addRooms(None, None, novitiat, None)
		calefactorum.addRooms(None,None, refectory, hall2)
		chapter.addRooms(infirmary,hall,cloister,church)

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
		chapter.addActivity("chapter meeting", True)
		
		#objects in room
		
		cellar.addObject(food)
		cellar.addObject(wine)
		chapel.addObject(altar)
		dormitory.addObject(bed)
		novitiat.addObject(bed)
		
		
		self.startRoom = novitiat
		
		print("hello world")
		print(cloister.description)
		
		#add people
		
		noviceCloister.addPeople([Player("Nova",dialogues.oldNovice),Player("Raoul", dialogues.visitingMonk)])
		
		novitiat.addPeople([Player("Odisius", dialogues.sincereMonk), Player("Berard", dialogues.sleepyMonk)])
		
		cloister.addPeople([Player("Paulus", dialogues.pontiusFollower), Player("Cuthbert", dialogues.grumpyMonk), Player("Hidelbert", dialogues.yesMonk), Player("Adelmo", dialogues.informedMonk)])
		
		hall.addPerson(Player("Carolus", dialogues.travellingMonk))
		
		passage1.addPerson(Player("Marius", dialogues.reprimandMonk))
		
		church.addPerson(Player("Humbert", dialogues.humbleMonk))
		
		galilee.addPeople([Player("Gerard", dialogues.fashionableMonk), Player("Arthur", dialogues.pilgrim)])
		
		dormitory.addPeople([Player("Guy", dialogues.saintlyMonk), Player("Bertrand", dialogues.visitingMonk)])
		
		childDormitory.addPeople([Player("Etienne", dialogues.child1), Player("Benedict", dialogues.child2), Player("Timothy", dialogues.child3)])
		
		infirmary.addPeople([Player("Mathias", dialogues.retiredMonk), Player("Roland", dialogues.sickMonk), Player("Fulque", dialogues.insincereMonk)])
		
		abbatialPalace.addPerson(Player("Pontius", dialogues.Pontius))
	
	
