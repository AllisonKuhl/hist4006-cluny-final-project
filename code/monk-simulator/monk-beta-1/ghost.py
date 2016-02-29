from random import randint

names = ["Adelmus", "Ethelbert", "Drogo", "Einhard", "Bernard le Gros", "Rudolphus", "Shulk"]

backstory = ["I was once a powerful lord.  My power was such that I did whatever was right in my own eyes and stole from the innocent and ravaged the helpless. Alas, too late did I realize my great sins. At the end of my life I put on the habit and become a monk at this very monastary, and because of this I was spared the eternal torment. However, due to my great sins I have not been able to enter paradise.",

"I used to be a brave and powerful warrior, until I took an arrow to the knee. After this injury I retired to this monastary, where I lived out the rest of my life. As a knight, I slaughtered and robbed many people. One deed was particularly notorious. But out of shame, I kept this terrible deed secret from my brothers and did not confess my sins. Because I did not confess my sin, I was unable to enter heaven, even though I had lived many years as an eager and pious monk.", 

"Dear friend, I was once a monk just like you. But I was lazy and irresolute  monk, and have recieved punishment for my sins. I was the first to go to bed in the evening and the last to wake up in the morning, often sleeping through matins altogether. Although perfectly healthy, I would hobble about like an old man in order to admitted to the infirmary, just so I could eat some extra meat. I disobeyed my superiors and arrogantly followed my own will. For all these things I surely deserve the worst and eternal punishment, but for the sake of the prestige of this most illustrious order, Christ has had mercy upon me and spared me from that land of weeping and gnashing of teeth. Now I wander in torment, waiting for the prayers of the faithful to release me from my suffering."

]


class Ghost: 
	def __init__(self):
		self.name = names[randint(0,len(names)-1)]
		self.backstory = backstory[randint(0,len(backstory)-1)]
		self.inHeaven = False
		self.massesSaid = 0
		self.appearances = 0
		
	def increaseAppearances(self, appearances):
		self.appearances += 1
		
	def display_message(self):
		if self.appearances == 0:
			print("Greetings mortal! My name is " + self.name + ". Let me tell you my sad sad tale.")
			print(self.backstory)
			print("I beg you to have mercy upon me a sinner, and tell the monks of Cluny to pray for my soul. Only through your diligent prayers will I be able to be saved.")
			
		elif self.appearances >= 1 and self.massesSaid >= 1:
			print("It is I, " + self.name + ". I have returned to thank your prayers. Thanks to you and the brothers diligently praying for my soul, I was finally able to leave behind my torment and enter the eternal bliss.")
			self.inHeaven = True
		
		elif self.appearances >= 3:
			print("It is I, " + self.name + ". I have returned to thank your prayers. Thanks to you and the brothers diligently praying for my soul, I was finally able to leave behind my torment and enter the eternal bliss.")
			self.inHeaven = True
			
		else:
			print("It is I, "+ self.name + ". Your prayers have had much affect on me, but my sins are still great. I beg for you to continue, knowing that they are not going to waste, but indeed are of the utmost merit.")
		
		#if name == "Shulk":
			#print("I'm really feeling it!")
			
		self.appearances += 1

	
