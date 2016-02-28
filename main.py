import kivy
import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

"""red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]
"""

class drawChat(Widget):
	#colors = [red, green, blue, purple]
	pass
	
class drawMenu(Widget):
	pass
		
class DebateSimApp(App):
	#kivy.resources.resource_add_path('/profpics')
	#candidates = ["Trump", "Cruz", "Rubio", "Kasich", "Carson", "Bush", "Christie"]
	
	speaker = "Bluhaha!"
	Image(source='profpics/trump.jpg')
	def build(self):
		self.load_kv('DebateSim.kv')
		return drawMenu()

if __name__ == "__main__":
    DebateSimApp().run()