
#This is just an experiment, it's not finished yet! 


class Player:
	def __init__(self):
		self.sins = 0
		self.holiness = 0
		self.sleeping = True

wake_up_words = ['wake up', 'get up', 'get out of bed']
sleep_words = ['keep sleeping', "don't get up", "sleep", "sleep longer", "don't wake up", "sleep a little longer"]
talk_words = ['talk to monks', 'chat with monks', 'ask monks a question', 'talk', 'speak with monks', 'speak with monk']
go_to_prayer_words = ["go to church", "go to prayer", "head toward church", 'leave']
dont_prayer_words = ["don't go to prayer", "dont go to prayer", 'skip prayer', "don't go to church"]
good_things = ['pray', 'think about god', 'sing psalms', 'read bible', 'read scripture', 'contemplate god', 'think holy thoughts', 'think about how sinful you are', 'contemplate', 'contemplate scripture', 'read']
bad_things = ['talk', 'sleep', 'swear', 'waste time', 'do nothing', 'leave abbey']
rule_of_benedict = ["The first degree of humility is obedience without delay. This is the virtue of those who hold nothing dearer to them than Christ; who, because of the holy service they have professed, and the fear of hell, and the glory of life everlasting, as soon as anything has been ordered by the Superior, receive it as a divine command and cannot suffer any delay in executing it.", "This vice especially is to be cut out of the monastery by the roots. Let no one presume to give or receive anything without the Abbot's leave, or to have anything as his own-- anything whatever, whether book or tablets or pen or whatever it may be-- since they are not permitted to have even their bodies or wills at their own disposal; but for all their necessities let them look to the Father of the monastery.", "Our prayer, therefore, ought to be short and pure, unless it happens to be prolonged by an inspiration of divine grace. In community, however, let prayer be very short, and when the Superior gives the signal let all rise together."]

bell = chr(7)  #ascii code seven is for the bell sound on your computer lol

player = Player()

def main():
	print("The bell rings.")
	print("DONG!", bell)
	print("It is time to wake up!")
	
	
	while True:
		
		action = (input("\n> ")).lower()

		if action in wake_up_words:
			print("You wake up.")
			break
		elif action in sleep_words:
			print("You sleep a little longer.")
			decrease_sin(1)
		else:
			print("I don't understand that. You should probably wake up.")
	
	
	print("You are in the dormitory. Around you, your fellow monks are waking up and getting ready for prayer.")
	

	while True:
	
		action = (input("\n> ")).lower()
	
	
		if action in go_to_prayer_words:
			print("You head to the church for morning prayer.")
			break
		elif action in talk_words:
			print("You turn to the monk next to you and say....")
			print("1. Nice weather we're having, eh?")
			print("2. Do you have any idea what I'm supposed to be doing right now?")
			print("3. What do you call a monk who has an itchy robe and keeps complaining about it?")
			

			choice = input("(type the number)\n > ")
			if choice == '1':
				print("The monk stares at you and gestures for you to be quiet.")
				decrease_sin(1)
			elif choice == '2':
				print("The monk stares at you and gestures for you to be quiet.")
				decrease_sin(1)
				print("The monk points toward the door. You're guessing you're supposed to go to the church.")
			elif choice == '3':
				print("The monk stares at you silently.")
				print("You say: 'He has a bad habit!'")
				print("'Eh? Eh? Geddit? A BAD HABIT??? You picking up what I'm laying down here?'")
				print(".....")
				decrease_sin(10)
			else:
				print("The monk stares at you in confusion. Apparantly he doesn't understand. Should have typed in one of the numbers.")
				decrease_sin(1)
				
		else:
			print("I don't understand that. What do you want to do?")
				
	print("It's free time. What should you do?")
	
	action = (input("\n> ")).lower()
	
	if action in good_things:
		print("You decide to", action + ". Wow! You're a pretty good monk!")
		player.holiness += 1
		print("Holiness + 1")
	elif action in bad_things:
		print("What are you doing that for?")
		decrease_sin(1)
	else:
		print("You spend your free time doing", action)
	
	print("The bell rings again.")
	print(bell)
	print("Time for prayer!")

	
	while True:
		action = (input("\n> ")).lower()
		if action in go_to_prayer_words:
			print("You go to prayer.")
			break
		elif action in dont_prayer_words:
			print("You don't go prayer! Gasp! You rebel!")
			decrease_sin(5)
			break
		else: 
			print("I don't understand that. Should you go to prayer or not?")
	
	print("It's lunch time!")
	print(bell)
	print("You go to lunch. Someone is reading something at the front of the room. There is a piece of bread in front of you. What do you do?")
	
	for i in range(0,2):
		action = (input("\n> ")).lower()
		if action == "listen" or action == "listen to reading":
			print(rule_of_benedict[i])
		elif action == "eat" or action == "eat food" or action == "eat bread":
			print("You eat your food. The voice of the reader drones on.")
		else:
			print("You can't do that now. It's time to eat.")
	
	print("Meal time is over. You notice that there are still some crumbs on your table. What should you do?")
	print("1: Eat them.")
	print("2: Leave them")
	
	while True:
		choice = input("\n> ")
		if choice == '1':
			print("Good decision!")
			break
		elif choice == "2":
			print("Bad decision!")
			decrease_sin(1)
			break
		else:
			print("I don't understand that!")
			
	print("The bell rings again.")
	print(bell)
	print("Time for prayer!")

	
	while True:
		action = (input("\n> ")).lower()
		if action in go_to_prayer_words:
			print("You go to prayer.")
			break
		elif action in dont_prayer_words:
			print("You don't go prayer! Gasp! You rebel!")
			decrease_sin(5)
			break
		else: 
			print("I don't understand that. Should you go to prayer or not?")
			
		
	print("It is time for bed.")
	print("Congratulations. You have completed your first day as a monk.")
	print("You have " + player.sins + " sins!")



			
def decrease_sin(amount):
	player.sins += amount;
	print("Sins + ", amount)
	

main()
