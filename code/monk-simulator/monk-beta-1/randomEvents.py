from random import randint

# chances of monks talking  is .... 20%

#you = Player("Hugh")
#randInt = randint(1,100)

#other random events... chandelier falling, death events, etc....


def normalRandomEvents(player): 
	randInt = randint(1,100)
	
	if randInt < 20:
		talkToMonks(player)	
	elif randInt < 40:
		demonApparation(player)	
	elif randInt < 50:
		demonAbbot(player)
	
	
	randInt = randint(1,100) 
	if randInt <= player.getSickliness() * 2:
		player.changeHealth(True) #makes player sick
		print("You aren't feeling very well. You decide to spend the rest of the day in the infimirary. You sleep for the rest of the day.")

	
	
	

def nightRandomEvents(player, ghost):

	randInt = randint(1,100)
	
	if randInt < 20:
		vision(ghost)
	elif randInt < 40:
		nightDemons(player)








def talkToMonks(player):
	
	killWords = ["kill them", "stab them", "kill monks", "attack monks"]

	print("You hear some monks talking in the hall.")
	
	#if player.prompt == True:
	if player.prompt == True:
		print("Do you....")
		print("1. Talk to them.")
		print("2. Ignore them.")
		
	while True:
		
		action = input("> ").lower()
	
		if action.lower() == "ignore them" or action == '2':
			print("Good idea!")
			break
		
		elif action.lower() == "talk to them" or action == '1':
			player.talk()
			break
		
		elif action.lower() in killWords:
			print("You run at the monks and begin to stab one violently.")
			player.increaseSins(100,"murder")
			#player.die()
			break

		else:
			print("I don't understand that!")
				
	

def demonApparation(player):

	demons = ["a giant beast, with jowls dripping wet with saliva exposing teeth sharp as swords, with great hairy legs as big as logs.", "a short deformed being, like a human but not quite, with dark skin and a horribly ugly face.", "some kind of giant black bird, hovering above you glaring at you with burning red eyes.", "a dark swarthy being with horns on his head and slitted eyes."]

	rand = randint(0,len(demons)-1)
	
	print("As you are walking through the halls of an abbey, suddenly you see a demon appearing in front of you! It looks like", demons[rand])
	
	print("What do you do?")
	
	action = input("> ")
	
	print("You " + action + ".")
	
	#if sins list > 0   "I know you still have unconfessed sins! "
	#if sins are really big...    will make you sick
	#if your holiness is high, the demon has no effect
	#if you pray, then it will go away


def demonAbbot(player):

	print("You meet a stranger in the hall. Do you talk to him?")
	
	while True:
		action = input("> ")
		action = action.lower()
		if action == "yes":
			print("You approach the stranger.")
			print('"Hello there brother!" he says, "My name is Guido and I am from a far off monastary. I couldn\'t help but notice that this monastary is very different from my own. It\'s a lot more work here. You have to say psalms over and over, and you hardly ever get to do anything fun. Things are more exciting at my monastary. Why don\'t you come with me?"')
			while True:
				action = input("You say....\n> ")
				if action.lower() == "yes":
					leaveMonastary()
					break
	
				elif action.lower() == "no":
					print("At your words, the abbot howls and leaves. As he runs through the halls, you notice that his shadow is deformed and he has a tail and horns... Good call!")
					break
				else:
					print("I don't understand that! (reply yes or no)")
			break
			
		elif action == "no":
			print("At your words, the abbot howls and leaves. As he runs through the halls, you notice that his shadow is deformed and he has a tail and horns... Good call!")
			break
		else:
			print("I don't understand that! Say either yes or no!")
			
def leaveMonastary():
	print("You leave the monastary with the abbot but they notice you left and punish you.") #edit more later.
	
def nightDemons(player):
	
	possibilities = ["Suddenly, the beds start shaking and blankets begin to rise into the air as if by an invisible force.", "A giant crow flies over your bed and begins discussing its misdeeds to another fearsome demon.", "You see a shadow in the hall outside of the dormitory. As you watch, a long procession of demons march by as if doing some twisted anti-liturgy. But due to the holiness of the abbey, they are unable to come and harrass the monks."]
	
	rand = randint(0, len(possibilities)-1)
	
	print(possibilities[rand])
	
	
def vision(ghost):
	
	if ghost.inHeaven == True:
		ghost = Ghost()
		
	print("While sleeping, you have a strange dream....")
	print("A ghostly figure appears in front of you and begins to speak.\n")
	ghost.display_message()

