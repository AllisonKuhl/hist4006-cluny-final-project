from random import randint
#from monk2 import Player
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
	



def nightRandomEvents(player):

	randInt = randint(1,100)
	
	if randInt < 20:
		vision(player)
	elif randInt < 40:
		nightDemons(player)


def talk(player):

	gossip = ["...And then I said to him, what, are you serious and I said, ya, I'm serious, and then he said...", "Well, personally I think that the habit DOES make him look fat...", "So my cousin wrote to the me the other day and...", "...twenty oxen, can you believe! TWENTY!"]
	
	hello = ["hello", "hi", "hey"]
	
	whatsUp = ["what's up?", "how are you?", "what's new", "whats new", "whats up"]
	
	replies = ["Is that so?", "Wow, that's really interesting.", "Hm.", "Please tell me more.", "No way!"]
	
	reply = replies[randint(0, len(replies)-1)]
	
	rand = randint(0,1)
	
	print("As you approach the monks you hear them say...")

	if rand == 1: #current events... will be implemented later
		print("Abbot Hugh is pretty cool isn't he!")
	else:
		print(gossip[randint(0, len(gossip)-1)])
	
	while True:
		 
		speech = input("You say....\n> ")
		speech = speech.lower()
		
		if speech in hello:
			print('Monk: \n"Hello,', player.getName() + '."')
			
		elif speech == "goodbye":
			print("Monk: \nGoodbye")
			break
		
		elif speech == "tell joke":
			print("You: \nWhat would you say to a novice who's always complaining about his itchy robe?")
			print("Monk: \nWhat?")
			print("You: \nHe has a bad habit!")
			print("Monk: \n.....")
			player.decreaseSins(5, "levity")
			#print("+ 100 sin for bad puns.")
			
		elif speech == "talk about God":
			print("You: \nSo I was thinking about this passage in Revelation the other night...")
			player.increaseHoliness(1)
			print("Monk: \n", reply)
		
		elif speech in whatsUp:
			print("Monk: \nI'm good, and you?")
			
		else:
			print("Monk: \n", reply)
	





def talkToMonks(player):
	
	

	print("You hear some monks talking in the hall.")
	
	#if player.prompt == True:
	if player.prompt == True:
		print("Do you....")
		print("1. Talk to them.")
		print("2. Ignore them.")
		
	action = input("> ")
	
	if action.lower() == "ignore them":
		print("Good idea!")
	
	elif action.lower() == "talk to them":
		talk(player)

	else:
		print("You ignore the monks who are talking and continue on your business.")
			
	

def demonApparation(player):

	demons = ["a giant beast, with jowls dripping wet with saliva exposing teeth sharp as swords, with great hairy legs as big as logs.", "a short deformed being, like a human but not quite, with dark skin and a horribly ugly face.", "some kind of giant black bird, hovering above you glaring at you with burning red eyes.", "a dark swarthy being with horns on his head and slitted eyes."]

	rand = randint(0,len(demons))
	
	print("As you are walking through the halls of an abbey, suddeny you see a demon appearing in front of you! It looks like", demons[rand])
	
	#print("What do you do?")
	
	#action = input("> ")
	
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
	
	rand = randint(0, len(possibilities))
	
	print(possibilities[rand])
	
	
def vision(player):
	
	names = ["Adelmus", "Ethelbert", "Drogo", "Einhard"]
	rand = randint(0,len(names))
	print("While sleeping, you have a strange dream....")
	print("\n A ghostly figure appears in front of you and begins to speak.")
	print('"My name is', names[rand], ' and I was once a powerful lord. My power was such that I did whatever was right in my own eyes and stole from the innocent and ravaged the helpless. Alas, too late did I realize my great sins. At the end of my life I put on the habit and become a monk at this very monastary, and because of this I was spared the eternal torment."')
	print('"However, due to my great sins I have not been able to enter paradise. I entreat you, brother, to have mercy on one who is wretched and tell the abbot to pray for my soul. Only through your prayers will I be able to be saved."')
	print("This said, the figure disappears.")
	


	
