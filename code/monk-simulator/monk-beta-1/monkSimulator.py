import player
import time
import activities

'''
TO-DO

- Random events
- cleaner code
- more liturgy (store each in object?)
- fine-tune dates
- add feast days and seasonal liturgy
- Add ways to decrease penance (like if you do prayers all correctly?)
- option to save or load game
- lots more stuff probably

'''



				
#which psalm is said during which hour. 
PSALMS_SAID = {'nocturnes': 121, 'matins': 31, 'prime': 6, 'terce': 56, 'sext': 101, 'nones': 129, 'vespers': 142, 'compline': 69}

		

		
#you = Player("Hugh")


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

#time = time.Time()

name = input("What is your name? \n> ")
you = player.Player(name)

print("Welcome", name + "! You are now a monk.")


sleep.random_events(you)


while you.alive == True:

	#time.printDate()
	
	print("A new day begins! Early in the morning, before even the light of day has broken over the fertile plains of Burgundy, the monks of Cluny rise from their slumber to begin their daily rounds of prayer.")

	for i in range(0,len(DAY_ACTIVITIES)):
		
		activity = DAY_ACTIVITIES[i]
		
		#gets index for previous activity
		if i == 0:
			previous = len(DAY_ACTIVITIES)-1 #loop around
		else:
			previous = i-1
		
		if DAY_ACTIVITIES[previous].skip == False:
			activity.go_to(you)
			if activity.skip == False:
				activity.random_events(you)
				activity.do_action(you)
			else:
				activity.skip = True
		
	#time.dayEnd(you)
	
end = input("You are dead. Thanks for playing.")


	
