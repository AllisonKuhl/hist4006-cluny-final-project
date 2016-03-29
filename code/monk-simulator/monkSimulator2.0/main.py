from AdventureInit import Abbey
from player import Player

cluny = Abbey()


def play():
	action = ""
	room = cluny.startRoom
	
	while action != "quit":
		
		
		print(room.getDescription())
		
		#print(room.getDescription)
		
		action = input("What would you like to do?\n> ").lower()

		if action == "go north":
			if room.north != None:
				print("You go north.")
				room = room.north
			else:
				print("You can't go north! There is no exit there!")
				
		elif action == "go east":
			if room.east != None:
				print("You go east.")
				room = room.east
			else:
				print("You can't go east! There is no exit there!")
				
		elif action == "go south":
			if room.south != None:
				print("You go south.")
				room = room.south
			else:
				print("You can't go south! There is no exit there!")
				
		elif action == "go west":
			if room.west != None:
				print("You go west.")
				room = room.west
			else:
				print("You can't go west! There is no exit there!")
		
		
		elif action == "use stairs":
			if room.stairs != None:
				print("You use the stairs")
				room = room.stairs
			else:
				print("There are no stairs in this room!")
		
		
		elif "talk to" in action:
			talked = False
			for person in room.people:
				if action == ("talk to " + person.name.lower()):
					person.talkTo()
					talked = True
					break
			if talked == False:
				print("Talk to whom? I don't understand.")
		
		
		
		
		
		
		
		
		elif action == "help":
			print("Avaliable commands:")
			print("go north, go east, go south, go west, use stairs, talk to (insert_persons_name_here), look at (insert object name here), help, quit")
			
		elif action == "quit":
			print("Are you sure you want to quit?!")
			while True:
				answer = input("y/n\n> ")
				if answer == "n":
					print("That's what I thought!")
					action = ""
					break
				elif answer == "y":
					print("Goodbye! Thanks for playing!")
					break
				else:
					print("Type either 'n' or 'y'.")
				
		else:
			print("Woops! I didn't understand that! If you are having trouble, please type 'help' for a list of commands.")
				
				
		
play()		
	
'''
def main():

	name = input("What is your name?\n> ")
	you = Player(name)
	
	print("Welcome,", you.getName() + "to the abbey of Cluny!")

	play()
	
main()
'''
