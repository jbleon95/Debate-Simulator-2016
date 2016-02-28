from pymarkovchain import MarkovChain

carson_file = open("carson.txt", "r")

carson_text = carson_file.read()


mc = MarkovChain("./carsondbase")

mc.generateDatabase(carson_text)

mc.dumpdb()

print mc.generateString()
