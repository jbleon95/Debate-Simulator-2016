from pymarkovchain import MarkovChain

trump_file = open("trump.txt", "r")
cruz_file = open("cruz.txt", "r")
rubio_file = open("rubio.txt", "r")
kasich_file = open("kasich.txt", "r")
carson_file = open("carson.txt", "r")

trumpText = trump_file.read()
cruzText = cruz_file.read()
rubioText = rubio_file.read()
kasichText = kasich_file.read()
carsonText = carson_file.read()

mcTrump = MarkovChain("./trumpdb")
mcCruz = MarkovChain("./cruzdb")
mcRubio = MarkovChain("./rubiodb")
mcKasich = MarkovChain("./kasichdb")
mcCarson = MarkovChain("./carsondb")

mcTrump.generateDatabase(trumpText)
mcCruz.generateDatabase(cruzText)
mcRubio.generateDatabase(rubioText)
mcKasich.generateDatabase(kasichText)
mcCarson.generateDatabase(carsonText)

mcTrump.dumpdb()
mcCruz.dumpdb()
mcRubio.dumpdb()
mcKasich.dumpdb()
mcCarson.dumpdb()

trumpList = []
cruzList = []
rubioList = []
kasichList = []
carsonList = []

for x in xrange(1,100):
	trumpList.append(mcTrump.generateString())
	cruzList.append(mcCruz.generateString())
	rubioList.append(mcRubio.generateString())
	kasichList.append(mcKasich.generateString())
	carsonList.append(mcCarson.generateString())
	# pass


keyword = "Mexico".lower()
done = 0;
print len(trumpList)
for x in xrange(0,99):
	splitted = trumpList[x].split()
	for y in range(0, len(splitted)):
		if ((splitted[y].lower() == keyword) and (len(trumpList[x].split()) > 4) and done == 0):
			print trumpList[x]
			print len(trumpList[x].split())
			done = 1