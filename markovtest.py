from pymarkovchain import MarkovChain

carson_file = open("transcripts/cruz.txt", "r")

carson_text = carson_file.read()

mc = MarkovChain("./cruzbase")

string = mc.generateString()

print string

trump_names = ["Donald", "Donald's", "Trump", "Trump's", "Don"]
jeb_names = ["Jeb", "JEB", "Jeb's", "JEB's", "Bush", "Bush's"]
cruz_names = ["Cruz", "Cruz's", "Ted", "Ted's", "Rafeal"]
rubio_names = ["Marco", "Marco's", "Rubio", "Rubio's"]
kasich_names = ["Kasich", "Kasich's"]
christie_names = ["Chris", "Christie", "Christie's"]
carson_names = ["Ben", "Ben's", "Doctor", "Carson", "Carson's"]

for x in string.split():
	if x in trump_names:
		print "\nTrump Mentioned"
		break