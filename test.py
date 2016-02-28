from graphics import *
import time
import ctypes

user32 = ctypes.windll.user32
print user32.IsProcessDPIAware()
screensize = user32.GetSystemMetrics(1)
print screensize
user32.SetProcessDPIAware(0)
screensize1 = user32.GetSystemMetrics(1)
print screensize1
scale = screensize1/screensize

winwidth = 1200
winheight = 800
win = GraphWin('title', winwidth, winheight)
bg = Image(Point(winwidth/2,winheight/2), "images/background.gif")
bg.draw(win)

# head = Circle(Point(40,100), 25) # set center and radius
# head.setFill("yellow")
# head.draw(win)

def modtextbox(window, pos):
	rect = Rectangle(Point(100,pos-25),Point(500,pos+25))
	rect.draw(win)
	circ = Circle(Point(60,pos), 25)
	circ.draw(win)
	label = Text(Point(150, pos), 'A face')
	label.draw(win)

	return label

def cantextbox(window, pos):
	rect = Rectangle(Point(100,pos-25),Point(500,pos+25))
	rect.draw(win)
	circ = Circle(Point(540,pos), 25)
	circ.draw(win)
	label = Text(Point(150, pos), 'A face')
	label.draw(win)

	return label

#side: 0 is left, 1 is right
def textbox(window, candidate, pos, text):
	string0 = ""
	string1 = ""
	string2 = ""
	textlist = text.split()
	for x in textlist:
		if(len(string0 + x + " ") < 165):
			string0 += (x+" ")
		elif(len(string0 + x + " ") >=165 and len(string1 + x + " ") < 165):
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
	if (candidate == 0):
		img = Image(Point(50,pos-10), "images/mod.gif")
		name = Text(Point(50,pos+30), "Moderator")
		rect.setFill(color_rgb(255,255,255))
	elif (candidate == 1):
		img = Image(Point(winwidth-50,pos-10), "images/trump.gif")
		name = Text(Point(winwidth-50,pos+30), "Trump")
		rect.setFill(color_rgb(188,87,87))
	elif (candidate == 2):
		img = Image(Point(winwidth-50,pos-10), "images/carson.gif")
		name = Text(Point(winwidth-50,pos+30), "Dr. Carson")
		rect.setFill(color_rgb(251,128,114))
	elif (candidate == 3):
		img = Image(Point(winwidth-50,pos-10), "images/rubio.gif")
		name = Text(Point(winwidth-50,pos+30), "Rubio")
		rect.setFill(color_rgb(190,186,218))
	elif (candidate == 4):
		img = Image(Point(winwidth-50,pos-10), "images/christie.gif")
		name = Text(Point(winwidth-50,pos+30), "Christie")
		rect.setFill(color_rgb(217,217,217))
	elif (candidate == 5):
		img = Image(Point(winwidth-50,pos-10), "images/cruz.gif")
		name = Text(Point(winwidth-50,pos+30), "Cruz")
		rect.setFill(color_rgb(141,211,199))
	elif (candidate == 6):
		img = Image(Point(winwidth-50,pos-10), "images/jeb.gif")
		name = Text(Point(winwidth-50,pos+30), "Bush")
		rect.setFill(color_rgb(253,180,98))
	elif (candidate == 7):
		img = Image(Point(winwidth-50,pos-10), "images/kasich.gif")
		name = Text(Point(winwidth-50,pos+30), "Kasich")
		rect.setFill(color_rgb(128,177,211))
	img.draw(win)
	name.setSize((int) (10/scale))
	name.draw(win)
	label0 = Text(Point(winwidth/2, pos-offset[1]), string0) #pos+-25
	label0.setSize((int) (9/scale))
	label0.setStyle('bold')
	label0.draw(win)
	label1 = Text(Point(winwidth/2, pos+offset[2]), string1)
	label1.setSize((int) (9/scale))
	label1.setStyle('bold')
	label1.draw(win)
	label2 = Text(Point(winwidth/2, pos+offset[1]), string2) #pos+-25
	label2.setSize((int) (9/scale))
	label2.setStyle('bold')
	label2.draw(win)

	objlist = [img, rect, name, label0, label1, label2]
	return objlist


test0 = textbox(win, 0, winheight-50, "And when they fight for you every day, and not for the American people is, on religious liberty, but this is something he cares about, why has he supported anti-Israel politicians from Jimmy Carter, to Hillary Clinton, Chuck Schumer, to Harry Reid was asked, of all the people who have gotten laid off because it's teenaged kids like my dad when he chants, \"Death to America,\" he means it.")

test1 = textbox(win, 1, winheight-150, "And when they fight for you every day, and not for the American people is, on religious liberty, but this is something he cares about, why has he supported anti-Israel politicians from Jimmy Carter, to Hillary Clinton")

test2 = textbox(win, 2, winheight-250, "It would allow public money to invest in the history of the United States the way they work for future generations to make America more like the rest of the mother because I'm influencing social policy, this is an important point.")

test3 = textbox(win, 3, winheight-350, "candidate")

test4 = textbox(win, 4, winheight-450, "candidate")

test5 = textbox(win, 5, winheight-550, "candidate")

test6 = textbox(win, 6, winheight-650, "candidate")

test7 = textbox(win, 7, winheight-750, "candidate")


# time.sleep(3) # delays for 5 seconds

# test2[2].setText("Trump sucks")

win.getMouse()