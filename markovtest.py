candidateList = ["Trump", "Rubio", "Christie", "Cruz", "Carson", "Jeb", "Kasich"]
candidateInfo = {}

z = 0
for name in candidateList:
	if name == "Trump":
		info = [["Donald", "Donald's", "Trump", "Trump's", "Don"], "Mr. Trump", "TRUMP: "]
	elif name == "Cruz":
		info = [["Cruz", "Cruz's", "Ted", "Ted's", "Rafeal"], "Senator Cruz", "CRUZ: "]
	elif name == "Rubio":
		info = [["Marco", "Marco's", "Rubio", "Rubio's"], "Senator Rubio", "RUBIO: "]
	elif name == "Kasich":
		info = [["Kasich", "Kasich's"], "Governor Kasich", "KASICH: "]
	elif name == "Carson":
		info = [["Ben", "Ben's", "Doctor", "Carson", "Carson's"], "Dr. Carson", "CARSON: "]
	elif name == "Jeb":
		info = [["Jeb", "JEB", "Jeb's", "JEB's", "Bush", "Bush's"], "Governor Bush", "BUSH: "]
	elif name == "Christie":
		info = [["Chris", "Christie", "Christie's"] , "Governor Christie", "CHRISTIE: "]
	candidateInfo[z] = info
	z += 1

def responded(msg):
	for word in msg.split():
		for key in candidateInfo:
			if word in candidateInfo[key][0]:
				return key
	return None

mess = "And while Donald Trump brought up the fact that Governor Kasich is supporting spending more money on drug treatment and mental health."

if responded(mess) != None:
	print "RESPONDED " + str(responded(mess))
