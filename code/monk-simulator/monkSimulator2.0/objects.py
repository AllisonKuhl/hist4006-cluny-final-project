from random import randint


class Object():
	def __init__(self, name, init, description, action):
		self.name = name
		self.init = init
		self.description = description
		self.action = action
	
	def use(self,player, time):
		self.action(player, time)


		
def eat(player, time):
	print("You look around furtively to see if anyone is watching, then you grab some food.")
	print("MMMMMmm! Delicious!")
	player.increaseSins("gluttony")
	player.increaseSins("lust")

def drink(player, time):
	print("You look around furtively to see if anyone is watching, then you pour yourself a cup of wine.")
	print("MMMMMmm! Delicious!")
	player.increaseSins("gluttony")
	player.increaseSins("lust")

def pray(player,time):
	print("You kneel in front of the altar and pray.")
	player.increaseHoliness()
	
	
def sleep(player, time):
	activity = time.getCurrentActivityClass()
	if activity.name == "sleep":
		activity.do(player, time)
	else:
		print("You lie down on the bed and soon fall asleep. Zzzzzzzz..... Uh-oh! You've missed going to", activity.name)
		time.resetTurn()
		player.increaseSins("laziness")
		player.increaseSins("skipping")


def read(player, time):

	saints = ["St. Maiolus, one of the great abbots of this monastary.", "St. Odo, who was one of the first abbots of Cluny and brought the monastary to greatness.", "St. Martin of Tours.", "St. Gerald of Aurrilac, a nobleman who was so noble he almost lived like a monk. It was written by St. Odo of Cluny."]
	
	print("What would you like to read?")
	print("1. The Bible")
	print("2. Roman Classics")
	print("3. Saint's Lives")


	while True:			
		response = input("> ").lower()
		if response == "the bible" or response == "1" or response == "bible":
			print("Good idea! You meditate on the profound words of scripture.")
			player.increaseHoliness()
			break
		elif response == "roman classics" or response == "2":
			print("Scandalous!")
			player.increaseSins("pagan literature")
			break
		elif response == "saint's lives" or response == "3":
			print("Good idea! You read about", saints[randint(0,len(saints)-1)])
			player.increaseHoliness()
			break
		else:
			print("I don't understand that!")
			
			
			
food = Object("food", "eat food", "There is food here.", eat)

wine = Object("wine", "drink wine", "There is wine here.", drink)

altar = Object("altar", "pray", "There is a altar by which you could pray.", pray)

books = Object("book", "read book", "The library is filled with interesting books you could read", read)

bed = Object("bed", "lie down", "There are beds you can lie down in.", sleep)

