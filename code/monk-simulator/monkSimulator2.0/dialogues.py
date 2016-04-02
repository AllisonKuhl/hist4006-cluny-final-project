

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
				
			
	
	
	
	
	
	
	
	
	
	
