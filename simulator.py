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
	return "MODERATOR: " + candidateInfo[candidate][2] + questions.questions[num][0]  + "\n"

def response(candidate, questionNum = None):
	stringList = []
	mc = candidateInfo[candidate][0]
	for x in range(0,499):
		stringList.append(mc.generateString())
	if questionNum != None:
		for x in range(0,499):
			splitted = stringList[x].split()
			for y in range(0, len(splitted)):
				if (splitted[y].lower() in questions.questions[questionNum][1]) and (len(stringList[x].split()) > 10):
					return candidateInfo[candidate][3] + stringList[x]  + "\n"
		while (True):
			randNum = random.randint(0,498)
			splitted = stringList[randNum].split()
			if (len(splitted) > 15):
				return candidateInfo[candidate][3] + stringList[randNum] + "\n"
	else:
		while (True):
			randNum = random.randint(0,499)
			splitted = stringList[randNum].split()
			if (len(splitted) > 5):
				return candidateInfo[candidate][3] + stringList[randNum]  + "\n"

def responded(msg):
	for word in msg.split():
		for key in candidateInfo:
			if word in candidateInfo[key][1]:
				return key
	return None

candidateInfo = {}

mcTrump = MarkovChain("db/trumpdb")
mcCruz = MarkovChain("db/cruzdb")
mcRubio = MarkovChain("db/rubiodb")
mcKasich = MarkovChain("db/kasichdb")
mcCarson = MarkovChain("db/carsondb")
mcJeb = MarkovChain("db/jebdb")
mcChristie = MarkovChain("db/christiedb")

candidateList = ["Trump", "Rubio", "Christie", "Cruz", "Carson", "Jeb", "Kasich"]

z = 0
for name in candidateList:
	if name == "Trump":
		info = [mcTrump, ["Donald", "Donald's", "Trump", "Trump's", "Don"], "Mr. Trump", "TRUMP: "]
	elif name == "Cruz":
		info = [mcCruz, ["Cruz", "Cruz's", "Ted", "Ted's", "Rafeal"], "Senator Cruz", "CRUZ: "]
	elif name == "Rubio":
		info = [mcRubio, ["Marco", "Marco's", "Rubio", "Rubio's"], "Senator Rubio", "RUBIO: "]
	elif name == "Kasich":
		info = [mcKasich, ["Kasich", "Kasich's"], "Governor Kasich", "KASICH: "]
	elif name == "Carson":
		info = [mcCarson, ["Ben", "Ben's", "Doctor", "Carson", "Carson's"], "Dr. Carson", "CARSON: "]
	elif name == "Jeb":
		info = [mcJeb, ["Jeb", "JEB", "Jeb's", "JEB's", "Bush", "Bush's"], "Governor Bush", "JEB: "]
	elif name == "Christie":
		info = [mcChristie, ["Christie", "Christie's"] , "Governor Christie", "CHRISTIE: "]
	candidateInfo[z] = info
	z += 1

numCandidates = len(candidateList) - 1	

isQuestion = True
randomChance = 0;
lastCandidateNum = ""
questionNum = ""
for x in range(0,10):
	candidateNum = random.randint(0, numCandidates)
	while (candidateNum == lastCandidateNum):
		candidateNum = random.randint(0, numCandidates)
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