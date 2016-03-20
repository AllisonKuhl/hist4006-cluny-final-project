import player
import chronology
import activities
from random import randint

'''
TO-DO

- more romance
- more contemporary events

'''


				
#which psalm is said during which hour. 
PSALMS_SAID = {'nocturnes': 121, 'matins': 31, 'prime': 6, 'terce': 56, 'sext': 101, 'nones': 129, 'vespers': 142, 'compline': 69}

		

		
you = player.Player("Hugh")


sleep = activities.Sleep()
freeTime = activities.FreeTime()
chapterMeeting = activities.ChapterMeeting()
dinner = activities.Dinner()
getDressed = activities.GetDressed()


nocturnes = activities.Prayer("nocturnes", PSALMS_SAID["nocturnes"])
matins = activities.Prayer("matins", PSALMS_SAID["matins"])
prime = activities.Prayer("prime", PSALMS_SAID["prime"])
terce = activities.Prayer("terce", PSALMS_SAID["terce"])
sext = activities.Prayer("sext", PSALMS_SAID["sext"])
nones = activities.Prayer("nones", PSALMS_SAID['nones'])
vespers = activities.Prayer("vespers", PSALMS_SAID['vespers'])
compline = activities.Prayer("compline", PSALMS_SAID['compline'])



DAY_ACTIVITIES = [getDressed, nocturnes, freeTime, matins, sleep, prime, freeTime, terce, chapterMeeting, freeTime, sext, nones, dinner, sleep, freeTime, vespers, compline, sleep]
#DAY_ACTIVITIES = [dinner, compline, chapterMeeting] #for testing



def main():

	
	time = chronology.Time()
	
	name = input("What is your name? \n> ")
	you = player.Player(name)

	print("Welcome", name + "! You are now a monk.")

	
	while you.alive == True:

		time.printDate()
		
		print(time.getTotalDays())
		
		if you.journey == False:
			print("A new day begins! Early in the morning, before even the light of day has broken over the fertile plains of Burgundy, the monks of Cluny rise from their slumber to begin their daily rounds of prayer.")

			if you.journey == True:
				journey(you)
			
			if you.isSick() == False:	
				normal_day(you)
			else:
				sick_day(you)
			#print("day over")
		else:
			journey(you)
		
		
		time.dayEnd(you)
		
		
	end = input("You are dead. Thanks for playing.")
	

	
def sick_day(player):
	
	turns = 0
	
	validActions = ['rest','sleep','relax']
	
	
	while player.getSickliness() > 0:
		print("You are in the infirmirary. You are still feeling a bit sick. You should rest.")
	
		while True:
			action = input("> ")
			
			if action in validActions:
				print("You close your eyes and rest. You can feel yourself getting healthier already.")
				player.decreaseHealth(-3)
				break
			else:
				print("Now's not the time for that! You need to rest!")
				
		print("You wake up feeling refreshed. Someone brings you some food to eat. Wow, it's meat! Should you eat it?")
		
		while True:
			action = input("> ")
			if action == 'yes':
				print("You eat the meat. Delicious! You feel healthier already.")
				player.decreaseHealth(-1)
				break
			elif action == 'no':
				print("You don't eat the meat. That's very holy of you.")
				player.decreasePenance(1)
				break
			else:
				print("Answer either yes or no!")
				
		print("You sleep for the rest of the day.")

	player.changeHealth(False)
	print("You are feeling a lot better! Tomorrow you can leave the infirmary and resume the regular hours.")
	
def normal_day(player):


	for i in range(0,len(DAY_ACTIVITIES)):
		
		activity = DAY_ACTIVITIES[i]
		
		#gets index for previous activity
		if i == 0:
			previous = len(DAY_ACTIVITIES)-1 #loop around
		else:
			previous = i-1
					
		if DAY_ACTIVITIES[previous].skip == False and player.isSick() == False:
			activity.go_to(player)
			if activity.skip == False:
				activity.random_events(player)
				if player.isSick() == False:
					activity.do_action(player)
			else:
				activity.skip = True

def journey(player):
	
	next = input("Press enter to continue on your journey.")
	print("You continue on your journey.")
	
	if player.journeyDays < 1:
		print("You are travelling across Burgandy. It's pretty scenic.")
		
	if player.journeyDays == 1:
		print("You are walking across the alps. It's a little bit rocky.")
		
	if player.journeyDays == 2:
		print("You are in Italy.")
		
	if player.journeyDays == 3:
		print("You arrive in Rome and deliver the message to the Pope.")
		print("After staying for a while in Rome, you decide it's time to go back.")
		
		
	rand = randint(0,100)
	
	if rand < 10:
		print("Oh no! You've been captured by brigands! What do you do?")
		print("1: Fight them.")
		print("2: Pray")
		
		while True:
			action = input("> ").lower()
			
			if action == "fight them" or action == "1":
				print("You fight against the bandits, but all they do is beat you up more. They leave you on the side of the road, nearly dead.")
				player.changeHealth(3)
				break
				
			elif action == "pray" or action == "2":
				print("You don't fight back against the bandits, and instead remain silent and pray to God. Miraculously, when the bandits try to attack you, they are repelled by a mysterious force. They are so in awe that they all decide to become monks. They let you go unharmed.")
				player.decreasePenance(2)
				break
			else: 
				print("I don't understand that!")
				
	elif rand < 20:
		print("You stop at a monastary on the road. They offer you some delicious looking chicken for dinner. Should you eat it?")
		
		while True:
			action = input("> ").lower()
			
			if action == "yes":
				print("You eat the meat.")
				player.increaseSins("laxity")
				break
			elif action == "no":
				print("You don't eat the meat! Good call!")
				player.decreasePenance(1)
				break
			else: 
				print("Please answer either yes or no!")
				
	elif rand < 30:
		print("You stop in an inn on the way to rest. While there, you notice a beautiful women looking at you. She approaches you.")
		print('"Hey there, handsome," she says, "Wanna have a good time?" She waggles her eyebrows at you.')
		print("You....")
		print("1. Have a good time.")
		print("2. Don't have a good time.")
		
		while True:
			action = input("> ").lower()
			
			if action == "1" or action == "have a good time":
				print("You have a good time.")
				player.increaseSins("kissing")
				break
			if action == "2" or action == "don't have a good time":
				print('"Get behind me Satan!", you cry. The woman looks insulted and walks away. Phew. You narrowly got out of that one.')
				break
			else:
				print("I don't understand that.")
		
	if player.journeyDays == 7:
		print("After a long and arduous trek, finally the great walls of Cluny come into sight once more! You did it!")
		player.journey = False
	
	player.journeyDays += 1
	
main()
