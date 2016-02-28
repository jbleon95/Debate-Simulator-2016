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

#Asks a moderator question to the randomly chosen candidate
def modQuestion(candidate, num):
	return "MODERATOR: " + candidateInfo[candidate][2] + questions.questions[num][0]  + "\n"

#Responds to a question on topic if it can, else picks random message
def response(candidate, questionNum = None):
	stringList = []
	mc = candidateInfo[candidate][0]
	for x in range(0,499):
		stringList.append(mc.generateString())
	#Attempts to respond to question by searching strings for specific keywords in questions, else returns random message
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
	#If no question number, picks a random messsage
	else:
		while (True):
			randNum = random.randint(0,499)
			splitted = stringList[randNum].split()
			if (len(splitted) > 5):
				return candidateInfo[candidate][3] + stringList[randNum]  + "\n"

#determines if another candidate is mentioned and returns their number, else returns none
def responded(msg):
	for word in msg.split():
		for key in candidateInfo:
			if word in candidateInfo[key][1]:
				return key
	return None

mcTrump = MarkovChain("db/trumpdb")
mcCruz = MarkovChain("db/cruzdb")
mcRubio = MarkovChain("db/rubiodb")
mcKasich = MarkovChain("db/kasichdb")
mcCarson = MarkovChain("db/carsondb")
mcJeb = MarkovChain("db/jebdb")
mcChristie = MarkovChain("db/christiedb")

#List of candidates to be included in Debate
candidateList = ["Trump", "Rubio", "Christie", "Cruz", "Carson", "Jeb", "Kasich"]
candidateInfo = {}

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

#Range determines number of responses with a small chance of one more if last message is a question
for x in range(0,10):
	#Randomly generates a candidate by choosing their number
	candidateNum = random.randint(0, numCandidates)
	#Ensures chosen candidate did not speak last round
	while (candidateNum == lastCandidateNum):
		candidateNum = random.randint(0, numCandidates)
	lastCandidateNum = candidateNum
	#If its time for a question, it will ask one with a response, then turn isQuestion off
	if isQuestion == True:
		questionNum = random.randint(0,20)
		print modQuestion(candidateNum, questionNum)
		msg =  response(candidateNum, questionNum)
		print msg
		isQuestion = False
		continue
	#If someone was mentioned in the last msg, responded will return their number and they will respond
	if responded(msg) != None:
		msg = response(responded(msg))
		print msg
		continue
	else:
		#If candidate is not responding, base chance of mod asking question next round is 25%
		#Every round of no response will increase the chances by 25%
		if (random.randint(0,4) + randomChance) > 3:
			isQuestion = True
			randomChance = 0
		else: 
			randomChance += 1
		msg = response(candidateNum, questionNum)
		print msg