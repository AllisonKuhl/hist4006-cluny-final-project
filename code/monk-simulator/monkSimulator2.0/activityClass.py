import psalms
import getRule

class Activity():
	def __init__(self, name, message, activation, certainTime, initMessage):
		self.name = name
		self.message = message
		self.activation = activation
		self.certainTime = certainTime 
		self.goToMessage = initMessage
	

	def do(self, player):
		None

			
class Prayer(Activity):
	def __init__(self):
		Activity.__init__(self, "liturgy", "The monks are preparing to do the liturgy. You should join them.", "join them", True, "You should get to the main church.")

		
	def do(self, player, time):
		print("You prepare to say the liturgy with the other monks.")
		psalms.responsary(player)
		psalms.say_psalms(23, player, psalms.getPsalms(), 3)
	

class Sleep(Activity):
	def __init__(self):
		Activity.__init__(self, "sleep", "The monks are preparing to go to bed. Maybe you should join them.", "join them", True, "You should get to the dormitory.")
		asleep = False

		
	def do(self, player, time):
	
		print("Now it is time for a nap!")
		print("You can either sleep, or stay up praying instead.")
			
		while True:
		
			user_input = input("> ").lower()
			
			if user_input == "sleep":
				print("You go to sleep.")
				#player.changeSleepiness(-1)
				self.asleep = True
				break
				
			elif user_input == "pray" or user_input == "stay up praying":
				print("You stay up praying instead.")
				player.increaseHoliness()
				self.asleep = False
				break
			else:
				print("I don't understand that.")
				
		if self.asleep == True:
			print("\nThe bell rings.")
			print("DONG!", chr(7))
			print("It's time to wake up! Do you wake up, or sleep more?")
			
			while True:
				user_input = input("> ").lower()
				
				if user_input == "wake up":
					print("You wake up feeling refreshed.")
					break
					
				elif user_input == "sleep more":
					print("You sleep some more.")
					player.increaseSin("laziness")
					break
				else:
					print("I don't understand that.")
				self.asleep == False
		else:
			print("After a while, everyone starts to wake up again.")
			
class Eat(Activity):
	def __init__(self):
		Activity.__init__(self, "dinner", "The monks are preparing to eat. Maybe you should join them.", "join them", True, "You should get to the refectory.")
		asleep = False

	def do(self, player, time):
		print("It is time to eat!")
		print("During dinner, somebody reads.")
		randInt = randint(0,len(ruleExcerpts)-7)
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
				player.increaseHoliness()
				break
			else:
				print("I don't understand that.")
		
