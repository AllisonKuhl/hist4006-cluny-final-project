from random import randint

#Time variables
DAYS_IN_YEAR = 12  #how many days in a year??

LENGTH_LENT = 2  #how long is lent?
LENT_MIN_START = 2 #earliest time for lent to start
LENT_MAX_START = 4 #latest time for lent to start
LENT_START = randint(LENT_MIN_START,LENT_MAX_START) #will pick a day for lent to start within those two intervals
AUTUMN_STARTS = 9  #what day does winter start?
CHRISTMAS = 11   #when is Christmas?

#the current seasons. 
#this is a dictionary that maps each season to when it begins
#you can add more if you like.
SEASONS = {0:'winter', LENT_START: 'lent', LENT_START+LENGTH_LENT:'easter', LENT_START+LENGTH_LENT+1:'summer', AUTUMN_STARTS:'autumn', CHRISTMAS: 'christmas'}

TURN_OFF_PROMPTS = 5


class Time:

	'''
	Time like an ever-rolling stream
	Soon bears us all away
	We fly forgotten as a dream
	Dies at the opening day
	'''

	def __init__(self):
		self.__year = 1111
		self.__currentSeason = "winter"
		self.__totalDays = 1
		self.__daysOfYear = 0

    #getters
	def getTotalDays(self):
		return self.__totalDays
		
	def getYear(self):
		return self.__year
	
	def getSeason(self):
		return self.__currentSeason
	
	def getDaysOfYear(self):
		return self.__daysOfYear
		
		
	#setters

	def setYear(self,year):
		self.__year = year
	
	def setSeason(self, season):
		self.__currentSeason = season
		
	def setTotalDays(self, days):
		self.__currentSeason = days
		
	def setDaysOfYear(self, day):
		self.__daysOfYear = day
		

	
	#other methods	
		
	def newYear(self, playerObj):
		#resets the time when a new year begins
		self.__daysOfYear = 0
		self.__year += 1
		self.__currentSeason = 'winter'
		
		#sets lent to begin at a random time
		LENT_START = randint(LENT_MIN_START,LENT_MAX_START) 
		playerObj.setAge(1) #increases your age.
		
	def dayEnd(self, playerObj):
		self.__totalDays += 1
		self.__daysOfYear += 1
		
		#changes the season
		if self.__daysOfYear in SEASONS:
			self.__currentSeason = SEASONS[self.__daysOfYear]
		
		#changes the year
		if self.__daysOfYear == DAYS_IN_YEAR:
			self.newYear(playerObj)
			
		if self.__totalDays > 5:
			playerObj.prompt = False
			
	def printDate(self):
		print("The year is", self.__year, "and it is", self.__currentSeason + ".")
		#print("We are at day", self.__daysOfYear)
		
		
