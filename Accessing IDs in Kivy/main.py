# test_app.py
# run me as...  python test_app.py --size 400x500


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from random import random as rand


kv = """
<ContainerBox>:
    BoxLayout:
        id: main_box
        orientation: 'vertical'
        padding: root.width * .02, root.width * .02, root.width * .02, root.width * .03
        spacing: root.width * .02

        Label:
            id: titlebar
            text: "NEMOM TEST APP -- v" + root.__version__
            font_size: '20sp'
            bold: True
            size_hint_y: None
            height: self.texture_size[1]
            color: [1, 1, 1, 1]
            canvas.before:
                Color:
                    rgba: [0, .6, 1, 1]
                Rectangle:
                    pos: self.pos
                    size: self.size

        Button:
            id: big_button
            halign: 'center'
            color: [1, 1, 1, 1]
            background_color: [2, 0, 0, 1]
            font_size: '50sp'
            bold: True
            on_press: root.push_button()
"""

Builder.load_string(kv)


class ContainerBox(BoxLayout):
    __version__ = '1.0.0'
    __author__ = 'Nemo M'

    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)
        self.ids.big_button.text = "DON'T PUSH\nTHE BIG,\nRED BUTTON!"

    def push_button(self):
        print(self.ids.keys())
        self.ids.big_button.background_color = [rand() * 2, rand() * 2, rand() * 2, 1]
        self.ids.big_button.text = self.ids.big_button.text.replace(',\nRED ', '\n')


class TestApp(App):
    def build(self):
        return ContainerBox()


if __name__=='__main__':
    TestApp().run()
