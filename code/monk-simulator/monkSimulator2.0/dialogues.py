

def intro(player):
	
	print("Welcome,", player.name + ". You are a knight from a noble family. For many years you have been living a life of iniquity. You have pillaged the poor, attacked the defenceless and terrorized the innocent, doing in all ways whatever was right in your own eyes. But recently you've been rethinking your life. After a certain life-changin event, you have realized the errors of your way. Overcome with remorse for your past actions, you decided to renounce your previous life entirely and become a monk. And so, you arrive at the monastary of CLUNY, hopeful that the life of a monk will purify your past sins.")
	print("But will it be enough to make it to heaven? Only YOUR actions will decide!")
	
	action = input("..... continue?")
	
	print("\nThe bell rings.")
	print("DONG!", chr(7))
	print("Groaning, you turn over on your uncomfortable cot. It's too early to wake up!")
	action = input("Wake up? > ").lower()
	wakeup = ["yes", "wake up", "y", "get up"]
	if action in wakeup:
		print("You wake up.")
	
	else:
		print("You decide you'd rather sleep. It's not even light out yet!")
		print("Unfortunately somebody shakes you awake.")
		print(player.name + "! Wake up!")
		print("You reluctantly wake up.")
		
	print("You are in the dormitory. There is an exit to the east. There is an exit to the west. John is here.")
	
	while True:
		action = input("What would you like to do?\n> ").lower()
		
		if "go" in action:
			print('John says: Wait! Do you know where you\'re going? Before you leave, you should talk to me!"')
		
		elif action == "talk to john":
			break
		else:
			print("Now's not the time for that!")
	

	print("John says: Good morning, " + player.name + "! Although, it's not actually morning! It's the middle of the night! I know that you're new here, so things might be a bit confusing at first. But don't worry! I'm here to help you. If you have any questions, don't hesitate to ask.")
	
	print("You ask...(please type the number)")
	print("1. Where to go")
	print("2. About the Abbey")
	print("3. Who are you?")
	print("4. exit conversation")
	
	while True:
		question = input("> ")
		print("John says: ")
		if question == "1":
			print("Right now, we are about to celebrate nocturnes in the church, so you better head over there. To get to the church, you need to go downstairs, then go right, then go left, then go right. By the way, you know how to move around, right? Just type: \"Go north\" or \"Go south\" or whatever direction you want to go.You got all that? Ask again and I'll repeat it for you. ")
		elif question == '2':
			print("Cluny was founded many years ago and was made great by many holy men such as Saint Odo, Saint Maijolus and Abbot Hugh. Recently we've been rebuilding the church, and now it's the biggest, greatest church in all of Europe! We control lots of land, and thanks to Cluny's prayers, many souls have been saved.")
		elif question == "3":
			print("My name is John. I've lived in this abbey my whole life. So I know everything there is to know about it!")
		elif question == "4":
			print("You're right. We should probably get going. It'll be bad if we don't make it there in time! If, after 15 turns, we don't make it to the next spot, we'll get in trouble!")
			break
				
			
	
	
	
def fashionableMonk(self, time):

	print("Hello brother. Is it not pious to suffer for God?")
	print("yes/no")

	while True:
		answer = input("> ").lower()
		print("Einhard says....")
		if answer == '1' or answer == "yes":
			print("I knew you would agree, for you appear wise. Gaze upon this, brother ...")
			print("The monk shifts his monastic habit in order to reveal to you a tunic worn tight to his body and made of uncomfortable, scratching, animal hair.")
			print("... Well? Is it not ascetic?")
			while True:
				print("yes or no")
				answer = input("> ")
				print("Einhard says...")
				if answer == "yes":
					print("Of course, as I am sure you are aware, I seek to imitate the most pious of men, those desert fathers who suffered in order to express their humility and devotion to our Lord. Now, I shall pray, for I seek to be closer to our Lord.")
					break
				elif answer == "no":
					print("Ah ...")
					print("The monk's mood clearly shifts from a calm enthusiasm to being somber")
					print("... I am sorry that you do not see the virtue in my actions. Do have a good day. Bless you.")
					break
				else:
					print("Answer either yes or no!")
			break
		elif answer == '2' or answer == 'no':
			print("Do not be so ridiculous, brother. Here, look ...")
			print("The monk reveals an uncomfortable hair shirt underneath his habit")
			print("... I am suffering just as those most holy men who came long before us had, and in doing so I seek to express my devotion to our Lord. In fact, I shall pray right now.")
			break
		else: 
			print("Answer either yes or no!")
	
def saintlyMonk(self,time):

	if self.meetings == 0:
		print("I like to read saint's lifes. They're really great. I want to try and be like a saint too! From now on, I'm going to act perfectly saint-like!")
	if self.meetings == 1:
		print("But wait, if I'm talking to you, doesn't that automatically disqualify me from being saint-like? Oh nooo!")
	if self.meetings == 2:
		print("In the life of Saint Odo, our ancient abbot of blessed memory, there is a story about two monks who were captured, but thanks to their diligent silence they were delivered from the snares of the enemy. That's why you won't catching me talking ever, nope, not ever!")
	if self.meetings == 3:
		print("Wait a minute, why am I still talking?")
	if self.meetings > 3: 
		print("Stop talking to me!!!!")
	
	
	
def oldNovice(self,time):

	if time.day == 1:
		print("I became a monk later in life. But even though I'm older than nearly everybody else here, they still outrank me because they became monks before me. And then they laugh at me because I don't know what to do. Bah! Heaven better be worth it!")

		
