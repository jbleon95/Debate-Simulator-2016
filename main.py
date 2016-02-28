import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class drawChat(Widget):
	pass

class drawMenu(Widget):
	pass
		
class DebateSimApp(App):
	def build(self):
		return drawMenu()

if __name__ == "__main__":
    DebateSimApp().run()
