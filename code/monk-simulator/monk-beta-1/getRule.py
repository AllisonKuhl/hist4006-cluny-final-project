def getLunchReading():  #function that returns a reading from the rule of Saint Benedict. You must have a text file of all the rule in the same directory for it to work however.

	rule = []

	ruletxt = open('rule.txt', 'r', encoding="utf8")
	

	for line in ruletxt:
		try:
			print(line)
			rule.append(line)
			
		except:
			continue

	ruletxt.close()


	return rule
	
def fixRule():

	rule = getLunchReading()

	newRules = open('rule2.txt', 'w')

	for thing in rule:
		if "CHAPTER" not in thing:
			newRules.write(thing)

	newRules.close()
	
	
	
def getRule():

	ruletxt = open('rule2.txt', 'r')
	
	rule = []

	for line in ruletxt:
			rule.append(line)

	ruletxt.close()


	return rule
