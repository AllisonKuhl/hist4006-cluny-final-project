import psalms
import getRule
import randomEvents
from ghost import Ghost

#some variables
VERSES_SAID = 3 # how many verses of the psalms should we say?
psalmsList = psalms.getPsalms()


ghost = Ghost() #should I put this somewhere else....???
	

class Activity():
	def __init__(self,name, location):
		self.__name = name
		self.__correctAction = "go to " + name
		self.location = location
		self.skip = False

	
	def go_to(self, playerObject):
	
		turns = 0
		
		print(self.__correctAction)
		
		if playerObject.prompt == True:
			print("Now it is time to", self.__correctAction)
	
		while self.skip != True: #... if 'skip' isn't true?
			user_input = (input("> ")).lower()
			if user_input == self.__correctAction:
				print("You", self.__correctAction + ".")
				break
				
			elif "go to" in user_input:
				print("You", user_input + ". But nobody's there! Uh-oh, looks like you went to the wrong place! You end up missing", self.__name + ".")
				self.skip = True	
				break
			
			else:
				self.other_inputs(playerObject, user_input, turns)
				
			turns += 1
				
	def do_action(self, player):
		print("You are in the", self.location + ".")
			
	def getName(self):
		return self.__name
		
	def random_events(self, player):
		randomEvents.normalRandomEvents(player)
		
	def other_inputs(self, player, action, turns):
		if action == "look around":
			print("You look around. You are in the", self.location+".")
		elif "sing" in action:
			print("You sing: 'Lalalalala~~~~'")
		elif "dance" in action:
			print("You start boogying about.")
			player.increaseSins(1,'levity')
		elif "talk" in action:
			print("You shouldn't be talking!")
			player.increaseSins(1, 'talking')
		#if go to church....
		#if pray....
		elif turns > 3:
			print("You've wasted so much time that you've missed " + self.__name + "!")
			self.skip = True
			player.increaseSins(5, "skipping")
		elif action == 'help':
			print("You don't know what to do? Type in where you'd like to go.")
		elif action == 'hint' and turns > 2: 
			print("Right now it is time for", self.__name + ".")
		else:
			print("I don't understand that!")

	
				
class Prayer(Activity):
	def __init__(self, name, psalmNumber):
		Activity.__init__(self, name, "church")
		self.__psalmNumber = psalmNumber
		#self.__psalms = psalms
		
	def setPsalmNumber(self, newNumber):
		self.__psalmNumber = newNumber
		
	def do_action(self, player):
		print("You arrive in the chapel and prepare to say the liturgy.")
		psalms.say_psalms(self.__psalmNumber, player, psalmsList, VERSES_SAID)

		

class FreeTime(Activity):  #needs editing!!!
	def __init__(self):
		Activity.__init__(self, "free time", "dormitory")
		self.action = "read"
	
	def go_to(self, playerObject):
	
		if playerObject.prompt == True:
			print("You have free time now! What would you like to do?")
			print("1. Read")
			print("2. Work")
			print("3. Sleep")
			print("4. Chat with other monks.")
			
		turns = 0
		
		while True:
		
			user_input = input("> ")
			
			if user_input == "read":
				print("You go study scripture.")
				playerObject.decreasePenance(1)
				break
			elif user_input == "work":
				print("You go help the monks work.")
				playerObject.decreasePenance(1)
				break
			else:
				self.other_inputs(playerObject, user_input, turns)
				
			turns += 1

	
class Sleep(Activity):
		def __init__(self):
			Activity.__init__(self, "sleep", "dormitory")
			self.asleep = False
			
		def go_to(self, player):
			if player.prompt == True:
				print("Now it is time to sleep.")
				print("Do you sleep, or stay up praying instead?")
				
			while True:
			
				user_input = input("> ")
				
				if user_input == "sleep":
					print("You go to sleep.")
					player.changeSleepiness(-1)
					self.asleep = True
					break
					
				elif user_input == "pray":
					print("You stay up praying instead.")
					player.decreasePenance(10)
					player.changeSleepiness(1)
					self.asleep = False
					break
				else:
					print("I don't understand that.")
					
		def do_action(self, player):
			if self.asleep == True:
				print("\nThe bell rings.")
				print("DONG!", chr(7))
				print("It's time to wake up! Wake up, O sleeper, arise!")
				
				while True:
					user_input = input("> ")
					
					if user_input == "wake up":
						if player.sleepiness > 3:
							print("You try and wake up, but you're too tired. Before you know it, you're drifting off to sleep.")
							player.increaseSins(5, "laziness")
							self.skip == True
						else:
							print("You wake up feeling refreshed.")
						break
						
					elif user_input == "sleep more":
						print("You sleep some more.")
						player.increaseSins(5, "laziness")
						self.skip == True
						break
					else:
						print("I don't understand that.")
					self.asleep == False
					
		def random_events(self, player):
			randomEvents.nightRandomEvents(player, ghost)
					

class ChapterMeeting(Activity):
	def __init__(self):
			Activity.__init__(self, "chapter meeting", "chaptorium") #or wherever chapter meetings took place????
					
			
	def do_action(self, player):
	
		print("\n Do you have any sins to confess? y or n")
		
		while True:
			userInput = input("> ").lower()
			
			if userInput == 'y':
				break 
			elif userInput == 'n':
				if you.getSins() == 0:
					break
				else:
					print("I don't think that's the case... But okay...")
					break		
			else:
				print("I don't understand that! Please type either y or n")
					
		if userInput == "y":
			
			while you.getSinsListLength() > 0:
				sin = input("What sins do you have to confess? \n > ")
				
				if you.prompt == True:
					print("Type exit to exit and hint for a hint if you can't remember what sins you've done.")
				you.confessSin(sin)				
				if you.getSinsListLength() == 0:
					print("You have no more sins to confess!")				
				if sin == 'exit':
					break
				
				if sin == "hint" and you.prompt == True:
					you.getHintSins()
						

class Dinner(Activity):
	def __init__(self):
			Activity.__init__(self, "dinner", "refectory") 
					
	def do_action(self, player):
		print("It is time to eat!")
		print("While you eat, somebody reads.")
		randInt = randint(0,len(ruleExcerpts)-1)
		print("\n",ruleExcerpts[randInt], ruleExcerpts[randInt+1], ruleExcerpts[randInt+2])
		
		action = input("> ")
		
		if action != "listen" or action != "eat":
			if action == "don't eat":
				print("You don't eat the food in front of you.")
				player.decreasePenance(2)
			
			if action != "eat":
				print("You are supposed to listen!")
				player.increaseSins(1,"not listening to rule")
		
		print("\n",ruleExcerpts[randInt+3], ruleExcerpts[randInt+4], ruleExcerpts[randInt+5])
		
		
class GetDressed(Activity):
	def __init__(self):
		Activity.__init__(self, "get dressed", "dormitory")

	
	#def go_to(self, player)
	
	def random_events(self, player):
		None
		
		
	def do_action(self, player):
		print("What should you wear today?")
		if player.prompt == True:
			print("1. Plain habit.")
			print("2. Haircloth.")
		
		while True:
		
			clothes = input("> ")
			if clothes == "haircloth":
				print("You decide to wear the hair cloth. It's not very comfortable.")
				player.decreaseHealth(1)
				player.decreasePenance(2)
				break
			elif clothes == "plain habit" or clothes == "habit":
				print("You wear your regular old everyday habit. A tried but true fashion.")
				break
			else:
				print("I don't understand that!")
		
		
		
		
