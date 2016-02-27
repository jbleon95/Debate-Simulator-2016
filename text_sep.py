debate_file = open('rdebate10.txt', 'r')
trump_file = open("trump.txt", "w")
cruz_file = open("cruz.txt", "w")
rubio_file = open("rubio.txt", "w")
kasich_file = open("kasich.txt", "w")
carson_file = open("carson.txt", "w")
mod_file = open("mods.txt", "w")

def add_text(name, text):
	if name == "TRUMP:":
		trump_file.write(text + "\n")
	elif name == "CRUZ:":
		cruz_file.write(text + "\n")
	elif name == "RUBIO:":
		rubio_file.write(text + "\n")
	elif name == "KASICH:":
		kasich_file.write(text + "\n")
	elif name == "CARSON:":
		carson_file.write(text + "\n")
	elif name == "mods":
		mod_file.write(text + "\n")
	return

last_person = ""

people = ["TRUMP:", "CRUZ:", "RUBIO:", "KASICH:", "CARSON:"]
mods = ["BLITZER:", "BASH:", "ARRASAS:", "HEWITT:" ]
descriptions = ["(APPLAUSE)\n", "(LAUGHTER)\n", "(CHEERING)\n", "(CROSSTALK)\n", "(BELL RINGING)\n", "(BELL RINGS)\n"]

for x in range(0, 2122):
	line = debate_file.readline()
	if (line == "\n" or line in descriptions):
		continue
	split_line = line.split()
	name = split_line[0]
	if name in people:
		text = line.split(' ', 1)[1]
		add_text(split_line[0], text)
		last_person = split_line[0]
	elif name in mods:
		text = line.split(' ', 1)[1]
		add_text(mods, text)
		last_person = "mods"
	else:
		add_text(last_person, line)

trump_file.close()
cruz_file.close()
rubio_file.close()
kasich_file.close()
carson_file.close()
mod_file.close()
