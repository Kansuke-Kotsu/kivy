from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from functools import partial

import func

class MyApp(App):
    def getlinkInfo(self, event): 
        deck_info = func.scrape_data(self.linkInput.text) 
        self.text_list = [deck_info[0], deck_info[1], deck_info[2], deck_info[3]]
        self.update_labels()

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.layout = BoxLayout(orientation='horizontal')
        
        self.linkInput = TextInput(text="", pos_hint={'center_x':0.5, 'center_y':0.65},
                            size_hint=(1,None), height=48,
                            font_size=29, foreground_color=(0,.5,0))

        self.linkButton = Button(text="Update List", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(.2, .1), font_size=24)
        self.linkButton.bind(on_press=self.getlinkInfo)

        self.layout_labels = BoxLayout(orientation='horizontal')
        
        self.text_list = ["https://club.battlespirits.com/bsclub/mydeck/image/card_serch/card/SD65-CX01.jpg", 
                          "https://club.battlespirits.com/bsclub/mydeck/image/card_serch/card/SD65-CX01.jpg", 
                          "https://club.battlespirits.com/bsclub/mydeck/image/card_serch/card/SD65-CX01.jpg", 
                          "https://club.battlespirits.com/bsclub/mydeck/image/card_serch/card/SD65-CX01.jpg"]
        

        
        self.layout.add_widget(self.layout_labels)
        layout.add_widget(self.linkInput)
        layout.add_widget(self.linkButton)
        layout.add_widget(self.layout)
                
        return layout

    def update_labels(self):
        # レイアウト内のラベルをすべてクリア
        self.layout_labels.clear_widgets()

        # 画面横幅の1/4に基づいて画像サイズを設定
        image_width = Window.width / 4

        for text in self.text_list:
            image = AsyncImage(source=text, width=image_width)
            self.layout_labels.add_widget(image)

if __name__ == '__main__':
    MyApp().run()