def sincereMonk(self,time):

	if self.meetings == 0:
		print("I'm the only son of a powerful family. But what use is power when it's so fleeting? You gain land and then its split between your children as soon as you die. All is vanity! But God's power never disappears. He is the source of all power. So even though my parents wanted me to become a knight, I decided to become a monk instead. The world passes away, but the one who does the will of God lives forever.")
	if self.meetings > 0:
		print("The world with its lust is passing away, but the one who does God's will remains forever")
	

def sleepyMonk(self,time):
	if self.meetings == 0:
		print("I don't like waking up early for vigils. I wish I could sleep all time.")
	if self.meetings == 1:
		print("I always get in trouble for sleeping during the liturgy. In the early services, a monk always walks around with a lantern to check if you are sleeping. Once see me, I have to take the lantern, since I'm always sleeping!")
	if self.meetings > 1:
		print("I'm tired...")
	
	
def PontiusFollower(self,time):
	
	if time.day == 1:
		print("Our abbot Pontius is really great!")
	
	if time.day == 2:
		print("The pope told us that Pontius abdicated, so we need to elect a new abbot. But personally, I don't believe it. Pontius did nothing wrong. He would never leave us.")
		
	if time.day == 3:
		print("I heard that Pontius might be coming to visit us soon! I'm so excited!")
		
		
		
		
def grumpyMonk(self,time):
	
	if time.day == 1:
		if self.meetings == 0:
			print("Bah! Monks these days! Back when Abbot Hugh was alive, things were so much better! I'm telling you, monasticism is just going downhill from here. Back in my days, we actually followed the Rule of Benedict like we meant it!")
			
		if self.meetings == 1:
			print("BAH!")
	
	if time.day == 2:
		if self.meetings == 0:
			print("So I hear we're going to elect a new abbot. Bah! There's no point! Things will never be as good as they were when Abbot Hugh was alive.")
		if self.meetings >  0:
			print("Monks these days are spoiled rotten!")
			
	if time.day == 3:
		if self.meetings == 0:
			print("Bah! Monks these days and their new-fangled ways! Back when Pontius was the abbot, you wouldn't see any of this nonsense.")
		if self.meetings > 0:
			print("Life was better when I was a kid!")
			
		
def indecisiveMonk(self,time):
	
	if time.day == 1:
		print("I think abbot Pontius is the best!")
		
	if time.day == 2:
		print("I wonder who should be our new abbot? It's so difficult to decide!")
		
	if time.day == 3: 
		print("Abbot Peter is the best!")
		
		
		
def humbleMonk(self,time):
	print("Always remember that you are a worm.")
	
	
def child1(self,time):
	if time.day != 4:
		if self.meetings == 0:
			print("What are you doing in here? You sicko.")
		if self.meetings == 1:
			print(".....")
		if self.meetings == 2:
			print("....Are you trying to hit on me?")
		if self.meetings == 3:
			print("Pervert.")
	
	
def child2(self,time):
	if time.day != 4:
		if self.meetings ==0:
			print("My best friend and I used to always get in trouble for talking during our lessons. So we invented our own language using hand gestures. But then we got in trouble for using that too!")	
		if self.meetings > 0:
			print("Because we aren't supposed to talk, a lot of monks use hand gestures to communicate.")
	
def child3(self,time):
	if time.day != 4:
		print("My parents donated me to this monastary when I was little. Cluny is the only thing I know!")
	
def reprimandMonk(self,time):
	if self.meetings == 0:
		print("You shouldn't be talking. Remember that the tongue is a fire, a world of iniquity.")
	if self.meetings == 1:
		print("....What did I tell you last time?")	
	if self.meetings == 2: 
		print(".....")
	if self.meetings > 2:
		print("You shouldn't be talking.")


def travellingMonk(self,time):
	if time.day == 1:
		print("Hey, I just got back to Cluny from a long trip. I was dealing with a conflict between the monastary and a local bishop. Cluny is supposed to be immune from their authority, but lately there's been a lot of conflicts. But Pontius is determined to uphold Cluny's authority in the face of these usurping bishops!")
		print("1. Ask about immunity.")
		print("2. Ask about trip")
			
		while True:
			question = input("> ")
			print(self.name, "says:")
			if question == "1":
				print("When Cluny was founded, we were given a charter that subjects us only to the Pope. So that means that lords or nobles or bishops or anybody other than the pope can't tell us what to do!")
				break
			if question == "2":
				print("Cluny owns a lot of land in many different places. So I had to travel far away to deal with this problem.")
				break
			else:
				print("Please enter a number between 0 and 3.")
	if time.day == 2:
		print("Hey, I just got back from Cluny from a long trip. I was dealing with a conflict with a local lord over some territory of Cluny. And you won't believe what happened!")
		print("1. What happened?")
		print("2. Ok.")
	
			while True:
			question = input("> ")
			print(self.name, "says:")
			if question == "1":
				print("Well! When the nefarious lord tried to defend his land, he fell over dead. Truly is Cluny defended by God!")
				break
			if question == "2":
				print("Ok.")
				break
			else:
				print("Please enter a number between 0 and 3.")
	
	if time.day == 3:
		print("Hey. I just got back from visiting some of Cluny's territories far away. Unfortunately our income hasn't been as great recently, so we all need to put our weight together.")
	
	
def miracleMonk(self,time):
	print("Hey, I just heard the craziest thing.")
	#miracle story
	
	if self.meetings > 1:
		print("Want to hear some more miracles?")
		print("yes/no")
		while True:
			answer = input("> ").lower()
			print(self.name, "says: ")
			if answer == "yes":
				print("Okay!")
				#randomized miracle
			if answer == "no":
				print("Well, your loss.")
				if time.day >= 3:
					print("At least the abbot likes my miracle stories. He says he'll write them down in a book one day!")
	
	
def pilgrim(self,time):
	print("I wanted to go to Rome, but Cluny was closer.")
	


	
	
	
	
	
	
