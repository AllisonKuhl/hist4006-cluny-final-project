import psalms
import getRule
import randomEvents
from ghost import Ghost
from random import randint

#some variables
VERSES_SAID = 3 # how many verses of the psalms should we say?
psalmsList = psalms.getPsalms()
ruleExcerpts = getRule.getRule()

ghost = Ghost() #should I put this somewhere else....???
	

class Activity():
	def __init__(self,name, location):
		self.__name = name
		self.__correctAction = "go to " + name
		self.location = location
		self.skip = False

	
	def go_to(self, playerObject):
	
		turns = 0

		
		if playerObject.prompt == True:
			print("Now it is time to", self.__correctAction)
	
		while self.skip != True: #... if 'skip' isn't true?
			user_input = (input("> ")).lower()
			if user_input == self.__correctAction:
				print("You", self.__correctAction + ".")
				break
				
			elif user_input.rstrip(" ") == "go to":
				print("Go to where?")
				
			elif "go to" in user_input:
				print("You", user_input + ". But wait! You were supposed to go to " + self.__name + " Uh-oh, looks like you went to the wrong place! You end up missing " + self.__name + ".")
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
			player.increaseSins('levity')
		elif "talk" in action or "say" in action:
			print("You shouldn't be talking!")
			player.increaseSins('talking')
		#if go to church....
		#if pray....
		elif turns > 3:
			print("You've wasted so much time that you've missed " + self.__name + "!")
			self.skip = True
			player.increaseSins("skipping")
		elif action == 'help':
			print("You don't know what to do? Type in where you'd like to go. If you don't know, try asking for a hint?")
		elif action == 'hint' and turns > 1: 
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
		rand = randint(0,1)
		if player.sleepiness > 2 and rand == 1:
			print("You are so tired that you fall asleep during the liturgy! Uh-oh!")
			player.changeSleepiness(-1)
			player.increaseSins("sleeping")
		else:
			psalms.responsary(player)
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
			print("5. Private mass")
			
		turns = 0
		
		while self.skip != True:
		
			user_input = input("> ").lower()
			
			if user_input == "read" or user_input == '1':
				self.read(playerObject)
				break
			elif user_input == "work" or user_input == '2':
				self.work(playerObject)
				break
			elif user_input == "sleep" or user_input == '3':
				print("You go to sleep.")
				playerObject.changeSleepiness(-1)
				playerObject.increaseSins("laziness")
				break
			elif user_input == "chat with other monks" or user_input == '4':
				playerObject.talk()
				break
			
			elif user_input == "private mass" or user_input == "5":
				print("You go to chapel for a private mass.")
				print("Is there anyone in particular you'd like to pray for?")
				person = input("Pray for.... > ")
				if person == ghost.name:
					ghost.massesSaid += 1
				print("You pray for", person + ".")
				break
				
			else:
				self.other_inputs(playerObject, user_input, turns)
				
			
				
			turns += 1
			
	def do_action(self, player):
		None
		#maybe... if self.action == so and so... do such and such activity??? 
		#maybe unnecessary tho 
		
		
	def read(self, player):
	
		print("What would you like to read?")
		print("1. The Bible")
		print("2. Ovid")
		print("3. Saint's Lives")

	
		while True:			
			response = input("> ")
			if response == "the Bible" or response == "1":
				print("Good idea!")
				player.decreasePenance(1)
				break
			elif response == "Ovid" or response == "2":
				print("Scandalous!")
				player.increaseSins("pagan literature")
				break
			elif response == "Saint's Lives" or "3":
				print("Good idea! You read about the life of St. Maiolus, one of the great abbots of this monastary.")
				player.decreasePenance(1)
				break
			else:
				print("I don't understand that!")
		
	def work(self, player):
	
		print("What kind of work would you like to do?")
		print("1. Hard labour")
		print("2. Illumination")
		print("3. Composition")
		while True:
			
			response = input("> ")
			if response == "hard labour" or response == "1":
				print("Nothing like some hard manual labour to get the blood pounding and the soul closer to God!")
				player.decreasePenance(3)
				player.decreaseHealth(1)
				player.changeSleepiness(1)
				break
			elif response == "illumination" or response == "2":
				print("You go to the scriptorium and help copy and decorate books.")
				player.decreasePenance(1)
				break
			elif response == "composition" or response == "3":
				print("You decide to write a literary masterpiece.")
				print("Please begin.")
				art = input("> ")
				if "god" in art.lower():
					player.decreasePenance(2)
				print("Beautiful! Truly a masterpiece for the ages.")
				break
				
			
	
