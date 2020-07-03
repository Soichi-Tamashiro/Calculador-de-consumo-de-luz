from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_string('''
<Root>:
    MainScreen:
        name: 'main'
    AnotherScreen:
        name: 'another'
<MainScreen>:
    BoxLayout:
        Button:
            text: 'next screen'
            on_release: root.parent.current='another'
        Button:
            text: 'ping!'
            on_release: root.ping()
<AnotherScreen>:
    BoxLayout:
        Button:
            text: 'previous screen'
            on_release: root.parent.current='main'
        Button:
            text: 'ping!'
            on_release: root.ping()
''')

class MainScreen(Screen):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)
        self.a = App.get_running_app()
    def ping(self):
        print(self.a.big_dict['hi'])

class AnotherScreen(Screen):
    def ping(self):
        b = App.get_running_app()
        print(b.big_dict['hi'])

class Root(ScreenManager):
    pass
class SimpleKivy(App):
    big_dict={'hi':'hi there!'}
    def build(self):
        return Root()
SimpleKivy().run()
