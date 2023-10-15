from kivy.app import App
from kivymd.app import MDApp

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button

from kivy.core.window import Window
from functools import partial

Window.size = (500, 600)

class MyApp(App):
    def getlinkInfo(self, event, window):
        self.link = self.linkInput.text
        print("url: " + self.link)
    
    def build(self):
        layout = RelativeLayout()
        
        self.decklink = Label(text="Please Input your link",
                              pos_hint={'center_x': 0.5, "center_y": .75},
                              size_hint=(1,1), font_size=20, color=(1,0,0))

        self.linkInput = TextInput(text="", pos_hint={'center_x':0.5, 'center_y':0.65},
                                   size_hint=(1,None), height=48,
                                   font_size=29, foreground_color=(0,.5,0))

        self.linkButton = Button(text="Simulation", pos_hint={'center_x':0.5, 'center_y':0.5},
                                 size_hint=(.2,.1), font_size=24)
        
        self.linkButton.bind(on_press=partial(self.getlinkInfo, layout))

        layout.add_widget(self.decklink)
        layout.add_widget(self.linkInput)
        layout.add_widget(self.linkButton)
        
        return layout

if __name__ == '__main__':
    MyApp().run()