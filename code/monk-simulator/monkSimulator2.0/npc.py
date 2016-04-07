class Player():

	def __init__(self,name, function):
		self.name = name
		self.meetings = 0
		self.specialConvo = function
		
	def talkTo(self,time, room):
		print(self.name, "says:")
		self.specialConvo(self,time)
		next = input("")
		self.meetings += 1
	
	def addConversation(self,convo):
		self.specialConvo = convo

	
class John(Player):
	
	def __init__(self):
		Player.__init__(self,"John",None)
		
	def talkTo(self,time, room):
		print("John says: ")
		if time.day == 1:
			self.first_day(time,room)
			
			
	def first_day(self,time, room):
		
		activity = time.getCurrentActivityName()
		
		if room.activity != time.getCurrentActivityType():
			print("It's time for", time.getCurrentActivityName(), "now, so you should probably get going!")
			if activity == "nocturnes":
				print("1. Ask for directions")
				print("2. Get going")
				
				action = input("> ").lower()
				if action == "1" or action == "ask for directions":
					print("John says: ")
					print("Don't worry, it's really easy. All you have to do is go west until you reach the galilee of the church. Then you just go north.")
				
				print("You say goodbye to John.")
			
			if activity == "free time":
				print("We have free time right now. There's nowhere in particular you have to be. Usually it's good to read or pray on your own, or do some other useful task, but since you're new here, why don't you take a look around the monastary? I'm sure you'll find many interesting things.")
		else:
			print("You made it! Good work!")
			if activity == "nocturnes":
				print("We're about to celebrate Nocturnes. Nocturnes celebrates the night or something like that I dunno I'll add more info later.")
			
			
			
class demonAbbot():

	def __init__(self, player):
		Player.__init__(self,"Wido",None)
		self.player = player
	
	def talkTo(self, time, room):
		print("Wido says....")
		print('"Hello there brother! My name is Guido and I am from a far off monastary. I couldn\'t help but notice that this monastary is very different from my own. It\'s a lot more work here. You have to say psalms over and over, and you hardly ever get to do anything fun. Things are more exciting at my monastary. Why don\'t you come with me?"')
		while True:
			action = input("You say....\n> ")
			if action.lower() == "yes":
				print("You agree to leave with him. However, just as you are about to leave, the bell rings for the next activity. Howling the abbot melts into a deformed shape and runs away. Turns out he was a demon!")
				self.player.increaseSins("giving in to temptation")
				break

			elif action.lower() == "no":
				print("At your words, the abbot howls and leaves. As he runs through the halls, you notice that his shadow is deformed and he has a tail and horns... Good call!")
				break
			else:
				print("I don't understand that! (reply yes or no)")
		
	
	
			
			