class Sleep(Activity):
		def __init__(self):
			Activity.__init__(self, "sleep", "dormitory")
			self.asleep = False
			
		def go_to(self, player):
			if player.prompt == True:
				print("Now it is time to sleep.")
				print("Do you sleep, or stay up praying instead?")
				
			while True:
			
				user_input = input("> ").lower()
				
				if user_input == "sleep":
					print("You go to sleep.")
					player.changeSleepiness(-1)
					self.asleep = True
					break
					
				elif user_input == "pray" or user_input == "stay up praying":
					print("You stay up praying instead.")
					player.decreasePenance(2)
					player.changeSleepiness(2)
					player.decreaseHealth(1)
					if player.getSleepiness() >= 4:
						print("You barely manage to stay awake...")
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
					user_input = input("> ").lower()
					
					if user_input == "wake up":
						if player.sleepiness > 3:
							print("You try and wake up, but you're too tired. Before you know it, you're drifting off to sleep.")
							player.increaseSins("sleeping")
							player.changeSleepiness(-4)
							self.skip == True
						else:
							print("You wake up feeling refreshed.")
						break
						
					elif user_input == "sleep more":
						print("You sleep some more.")
						player.increaseSins("sleeping")
						player.changeSleepiness(-2)
						player.decreaseHealth(-1)
						self.skip == True
						break
					else:
						print("I don't understand that.")
					self.asleep == False
					
		def random_events(self, player):
			if self.asleep == True:
				randomEvents.nightRandomEvents(player, ghost)
					

class ChapterMeeting(Activity):
	def __init__(self):
			Activity.__init__(self, "chapter meeting", "chaptorium") #or wherever chapter meetings took place????
					
			
	def do_action(self, player):
	
		sins = player.getSinsList()
		
		print("\n Do you have any sins to confess? y or n")
		
		while True:
			userInput = input("> ").lower()
			
			if userInput == 'y':
				break 
			elif userInput == 'n':
				if player.getSins() == 0:
					break
				else:
					print("I don't think that's the case... But okay...")
					break		
			else:
				print("I don't understand that! Please type either y or n")
					
		if userInput == "y":
			
			if player.getSinsListLength() == 0:
				print("You don't have any sins to confess!")
							
			while player.getSinsListLength() > 0:
				if player.prompt == True:
					print("Type exit to exit and hint for a hint if you can't remember what sins you've done.")
				sin = input("What sins do you have to confess? \n > ")
				
				
					
				#times = input("How many times have you done this?") 
				#should I have it so you can decrease it multiple times at once?? +.+?
				player.confessSin(sin)	

				if player.getSinsListLength() == 0:
					print("You have no more sins to confess!")
						
				if sin == 'exit':
					break
				
				if sin == "hint" and player.prompt == True:
					player.getHintSins()
		

		#denunciations
		
		if "romance" in sins and player.romance1 == "kissed":
			print("The chapter meeting is finishing up when suddenly a voice pierces the silence.")
			print('"WAIT!"')
			print("One of the monks is standing, pointing dramatically at you.")
			print("I saw " + player.getName() + " kissing a servant girl the other day!!!!")
			print("The monks all gasp collectively.")
			print('"' + player.getName() + '! Is that true?!" asks the abbot.')
			player.romance1 = 'closed'
			print("You say...")
			while True:
				action = input("> ").lower()
				
				if action == "yes":
					print('"Well... as long as you\'ve admitted it now. However, this is a serious crime, and you shouldn\'t have kept it from us for so long! You\'re going to have to pay a lot of penance for this!"')
					print("Your penance increased by 8!")
					player.__penance += 8
					break
					
				elif action == "no":
					print('"That\'s not true!" shouts the other monk, "I saw them with my own two eyes!"')
					print('"The other monks deliberate for a bit. Eventually they turn to you."')
					print('"' + player.getName() + ', I\'m afraid that you have greatly sinned. Since you refused to admit it, I\'m afraid that you\'re going to have to be punished.')
					print("You penance increased by 15!")
					player.__penance += 15
					break
				else:
					print("Please answer either yes or no.")

		if player.romance2 == "alarmed":
			print("The chapter meeting is finishing up when suddenly a voice pierces the silence.")
			print('"WAIT!"')
			print("It is the boy you hit on earlier. His voice is shaking.")
			print('"This monk....!" he says, "He tried to.... he... said that... What he did cannot even be said in polite company! You know what I mean!"')
			print("The monks gasp collectively.")
			print('"' + player.getName() + '! Is that true?!" asks the abbot. "Did you try and commit sodomic acts with this boy?')
			print("You say...")
			
			while True:
				action = input("> ")
				
				if action == "yes":
					print("The monks gasp collectively once more, but the abbot gestures for them to be quiet.")
					print('"Well... as long as you\'ve admitted it now. However, this is a very serious crime, and you should\'ve confessed it earlier. You\'re going to have to pay a lot of penance for this!"')
					print("Your penance increased by 8!")
					player.__penance += 8
					break
			
				if action == "no":
					print('"I see," the other monks mutter to themselves. They turn toward the younger monk and begin to scold him. "You shouldn\t slander your superiors!"')
					print("...You feel a little bit guilty.")
					player.increaseSins("lying")
					player.romance2 = "continued"
					
				else:
					print("Please answer either yes or no!")
					
					

