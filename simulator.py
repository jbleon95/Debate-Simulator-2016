from pymarkovchain import MarkovChain
from graphics import *
import questions
import random
import time

"""
trump_file = open("debateText/trump.txt", "r")
cruz_file = open("debateText/cruz.txt", "r")
rubio_file = open("debateText/rubio.txt", "r")
kasich_file = open("debateText/kasich.txt", "r")
carson_file = open("debateText/carson.txt", "r")
jeb_file = open("debateText/jeb.txt", "r")
christie_file = open("debateText/christie.txt", "r")

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
	return candidateInfo[candidate][2] + questions.questions[num][0]  + "\n"

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
					return format(stringList[x])
		while (True):
			randNum = random.randint(0,498)
			splitted = stringList[randNum].split()
			if (len(splitted) > 15):
				return format(stringList[randNum])
	#If no question number, picks a random messsage
	else:
		while (True):
			randNum = random.randint(0,499)
			splitted = stringList[randNum].split()
			if (len(splitted) > 5):
				return format(stringList[randNum])

#determines if another candidate is mentioned and returns their number, else returns none
def responded(msg):
	for word in msg.split():
		for key in candidateInfo:
			if word in candidateInfo[key][1]:
				return key
	return None

def format(msg):
	if (msg[len(msg) -1] is not "." or "!" or '?'):
		msg = msg + "."
		return msg
	else:
		return msg

def log(wfile, msg, candidate = None, questionNum = None):
	if questionNum != None:
		msg = "MODERATOR: " + candidateInfo[candidate][2] + questions.questions[questionNum][0]  + "\n"
		wfile.write(msg + "\n")
		return
	elif candidate != None:
		msg = candidateInfo[candidate][3] + msg + "\n"
		wfile.write(msg + "\n")
		return
	else:
		msg = "MODERATOR: " + msg
		wfile.write(msg + "\n")

def makeWriteFile():
	timeStr = time.strftime('%m-%d-%Y_%H_%M_%S')
	writeStr = "Debate_Transcript_" + timeStr + ".txt"
	return open("transcripts/" + writeStr, "w")

def textbox(window, candidate, pos, text):
	string0 = ""
	string1 = ""
	string2 = ""
	textlist = text.split()
	for x in textlist:
		if(len(string0 + x + " ") < 175):
			string0 += (x+" ")
		elif(len(string0 + x + " ") >=175 and len(string1 + x + " ") < 175):
			string1 += (x+" ")
		else:
			string2 += (x+" ")
	if (string2 == ""):
		if (string1 == ""):
			offset = [15,0,0]
		else:
			offset = [30,15,10]
	else:
		offset = [40,25,0]
	rect = Rectangle(Point(100,pos-offset[0]),Point(winwidth-100,pos+offset[0])) #pos+-40
	rect.draw(win)
	if (candidate == "TRUMP: "):
		img = Image(Point(winwidth-50,pos-10), "images/trump.gif")
		name = Text(Point(winwidth-50,pos+30), "Trump")
		rect.setFill(color_rgb(188,87,87))
	elif (candidate == "CARSON: "):
		img = Image(Point(winwidth-50,pos-10), "images/carson.gif")
		name = Text(Point(winwidth-50,pos+30), "Dr. Carson")
		rect.setFill(color_rgb(251,128,114))
	elif (candidate == "RUBIO: "):
		img = Image(Point(winwidth-50,pos-10), "images/rubio.gif")
		name = Text(Point(winwidth-50,pos+30), "Rubio")
		rect.setFill(color_rgb(190,186,218))
	elif (candidate == "CHRISTIE: "):
		img = Image(Point(winwidth-50,pos-10), "images/christie.gif")
		name = Text(Point(winwidth-50,pos+30), "Christie")
		rect.setFill(color_rgb(217,217,217))
	elif (candidate == "CRUZ: "):
		img = Image(Point(winwidth-50,pos-10), "images/cruz.gif")
		name = Text(Point(winwidth-50,pos+30), "Cruz")
		rect.setFill(color_rgb(141,211,199))
	elif (candidate == "BUSH: "):
		img = Image(Point(winwidth-50,pos-10), "images/jeb.gif")
		name = Text(Point(winwidth-50,pos+30), "Bush")
		rect.setFill(color_rgb(253,180,98))
	elif (candidate == "KASICH: "):
		img = Image(Point(winwidth-50,pos-10), "images/kasich.gif")
		name = Text(Point(winwidth-50,pos+30), "Kasich")
		rect.setFill(color_rgb(128,177,211))
	elif (candidate == "mod"):
		img = Image(Point(50,pos-10), "images/mod.gif")
		name = Text(Point(50,pos+30), "Moderator")
	img.draw(win)
	name.setSize(10)
	name.draw(win)
	label0 = Text(Point(winwidth/2, pos-offset[1]), string0) #pos+-25
	label0.setSize(9)
	label0.setStyle('bold')
	label0.draw(win)
	label1 = Text(Point(winwidth/2, pos+offset[2]), string1)
	label1.setSize(9)
	label1.setStyle('bold')
	label1.draw(win)
	label2 = Text(Point(winwidth/2, pos+offset[1]), string2) #pos+-25
	label2.setSize(9)
	label2.setStyle('bold')
	label2.draw(win)

	objlist = [img, rect, name, label0, label1, label2]
	return objlist

def moveAll(shapeList, dx, dy):
    for shape in shapeList: 
        shape.move(dx, dy)

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)

writeFile = makeWriteFile()

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
		info = [mcJeb, ["Jeb", "JEB", "Jeb's", "JEB's", "Bush", "Bush's"], "Governor Bush", "BUSH: "]
	elif name == "Christie":
		info = [mcChristie, ["Chris", "Christie", "Christie's"] , "Governor Christie", "CHRISTIE: "]
	candidateInfo[z] = info
	z += 1

numCandidates = len(candidateList) - 1	

isQuestion = True
randomChance = 0;
lastCandidateNum = ""
questionNum = ""

debateDict = {}
msgNum = 0
#Range determines number of responses with a small chance of one more if last message is a question
for x in range(0,20):
	#Randomly generates a candidate by choosing their number
	candidateNum = random.randint(0, numCandidates)
	#Ensures chosen candidate did not speak last round
	while (candidateNum == lastCandidateNum):
		candidateNum = random.randint(0, numCandidates)
	lastCandidateNum = candidateNum
	#If its time for a question, it will ask one with a response, then turn isQuestion off
	if isQuestion == True:
		questionNum = random.randint(0,20)
		que = modQuestion(candidateNum, questionNum)
		log(writeFile, que, candidateNum, questionNum)
		debateDict[msgNum] = [que, "mod"]
		msgNum += 1
		msg =  response(candidateNum, questionNum)
		log(writeFile, msg, candidateNum)
		debateDict[msgNum] = [msg, candidateInfo[candidateNum][3]]
		msgNum += 1
		isQuestion = False
		continue
	#If someone was mentioned in the last msg, responded will return their number and they will respond
	nameMention = responded(msg)
	if nameMention != None:
		msg = response(nameMention)
		log(writeFile, msg, candidateNum)
		debateDict[msgNum] = [msg, candidateInfo[candidateNum][3]]
		msgNum += 1
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
		log(writeFile, msg, candidateNum)
		debateDict[msgNum] = [msg, candidateInfo[candidateNum][3]]
		msgNum += 1

msg = "That concludes tongight's 2016 Republican Debate. Thank you, and good night."
log(writeFile, msg)
debateDict[msgNum] = [msg, "mod"]
msgNum +=1

writeFile.close()

winwidth = 1200
winheight = 800
win = GraphWin('Debate Simulator 2016', winwidth, winheight)
bg = Image(Point(winwidth/2,winheight/2), "images/background.gif")
bg.draw(win)

msgList = []
shapeNum = 0;
pos = winheight - 50
for x in range (0, msgNum):
	textboxList = textbox(win, debateDict[x][1], pos, debateDict[x][0])
	for item in textboxList:
		msgList.append(item)
	pos += 100

scroll = msgNum*100
moveAllOnLine(msgList, 0, -1, msgNum*100, 0.025)
win.getMouse()