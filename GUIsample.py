import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

########################################################################
class VBoxLayoutExample(App):
    """
    Vertical oriented BoxLayout example class
    """

    #----------------------------------------------------------------------
    def setOrientation(self, orient):
        """"""
        self.orient = orient

    #----------------------------------------------------------------------
    def build(self):
        """"""
        layout = BoxLayout(padding=10, orientation=self.orient)

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1) )
            layout.add_widget(btn)
        return layout

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = VBoxLayoutExample()
    app.setOrientation(orient="vertical")
    app.run()