class Dinner(Activity):
	def __init__(self):
			Activity.__init__(self, "dinner", "refectory") 
					
	def do_action(self, player):
		print("It is time to eat!")
		print("During dinner, somebody reads.")
		randInt = randint(0,len(ruleExcerpts)-1)
		print("\n",ruleExcerpts[randInt], ruleExcerpts[randInt+1], ruleExcerpts[randInt+2])
		
		if player.prompt == True:
			print("Listen to the rule?")
		action = input("> ").lower()
		
		if action != "listen" and action != "yes" and action != "ok":
			print("You are supposed to listen!")
			player.increaseSins("not listening to rule")
		else:
			print("Good idea.")
		print("\n",ruleExcerpts[randInt+3], ruleExcerpts[randInt+4], ruleExcerpts[randInt+5])
		
		
		print("Your food today is some bread and vegetable soup.")
		if player.prompt == True:
			print("Do you eat the food?")
			
		while True:
			action = input("> ").lower()
			
			if action == "eat the food" or action == "yes":
				print("You eat the food. Delicious.")
				break
			elif action == "don't eat food" or action == "no":
				print("You don't eat the food. How very ascetic of you.")
				player.decreaseHealth(1)
				player.decreasePenance(2)
				break
			else:
				print("I don't understand that.")
		
class GetDressed(Activity):
	def __init__(self):
		Activity.__init__(self, "get dressed", "dormitory")
		
	def go_to(self, player):
		None

	def random_events(self, player):
		None
		
		
	def do_action(self, player):
		print("Now it is time to get dressed.")
		print("What would you like to wear?")
		if player.prompt == True:
			print("1. Plain habit.")
			print("2. Haircloth.")
		
		while True:
		
			clothes = input("> ").lower()
			if clothes == "haircloth" or clothes == '2':
				print("You decide to wear the hair cloth. It's not very comfortable.")
				player.decreaseHealth(1)
				player.decreasePenance(2)
				break
			elif clothes == "plain habit" or clothes == "habit" or clothes == '1':
				print("You wear your regular old everyday habit. A tried but true fashion.")
				break
			else:
				print("I don't understand that!")
		
		
		
		
