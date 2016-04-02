'''
To-Do

-Add different people and conversation and events for each day
-make liturgy more interesting (and different for each one?)
- add more people if more dialogue options
- get the exposition monk to follow you around

'''
from AdventureInit import Abbey
from player import Character
from timeClass import Time
import dialogues
cluny = Abbey()


def play(player):
	action = ""
	time = Time()
	room = cluny.startRoom
	
	while action != "quit":
		
		
		currentActivity = time.getCurrentActivityClass()
		
		
		if time.turns == 0:
			print(chr(7) +"The bell rings, telling you that it is time for", currentActivity.name,  currentActivity.goToMessage)
		
		print(room.getDescription())	
		
	
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
					person.talkTo(time)
					talked = True
					break
			if talked == False:
				print("Talk to whom? I don't understand.")
		
		
		elif action == currentActivity.activation and action != "":
			if currentActivity.name == room.activity:
				currentActivity.do(player,time)
				time.turns = -1
				time.activityIndex += 1
			else:
				print("Now's not the time for that!")
		
		
		
		
		
		elif action == "help":
			print("Avaliable commands:")
			print("go north, go east, go south, go west, use stairs, talk to (insert_persons_name_here), help, quit, ")
			
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
			print("Woops! I didn't understand that! If you are having trouble, please type 'help' for a list of commands. If you are lost, please refer to the map in the manual. (P.S. manual not yet avaliable)")
			
	
		time.endTurn()	
		
#play()		
	

def main():

	name = input("What is your name?\n> ")
	you = Character(name)
	
	dialogues.intro(you)
	
	play(you)
	
main()
