from pymarkovchain import MarkovChain

trump_file = open("trump.txt", "r")
cruz_file = open("cruz.txt", "r")
rubio_file = open("rubio.txt", "r")
kasich_file = open("kasich.txt", "r")
carson_file = open("carson.txt", "r")

mcTrump = MarkovChain("./trumpdb")
mcCruz = MarkovChain("./cruzdb")
mcRubio = MarkovChain("./rubiodb")
mcKasich = MarkovChain("./kasichdb")
mcCarson = MarkovChain("./carsondb")


trumpText = trump_file.read()
cruzText = cruz_file.read()
rubioText = rubio_file.read()
kasichText = kasich_file.read()
carsonText = carson_file.read()

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

print mcTrump.generateString() + ".\n"
print mcCruz.generateString() + ".\n"
print mcRubio.generateString() + ".\n"
print mcKasich.generateString() + ".\n"
print mcCarson.generateString() + ".\n"
