from random import randint #allows random variables

#this is essentially your 'field' where you grow stuff. 0 means the plot is empty.
plots = [0,0,0,0]


#cookie cutter model for each plant we will grow
class Plant:
	#each plant has a type, a time for it to finish growing and a total harvest. We begin it's growth at 0.
	def __init__(self, type, timeToGrow, totalHarvest):
		self.__type = type
		self.__timeToGrow = timeToGrow
		self.__totalHarvest = totalHarvest
		self.__growth = 0
	
	#method that controls the growing of the plant
	def grow(self, weather, drought, rain):
	
		#if there is too much sun or rain it will stunt growth and not produce as much.
		if drought > 3 or rain > 3:
			self.__totalHarvest -= 5
			
		#if it is sunny, then it will grow 
		elif weather == "sunny" and drought < 3 and rain < 3:
			self.__growth += 2	
			
		#if cloudy it will also grow... but not as much
		elif weather == "cloudy" and drought < 3 and rain <3:
			self.__growth +=1
		
		#if there is a storm, the crops will be damaged and it won't produce as much.
		elif weather == "violent storm":
			self.__totalHarvest -= 10
	
	def check_if_grown(self):
		if self.__timeToGrow == self.__growth:
			return True
		else:
			return False
	
	#getter method for type
	def get_type(self):
		return self.__type
		
	#getter method for harvest
	def get_total_harvest(self):
		return self.__totalHarvest
		
	#setter method for total harvest. Provides way to decrease total harvest from outside the class.
	def decrease_total_harvest(self, damage):
		self.__totalHarvest -= damage
		if self.__totalHarvest < 0:  #prevents you from reaping negative values
			self.__totalHarvest = 0  
		
	def get_growth(self):
		return self.__growth
	
	
#after defining what a plant is more generally, we create specific types of plants
	
class Wheat(Plant):
	def __init__(self):
		#Wheat takes 5 weeks to grow and produces 30 units - pounds maybe?? or bushels?
		Plant.__init__(self, "Wheat", 6, 30)
		
class Bean(Plant):
	def __init__(self):
		#Beans take 5 weeks to grow and produces 15 units
		Plant.__init__(self, "Bean", 4, 15)

class Turnip(Plant):
	def __init__(self):
		#turnips take 3 weeks to grow and produces 8 units
		Plant.__init__(self, "Turnip", 3, 8)

		
#here is our main function where most of the things happen		
def main():

	#declaring some variables that will be used later
	week = 1
	previous_weather = "no rain"
	winter = False
	total_harvest = 0
	drought = 0
	rain = 0
	damage = False


	print("Welcome to Peasant Simulator.")
	
	next = input("It is time to plow your land. Press enter to plow your land. ")
	print("Your land has been ploughed.")
	
	print("One week has passed.")
	print("")
	
	print("It is time to plant your seeds. You have a small piece of land which can be divided into", len(plots), "segments. What would you like to plant in each segment?")
	
	plant_a_plant(plots) #calls the plant function which is further down. This function lets you choice what plant you would like to plant in each spot.
	

	while(winter == False): #as long as it is not winter, the following will repeat. 
		print("")
		print("")
		print("Week", week) #displays the week number.
		print("")
		
		weather = decide_weather() #get a randomized weather from a function later on.
		print("The weather today is:", weather +'.')
		
		#this controls the random events.
		#1/2 chance everything is normal
		#1/4 chance knights pillage your land
		#1/4 chance your lord makes you work for him
		num = randint(1,8)
			
		if num <= 4:
			print("The week passes unevenfully.")
			weather_message(weather, rain, drought, damage)
			plant_a_plant(plots)
			damage = False
			work = False
		elif num <= 7:
			print("Some knights pass by and pillage your lands!")
			damage = True
			weather_message(weather,rain,drought, damage)
			plant_a_plant(plots)
			work = False
		elif num <= 8:
			print("Your local lord commands you to go work for him the rest of the week.")
			damage = False
			work = True
		
		#keeps track of how many days with or without rain
		if weather == "sunny" or weather == "cloudy":
			if previous_weather == "no rain": #if it didn't rain the day before, the drought increases
				drought += 1
			else:
				rain = 0
			previous_weather = "no rain" #resets previous weather
		if weather == "rainy" or weather == "violent storm":
			if previous_weather == "raining":
				rain += 1
			else:
				drought = 0
			previous_weather = "rain"
				
		
		
			for i in range(len(plots)):  #goes through each element in your field
			
					
				if plots[i] != 0:  #checks to see if a plant is there.
					#if there is...
					i.grow(weather, drought, rain) #we call the "grow function" that makes it grow
					growth = i.get_growth() #use getter function because growth is a private variable
					if damage == True: #from above... this is when knights attack your field
						i.decrease_total_harvest(5) #it decreases your total harvest.
					
					
				
				#checks to make sure your plants still exist. If it doesn't, then we reset the plot.
				if i.get_total_harvest() == 0:
					print("Uh-oh! Looks like your", i.get_type(), "was destroyed!")
					plot[i] = 0
				
				
				#checks if it's finished growing, and if it is you can harvest it.
				if work == False: #can't harvest if you are working on lord's land
					if plots[i].check_if_grown() == True:
						name = plots[i].get_type()
						print("Your ", name, "is ready to harvest.")
						next = input("Press enter to harvest.")
						harvest = int(plots[i].get_total_harvest())
						total_harvest = harvest + total_harvest #adds harvest from plant to running total
						print("You got", harvest, name +"s!")
						plots[i] = 0  #resets plot
					
			
		week += 1  #increases the number of weeks before the loop begins again.
		
		next = input("Press enter to continue. ")
		
		#after 8 weeks, there is a 50/50 chance of winter arriving. You don't know when it will come though.
		if week > 8 and randint(0,1) == 1:
			winter = True
			
	#loop ends
	print("")
	print("Winter has come! You can't grow anything anymore!")
	if total_harvest > 10:
		print("You managed to harvest", total_harvest, "food for the winter! You are able to survive!")
	elif total_harvest < 0:
		print("Due to various unfortunate events, your crops were either destroyed or unable to grow. Your entire family starves.")
		print(":(")
	else:
		print("You managed to harvest", total_harvest, "food! Unfortunately that's not enough to survive the winter. You and your entire family starve.")
	
	
	exit = input("Press enter to exit the program.")

	
	
