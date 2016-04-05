from random import randint

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
				
			


#novices	
	
def oldNovice(self,time):

	if time.day == 1:
		print("I became a monk later in life. But even though I'm older than nearly everybody else here, they still outrank me because they became monks before me. Life is so unfair.")

		
def sincereMonk(self,time):

	if self.meetings == 0:
		print("I'm the only son of a powerful family. But what use is power when it's so fleeting? You gain land and then its split between your children as soon as you die. But God's power never disappears. He is the source of all power. The world passes away, but the one who does the will of God lives forever.")
	if self.meetings > 0:
		print("The world with its lust is passing away, but the one who does God's will remains forever")

def sleepyMonk(self,time):
	if self.meetings == 0:
		print("I don't like waking up early for vigils. I wish that I could sleep all time.")
	if self.meetings == 1:
		print("I always get in trouble for sleeping during the liturgy. During vigil, if you are caught sleeping you have to walk around with a lantern until you catch someone else sleeping. But walking around with that lantern just makes me more tired!")
	if self.meetings > 1:
		print("ZZZzzzzzz...")
	
def sicklyMonk(self, time):
	print("I was sick a lot as a child, so I wasn't very suited to life at court. Eventually my parents decided to send me to the monastary.")
	

def visitingMonk(self, time):
	print("I'm actually from a different monastary, but I've been staying at Cluny for a while. It's been great seeing how they do things differently here. Just wait until I tell the monks back home!")
	
	
	
	
#cloister monks	
	
def pontiusFollower(self,time):
	
	if time.day == 1:
		print("Our abbot's really great. He upholds the authority of Cluny against any villain who dares to oppose it!")
	
	if time.day == 2:
		if self.meetings == 0: 
			print("The pope told us that Pontius abdicated, so we need to elect a new abbot. But personally, I don't believe it. Pontius would never leave us like this, no matter what the trouble we had before!")
		if self.meetings == 1:
			print("Pontius is still the rightful abbot. This election is a sham.")
		if self.meetings > 1:
			print("Pontius did nothing wrong!")
		
	if time.day == 3:
		if self.meetings == 0:
			print("I heard that Pontius might be coming to visit us soon! I'm so excited! Abbot Pontius is the best!")
		if self.meetings == 1:
			print("I wanted to go visit him in Italy, but Peter wouldn't let me.")
		if self.meetings > 1:
			print("Is Pontius back yet?")
			
		
def grumpyMonk(self,time):
	
	if time.day == 1:
		if self.meetings == 0:
			print("Bah! Monks these days! Back when Abbot Hugh was alive, things were so much better! I'm telling you, monasticism is just going downhill from here.")
			
		if self.meetings == 1:
			print("BAH!")
	
	if time.day == 2:
		if self.meetings == 0:
			print("So I hear we're going to elect a new abbot. Bah! Have you heard all this discussion! We should elect this man, we should elect that man. Back in my days, we elected abbots unanimously!")
		if self.meetings >  0:
			print("It doesn't matter who we choose. The candidates are all terrible anyways.")
			
	if time.day == 3:
		if self.meetings == 0:
			print("Bah! Monks these days and their new-fangled ways! Back when Pontius was the abbot, you wouldn't see any of this nonsense.")
		if self.meetings > 0:
			print("Life was better when I was a kid!")
			
		
def yesMonk(self,time):
	
	if time.day == 1:
		print("Abbot Pontius is the best!")
		
	if time.day == 2:
		print("Who should we elect as the next abbot? Everybody is saying different things. I'm so confused!")
		
	if time.day == 3 or time.day == 4: 
		print("Abbot Peter is the best!")
		

def informedMonk(self,time):
	if time.day == 1:
		print("Cluny's finances haven't been doing so good lately. And lately some bishops have been challenging Cluny's authority. Abbot Pontius is doing his best but there's only so much we can do. If things continue like this, some people might begin to grumble....")
	if time.day == 2:
		print("We're holding an election today for our new abbot. But some people are upset because they think Pontius is still the abbot. But the pope told us he abdicated and that we should go ahead with the election.")
		print("1. Ask about election")
		print("2. Ask about Pontius")
		print("3. Goodbye")
		while True:
			question = input("> ")
			print(self.name, "says...")
			if question == "1":
				print("People from Clunaic lands from all across Europe have come to vote on the election. Right now, the main two candidates are Hugh of Marcigny and Peter of Vezelay. We'll hold the election during the chapter meeting.")
				break
			if question == "2":
				print("Pontius went to Rome a while back because some people were upset. Apparantly, while he was there he abdicated and then, refusing to ask the pope's permision, went off to the Holy Land. That's what the pope tells us at any rate.")
				break
			if question == "3":
				print("Goodbye")
				break
			else:
				print("Please enter a number.")
				

		
		
#children 

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
		print("My parents donated me to this monastary when I was little. I wonder what life is like outside the monastary? Do you know?")
	
	


#other monks	
		
def humbleMonk(self,time):
	if self.meetings == 1:
		print("It's important for a monk to be humble.")
	else:
		print("Always remember that you are no greater than a worm.")

	
	
def fashionableMonk(self, time):

	if time.day == 1:
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
				
	if time.day == 2:
		print("Hello brother. I've been speaking with visitors, and after noticing a trend at other houses I now seek to attain a very finely dyed habit in our order's black color, and perhaps with some luxurious trimmings. Maybe I can also find a very nice ring that I may wear. What do you think, brother, would these not be beautiful expressions of our faith?")
		print("yes/no")
		while True:
			answer = input("> ")
			if answer == "yes":
				print("Indeed. The hair shirt I had donned so long ago was part of an older tradition that perhaps has no place in our abbey. Of course, I have no authority to make such rulings. However, the new habit I will soon have will indeed be a display of my devotion to the order, given that it will be a beautiful representation of our order for others to see. Now, I must seek arrangements for acquiring this new habit. God be with you.")
				break
			if answer == "no":
				print("Do you presume to be more wise than our brothers at other abbeys? If others seek to acquire beautiful habits with which to express their faith, so should I. Now, I must get back to making arrangements for acquiring this new habit. God be with you.")
				break
			else: 
				print("Answer either yes or no!")
	
