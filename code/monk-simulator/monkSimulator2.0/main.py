'''
To-Do

- add more dialogues and plot
- change up people and activities and starting place depending on the day
- fix up map
- graphics? (someday)

'''


from AdventureInit import Abbey
from player import Character
from timeClass import Time
import dialogues
from npc import John, demonAbbot

from random import randint

cluny = Abbey()


def play(player):
	action = ""
	time = Time()
	room = cluny.startRoom
	johnIsIn = room
	john = John()
	room.addPerson(john)
	wido = demonAbbot(player)
	widoThere = False
	
	while action != "quit":
		
		currentActivity = time.getCurrentActivityClass()
		#random events
		rand = randint(0,100)
		#demon abbot
		if wido in room.people:
			widoThere = True
		if rand < 5:
			if widoThere != True:
				room.addPerson(wido)
				
		elif rand < 10:
			dialogues.demon(player)
		
		
		if widoThere == True and rand >= 10:
				room.removePerson(wido)
				widoThere = False
			
		if currentActivity.name == room.activity:
			room.addPerson(john)
			johnIsIn.removePerson(john)
			johnIsIn = room
		

		if time.turns == 0:
			print(chr(7))
			str = "The bell rings, telling you that it is time for " + time.getCurrentActivityName() + ". " +   currentActivity.goToMessage
			next = input(str)
		
		print(room.getDescription())	
		
		room.visited = True
		
		if room.activity == currentActivity.name:
			print(currentActivity.message)
		
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
					person.talkTo(time, room)
					talked = True
					break
			if talked == False:
				print("Talk to whom? I don't understand.")
		
		elif action == currentActivity.activation and action != "":
			if currentActivity.name == room.activity:
				currentActivity.do(player,time)
				time.resetTurn()
			else:
				print("Now's not the time for that!")
		
		
		elif action == "look around":
			print(room.description)
		
		
		elif action == "help":
			str = "look around, go north, go east, go south, go west, use stairs, talk to (insert_persons_name_here), help, quit"
			
			for object in room.objects:
				str += ", " + object.init
			
			print("Avaliable commands:")
			print(str + ".")
			
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
			if len(room.objects) != 0:
				used = False
				for object in room.objects:
					if action == object.init:
						object.use(player,time)
						used == True
				if used == False:
					print("Woops! I didn't understand that! If you are having trouble, please type 'help' for a list of commands. If you are lost, please refer to the map in the manual. (P.S. manual not yet avaliable)")
			
		
		time.endTurn(player)	
		
#play()		
	

def main():

	name = input("What is your name?\n> ")
	you = Character(name)
	
	dialogues.intro(you)
	
	play(you)
	
main()