#various functions that are used above.
	
def plant_a_plant(plots):
	for i in range(0,len(plots)):
		if plots[i] == 0:
			print("")
			print("Segment", i+1, "of your field is empty.")
			print("What plant would you like to plant in it?")
			print("1: Wheat")
			print("2: Beans")
			print("3: Turnips")
			print("4: Nothing")
			
			while True:
				plant_choice = input("Please enter the corresponding number of the product you'd like to plant. ")
				
				if plant_choice == "1":
					print("\nYou plant some wheat.")
					plots[i] = Wheat()
					break
				elif plant_choice == "2":
					print("\nYou plant some beans.")
					plots[i] = Bean()
					break
				elif plant_choice == "3":
					print("\nYou plant some turnips.")
					plots[i] = Turnip()
					break
				elif plant_choice == "4":
					print("You decide not to plant anything after all.")
					break
				else:
					print("I don't understand that!")
				print("")

				
				
def decide_weather():
	num = randint(1,9)
	if num <= 3:
		weather = "sunny"
	elif num <= 6:
		weather = "rainy"
	elif num <= 7:
		weather = "violent storm"
	elif num <= 9:
		weather = "cloudy"
	return weather


def weather_message(weather, rain, drought, damage):
	#controls what message will print out depending on weather
	if weather == "sunny" and drought >= 3:
		print("Your plants aren't looking so good... Hopefully it will rain soon.")
	elif weather == "sunny" and damage == False:
		print("Your plants are growing nicely.")
		
	if weather == "rainy" and rain >= 3:
		print("Your plants aren't looking so good. They look like they're drowning in the rain!")
	elif weather == "rainy" and damage == False:
		print("Your plants look pretty happy.")
		
	if weather == "violent storm":
		print("Uh oh! The storm has damaged your crops!")


#this didn't work for some reason....		
'''	
def harvest(plots, total_harvest):
	for i in range(len(plots)):
		if plots[i].check_if_grown() == True:
			name = plots[i].get_type()
			print("Your ", name, "is ready to harvest.")
			next = input("Press enter to harvest.")
			harvest = int(plots[i].get_total_harvest())
			print(harvest)
			total_harvest = harvest + total_harvest #adds harvest from plant to running total
			print("You got", harvest, name +"s!")
			plots[i] = 0  #resets plot
			return total_harvest
'''
			
			
			


	
main()	
	
	

	
		