def saintlyMonk(self,time):

	if self.meetings == 0:
		print("I like to read saint's lifes. They're really great. I want to try and be like a saint too! From now on, I'm going to act perfectly saint-like!")
	if self.meetings == 1:
		print("But wait, if I'm talking to you, doesn't that automatically disqualify me from being saint-like?")
	if self.meetings == 2:
		print("You see, saints who are monks never talk. In the life of Saint Odo, our ancient abbot of blessed memory, there is a story about two monks who were captured, but thanks to their diligent silence they were delivered from the snares of the enemy. That's why you won't catching me talking ever, nope, not ever!")
	if self.meetings == 3:
		print("Wait a minute, why am I still talking?")
	if self.meetings > 3: 
		print("Stop talking to me!!!! Aaaaaaaaahhhh!")
	
		


def reprimandMonk(self,time):
	if self.meetings == 0:
		print("You shouldn't be talking. Remember that the tongue is a fire, a world of iniquity.")
	if self.meetings == 1:
		print("....What did I tell you last time?")	
	if self.meetings == 2: 
		print(".....")
	if self.meetings > 2:
		print("Stop talking!")


def travellingMonk(self,time): #needs editing!!!! #not complete!
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
	


#monk who talks about praying for the dead

#sick old monk
	
#cellerar





#infirmary monks

def retiredMonk(self,time):
	if self.meetings == 0: 
		print("My health isn't what it used to be. And my son is off in the Holy Land, so there's no one to look after me. So my wife and I decided to join a monastary.")
	if self.meetings == 1:
		print("My wife is in the abbey of Marcigny, so I never get to see her. But she was always very pious, so I think she must be happy.")
	if self.meetings > 1:
		print("I enjoy my life here. My health isn't very good, but they look after me. And it's a lot less stressful than looking after my estate. Thanks be to God!")
	

def sickMonk(self,time):
	if self.meetings == 0:
		print("I got a really bad fever a while back and had to go to the infirmary. It wasn't fun being sick, but now that I'm better, I kinda don't want to leave!")
	if self.meetings == 1:
		print("Don't tell anybody, but I'm actually almost better. I'm just pretending to still be sick because I don't want to leave!")
	if self.meetings > 1:
		print("*COUGH COUGH* Boy, am I feeling lousy. Guess I should get a double portion of meat tonight!")
	
def insincereMonk(self,time):
	if self.meetings == 0:
		print("Back in my day, I was a really powerful lord. You wouldn't have wanted to mess with me back then, that's for sure! I pillaged and plundered like there was no tomorrow! But I know I'm not going to live much longer. I'm an old man. So I decided to join a monastary. Cluny's a pretty big and important monastary, so I thought it'd be suitable for some one pretty big and important like me.")
	if self.meetings > 0:
		print("I know I'm going to die, so I might as well get buried in holy ground. The monks will pray for my soul.")


















def demonAbbot(self,time):
	print('"Hello there brother! My name is Guido and I am from a far off monastary. I couldn\'t help but notice that this monastary is very different from my own. It\'s a lot more work here. You have to say psalms over and over, and you hardly ever get to do anything fun. Things are more exciting at my monastary. Why don\'t you come with me?"')
	while True:
		action = input("You say....\n> ")
		if action.lower() == "yes":
			print("You agree to leave with him. However, just as you are about to leave, the bell rings for the next activity. Howling the abbot melts into a deformed shape and runs away. Turns out he was a demon!")
			player.increaseSins("giving in to temptation")
			break

		elif action.lower() == "no":
			print("At your words, the abbot howls and leaves. As he runs through the halls, you notice that his shadow is deformed and he has a tail and horns... Good call!")
			break
		else:
			print("I don't understand that! (reply yes or no)")

	

	
def demon(player):
	demons = ["a giant beast, with jowls dripping wet with saliva exposing teeth sharp as swords, with great hairy legs as big as logs.", "a short deformed being, like a human but not quite, with dark skin and a horribly ugly face.", "some kind of giant black bird, hovering above you glaring at you with burning red eyes.", "a dark swarthy being with horns on his head and slitted eyes."]

	rand = randint(0,len(demons)-1)
	
	print("As you are walking through the halls of an abbey, suddenly you see a demon appearing in front of you! It looks like", demons[rand])
	
	print("What do you do?")
	print("1. Pray to God")
	print("2. Sprinkle holy water")
	if len(player.sinsList) != 0:
		print("3. Confess your sins")
	
	while True:
		action = input("> ")
		if action == "1":
			print("You say some of the psalms out loud, and at the name of God, the demon flees! Truly is God's power mighty!")
			break
		if action == "2":
			print("You run and find some holy water and sprinkle it over the demon.")
			if len(player.sinsList) == 0:
				print("Howling in pain, the demon flees. Praise be to God!")
				break
			else:
				print("But it doesn't work! This kind of demon is too powerful! You need to confess your sins.")
		if action == "3":
			if len(player.sinsList) != 0:
				print("You confess about the time you sinned by:", player.sinsList[0])
				players.sinsList.remove(players.sinsList[0])
				print("There is a blinding light and the demon howls and disappears.")
			else:
				print("That's not an option!")
	
	
	
