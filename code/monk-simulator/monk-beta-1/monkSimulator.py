import player
import chronology
import activities
#from save_load import save  COMING SOON!!!

'''
TO-DO

- add interaction for demon random event
- cleaner code
- fine-tune dates and schedule
- add more interactivity for free-time function
- update dinner activity
- add feast days and seasonal liturgy
- Add more ways to decrease penance (like if you do prayers all correctly?)
- option to save or load game
- lots more stuff probably
- romance events
- special jobs

'''

#COMING SOON!!!

# Loading and saving ability! 


				
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



#DAY_ACTIVITIES = [getDressed, nocturnes, freeTime, matins, sleep, prime, freeTime, terce, chapterMeeting, freeTime, sext, nones, dinner, sleep, freeTime, vespers, compline, sleep]
DAY_ACTIVITIES = [sleep] #for testing



def main():

	
	time = chronology.Time()
	
	name = input("What is your name? \n> ")
	you = player.Player(name)

	print("Welcome", name + "! You are now a monk.")
	
	while you.alive == True:

		time.printDate()
		
		print(time.getTotalDays())
		
		print("A new day begins! Early in the morning, before even the light of day has broken over the fertile plains of Burgundy, the monks of Cluny rise from their slumber to begin their daily rounds of prayer.")

		if you.isSick() == False:	
			normal_day(you)
		else:
			sick_day(you)
		
		#print("day over")
			
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
				player.decreaseHealth(-1)
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

main()
