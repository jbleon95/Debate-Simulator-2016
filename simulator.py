from pymarkovchain import MarkovChain
import questions
import random

"""
trump_file = open("transcripts/trump.txt", "r")
cruz_file = open("transcripts/cruz.txt", "r")
rubio_file = open("transcripts/rubio.txt", "r")
kasich_file = open("transcripts/kasich.txt", "r")
carson_file = open("transcripts/carson.txt", "r")
jeb_file = open("transcripts/jeb.txt", "r")
christie_file = open("transcripts/christie.txt", "r")

trumpText = trump_file.read()
cruzText = cruz_file.read()
rubioText = rubio_file.read()
kasichText = kasich_file.read()
carsonText = carson_file.read()
jebText = jeb_file.read()
chrisiteText = christie_file.read()

mcTrump.generateDatabase(trumpText)
mcCruz.generateDatabase(cruzText)
mcRubio.generateDatabase(rubioText)
mcKasich.generateDatabase(kasichText)
mcCarson.generateDatabase(carsonText)
mcJeb.generateDatabase(jebText)
mcChristie.generateDatabase(chrisiteText)

mcTrump.dumpdb()
mcCruz.dumpdb()
mcRubio.dumpdb()
mcKasich.dumpdb()
mcCarson.dumpdb()
mcJeb.dumpdb()
mcChristie.dumpdb()
"""

def modQuestion(candidate, num):
	return "MODERATOR: " + formalCandidates[candidateNum] + questions.questions[num][0]  + "\n"

def response(candidate, questionNum = None):
	stringList = []
	if candidate == 0:
		mc = mcTrump
	elif candidate == 1:
		mc = mcCruz
	elif candidate == 2:
		mc = mcRubio
	elif candidate == 3:
		mc = mcKasich
	elif candidate == 4:
		mc = mcCarson
	elif candidate == 5:
		mc = mcJeb
	elif candidate == 6:
		mc = mcChristie
	for x in range(0,99):
		stringList.append(mc.generateString())
	if questionNum != None:
		for x in xrange(0,99):
			splitted = stringList[x].split()
			for y in range(0, len(splitted)):
				if (splitted[y].lower() in questions.questions[questionNum][1]) and (len(stringList[x].split()) > 4):
					return candidates[candidate] + stringList[x]  + "\n"
				else:
					while (True):
						randNum = random.randint(0,99)
						splitted = stringList[randNum].split()
						if (len(splitted) > 4):
							return candidates[candidate] + stringList[randNum] + "\n"
	else:
		while (True):
			randNum = random.randint(0,99)
			splitted = stringList[randNum].split()
			if (len(splitted) > 4):
				return candidates[candidate] + stringList[randNum]  + "\n"
	# pass

def responded(msg):
	for word in msg.split():
		if word in trump_names:
			return 0
		elif word in cruz_names:
			return 1
		elif word in rubio_names:
			return 2
		elif word in kasich_names:
			return 3
		elif word in carson_names:
			return 4
		elif word in jeb_names:
			return 5
		elif word in christie_names:
			return 6
	return None

mcTrump = MarkovChain("db/trumpdb")
mcCruz = MarkovChain("db/cruzdb")
mcRubio = MarkovChain("db/rubiodb")
mcKasich = MarkovChain("db/kasichdb")
mcCarson = MarkovChain("db/carsondb")
mcJeb = MarkovChain("db/jebdb")
mcChristie = MarkovChain("db/christiedb")

formalCandidates = ["Mr. Trump", "Senator Cruz", "Senator Rubio", "Governor Kasich", "Dr. Carson", "Governor Bush", "Governor Christie"]
candidates = ["TRUMP: ", "CRUZ: ", "RUBIO: ", "KASICH: ", "CARSON: ", "JEB: ", "CHRISTIE: "]

trump_names = ["Donald", "Donald's", "Trump", "Trump's", "Don"]
jeb_names = ["Jeb", "JEB", "Jeb's", "JEB's", "Bush", "Bush's"]
cruz_names = ["Cruz", "Cruz's", "Ted", "Ted's", "Rafeal"]
rubio_names = ["Marco", "Marco's", "Rubio", "Rubio's"]
kasich_names = ["Kasich", "Kasich's"]
christie_names = ["Chris", "Christie", "Christie's"]
carson_names = ["Ben", "Ben's", "Doctor", "Carson", "Carson's"]

isQuestion = True
randomChance = 0;
lastCandidateNum = ""
questionNum = ""
for x in range(0,10):
	candidateNum = random.randint(0,6)
	while (candidateNum == lastCandidateNum):
		candidateNum = random.randint(0,6)
	lastCandidateNum = candidateNum
	if isQuestion == True:
		questionNum = random.randint(0,20)
		print modQuestion(candidateNum, questionNum)
		msg =  response(candidateNum, questionNum)
		print msg
		isQuestion = False
		continue
	if responded(msg) != None:
		msg = response(responded(msg))
		print msg
		continue
	else:
		if (random.randint(0,4) + randomChance) > 3:
			isQuestion = True
			randomChance = 0
		else: 
			randomChance += 1
		msg = response(candidateNum, questionNum)
		print msg