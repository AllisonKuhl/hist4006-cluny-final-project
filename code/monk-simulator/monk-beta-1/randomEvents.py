from random import randint
from player import Player
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
		
	elif randInt < 70:
		romance(player)
	
	
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
			player.increaseSins("murder")
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


def romance(player):
	
	rand = randint(0,100)
	if rand < 50: #romance 1
		servantGirl(player)
	else:
		oblate(player)
	
	

def servantGirl(player):
	
	player.meetings1 += 1
	print("You see a pretty servant girl walking through the halls carrying some vegetables. You can't help but think she's very beautiful.")
	player.increaseSins("impure thoughts")
	print("What should you do?")
	print("1. Ignore")
	print("2. Say hello")
	print("3. Flirt")
	
	while True: 
		action = input("> ").lower()
		
		if action == "ignore" or action == '1':
			print("Good decision!")
			break
			
		elif action == "say hello" or action == "2":
			print("You come up and say hello.")
			player.increaseSins("talking")
			romance1(player)
			break
			
		elif action == "flirt" or action == '3':
			print('You say: "Hey there beautiful."')
			player.increaseSins("romance")
			
			if player.romance1lvl > 3:
				print('She blushes happily and hits you on the arm. "S-stop it! Stupid! What if somebody finds out?"')
				player.romance1lvl+= 1
				
			elif player.meetings1 > 3:
				print('"W-what do you want? Why do you keep doing this to me? Can\'t you just leave me alone?"')
				player.romance1lvl -= 2
				break
			
			elif player.meetings1 == 3:
				print('She asks: "What do you want from me?!"')
				print("You say...")
				print("1. Your body")
				print("2. Nothing.")
				
				while True:
				
					action = input("> ")
					if action == "1":
						print('You press her against the wall. "I think you know what I want", you say.')
						print(".....")
						player.sins(5,'romance')
						break
					if action == "2":
						print('You stare at her for a bit, then turn away abruptly, as if coming to your senses. "Nevermind," you tell her.')
						break
				break		
			
			else:
				print('She turns deep red and quickly moves away avoiding your eyes."')
				player.romance1lvl -= 1
				break
				
		else:
			print("Please enter a number.")
	
	
	

	
	
def romance1(player):
		
	if player.romance1 != "closed":
			player.romance1lvl += 1
	
	if player.meetings1 <= 2 or player.romance1 == "closed": #should have a boolean?
		print("She blushes and quickly moves away.")
		
	elif player.meetings1 <= 4 and player.romance1lvl >= 2:
		print('She looks at you shyly. "....Hello...". She blushes and continues down the hall.')
	
	elif player.meetings1 > 4 and player.romance1lvl > 2:
		print('"You again?", she laughs. "What do you want?"')
		print("You say....")
		print("1. I just want to talk to you.")
		print("2. Do you need any help?")
		print("3. I want.... you!")
		
		while True: 
			action = input("> ").lower()
			
			if action == '1':
				print("You tell her you just wanted to talk to her.")
				print('"Me?", she replies..., "But I\'m just an uneducated servant..."')
				print('You tell her that doesn\'t matter. She blushes. "I should get back to work," she says.')
				player.romance1lvl += 1
				break
		
			if action == "3":
				if player.romance1lvl > 5:
					print('She blushes deeply. "I\m sorry," you say, "...I guess I stepped out of bounds." You turn to leave, but then you feel a tug on your habit. "...Don\'t go..." she says quietely. "I....I want you to stay."')
					print("Then you kiss.")
					player.increaseSins("kissing")
					player.romance1 = 'kissed'
					
					
				else:
					print('She blushes and frowns at you. "Whaaa? How can you say that!? Don\'t be stupid! We can never be together!" She pulls herself away from you and hurries down the hall.')
					player.romance1lvl -= 1
				break
				
			if action == '2':
				print("You ask her if she needs any help. Those vegetables look kind of heavy.")
				print('"H-help me?!" she stutters, "But...I\'m just a servant here, you shouldn\'t.... I mean...you shouldn\'t demean yourself to helping someone like me.')
				print("You say....")
				print("1. No problem. This is what Jesus would do.")
				print("2. Someone like *you* is worth it~ <3")
				print("3. k bye")
				
				while True:
					response = input("> ")
					
					if response == '1':
						print("You tell her that your love of Christ compels you to help all those in need, whether a servant or a king, and that you, a poor miserable sinner, is just as wretched as she, so it is really no trouble at all.")
						print('"...I see..." she responds. She looks strangely disapointed?')
						player.holiness += 5
						break
		
					if response == '2':
						print('She blushes deeply. "Waaa?" she says, "D-don\'t say things like that! What if the abbot finds out?" She rushes away quickly. But she\'s smiling.')
						player.romance1lvl += 1
						#romance up
						break

					if response == '3':
						print("You leave.")
						break
						
					else:
						print("I don't understand that!")
			break 
		else:
			print("I don't understand that! Enter a number!")
		
	if player.romance1lvl < 0:
		print('She stares at you coldly, "I don\'t want to talk to you," she says, and hurries down the hall.')
		player.romance1lvl += 1
		
	if romance1 == 'closed':
		print('"I\'m sorry..." she says,"I can\'t talk to you anymore..."')
		
def oblate(player):
	
	
	player.meetings2 += 1
	print("You see some young monks walking through the hall. You can't help but notice one in particular... He's thin and skinny and looks about 17 years old. His skin is very fair and smooth, and his hair thick and brown and curly. He's very beautiful.")
	player.increaseSins("impure thoughts")
	
	print("What should you do?")
	print("1. Ignore him")
	print("2. Talk to him")
	print("3. Flirt")
		
	while True:
		action = input("> ").lower()
		
		if action == "ignore him" or action == "1":
			print("Good idea! You're ashamed to have even considered doing otherwise.")
			break
		
		if action == "talk to him" or action == "2" or action == "talk":
			romance2(player)
			player.increaseSins("talking")
			break
			
		if action == "flirt" or action == "3":
			
			if player.romance2lvl > 4:
				print("You wait until nobody is around before you approach him.")
				print("Suddenly you kiss him.")
				print("He kisses you back.")
				player.increaseSins("sodomy")
		
			else:
				print("You wait until nobody else his around before you approach him.")
				print("You tell him you think he's very attractive.")
				print('"The boy says, "!!!!!! >:O"')
				if player.romance2 != "continued":
					player.romance2 = "alarmed"
				player.increaseSins("romance")
			break
		else:
			print("I don't understand that!")
			
		
def romance2(player):
	
	player.romance2lvl += 1
	print("What do you want to talk about?")
	print("1. God")
	print("2. The boy")
		
	while True:
		action = input("> ").lower()
		
		if action == '1':
			print('You discuss some Bible passages.')
			break
		if action == '2':
		
			if player.romance2lvl == 3:
				print("You ask him how he likes the monastary.")
				print('"It\'s nice..." he says... "But sometimes I wish I could... Nevermind."')
			else:
				print("You ask him about himself.")
				print("He shrugs and tells you that there isn't much to say. He's been here his whole life.")
		
			break
		

	
