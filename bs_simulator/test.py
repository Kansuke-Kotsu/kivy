from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from PIL import Image as PILImage
from PIL import ImageDraw
import io
from kivy.graphics.texture import Texture

import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

class VectorToImageApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # URLから画像を取得
        url = "https://club.battlespirits.com/bsclub/mydeck/image/card_serch/card/SD65-CX01.jpg"
        response = requests.get(url)

        # 取得したデータを画像に変換
        image = Image.open(BytesIO(response.content))

        # 画像を表示
        img_widget = Image(texture=image)
        layout.add_widget(img_widget)
        
        return layout

if __name__ == '__main__':
    VectorToImageApp().run()
