import psalms
import getRule

class Activity():
	def __init__(self, name, message, activation, initMessage):
		self.name = name
		self.message = message
		self.activation = activation
		self.goToMessage = initMessage
	

	def do(self, player, time):
		None

			
class Prayer(Activity):
	def __init__(self):
		Activity.__init__(self, "liturgy", "The monks are preparing to do the liturgy. You should join them.", "join them", "You should get to the main church.")

		
	def do(self, player, time):
		print("You prepare to say the liturgy with the other monks.")
		psalms.responsary(player)
		psalms.say_psalms(23, player, psalms.getPsalms(), 3)
	

class Sleep(Activity):
	def __init__(self):
		Activity.__init__(self, "sleep", "The monks are preparing to go to bed. Maybe you should join them.", "join them", "You should get to the dormitory.")
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
		Activity.__init__(self, "dinner", "The monks are preparing to eat. Maybe you should join them.", "join them", "You should get to the refectory.")

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
		
		
		print("Your food today is some beans and bread.")
		print("Do you eat the food?")
			
		while True:
			action = input("> ").lower()
			
			if action == "eat the food" or action == "yes":
				if time.day == 1:
					print("You eat some food. Delicious! But after a while your throat gets parched. You would like someone to pass the water, but you remember that you are not supposed to speak.")
					print("1. Use hand gestures.")
					print('2. Say "Water"')
					print("3. Explain your predicament.")
					
					while True:
						action = input("> ").lower()
						
						if action == "1":
							print("Excellent choice! The monks immediately understand and pass you some water.")
							break
						if action == "2":
							print("While this is acceptable, you receive a few glares from other monks for disrupting the reading.")
							break 
						if action == "3":
							print("Every eye in the refectory turns to look at you! Silence is to be maintained at all cost in the refectory. As punishment, you are deprived of wine for the rest of the meal!")
							player.increaseSin("talking")
							break
						else:
							print("Please enter a number")
				
				elif time.day == 2:
					print("You want to eat some bread, but the bread is juuuuust out of reach. What should you do?")					
					print("1. Use hand gestures.")
					print('2. Say "Bread"')
					print("3. Explain your predicament.")
					
					while True:
						action = input("> ").lower()
						
						if action == "1":
							print("Excellent choice! The monks immediately understand and pass you some bread.")
							break
						if action == "2":
							print("While this is acceptable, you receive a few glares from other monks for disrupting the reading.")
							break 
						if action == "3":
							print("Every eye in the refectory turns to look at you! Silence is to be maintained at all cost in the refectory. As punishment, your meal is taken away!")
							player.increaseSin("talking")
							break
						else:
							print("Please enter a number")
				
				
				break
			elif action == "don't eat food" or action == "no":
				print("You don't eat the food. How very ascetic of you.")
				player.increaseHoliness()
				break
			else:
				print("I don't understand that.")
				
class Kitchen(Activity):
	def __init__(self):
		Activity.__init__(self, "kitchen work", "Some monks are preparing dinner.", "join them", True, "You should go to the kitchen")
		asleep = False

	def do(self, player, time):
		print("It is your turn on kitchen duty. You enter the kitchen and are given the job of cutting up vegetables for dinner. Another monk is working beside you. Do you:")
		print("1. Say Hello. ")
		print("2. Work in Silence")
		
		while True:
			action = input("> ")
			if action == "1":
				print("The kitchen worker smiles and says, “Hello! You look new here. I am so hungry. You know, technically the Rule only stipulates what it to be eaten in the refectory and we’re not in the refectory. I have some bacon left over from a meal we cooked for the sick. Would you like some?")
				print("yes/no")
				while True:
					action = input("> ").lower()
					if action == "yes":
						print("You eat the piece of bacon and it is delicious. It reminds you of your life before the monastery. You want some more, but this is a grievous sin!!")
						player.increaseSin("gluttony")
						player.increaseSin("lust")
						break
					if action == "no":
						print("Excellent choice! Meat excites lust and that could be very dangerous.")
						break
					else:
						print("Please answer either yes or no.")
				break
			if action == "2":
				print("How very proper of you! You continue to work in silence completing the task quickly.")
				break
			else:
				print("Please enter 1 or 2")

		print("After you finish, you join the other monks in the refectory for dinner.")

				
			
			
