from kivy.app import App
from kivy.clock import mainthread
# from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget


class MainWindow(Screen):
    pass


class SecondWindow(Screen, Widget):
    pass


class WindowManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #
        # @mainthread
        # def delayed():
        #     mainwindow = self.get_screen('main')
        #     secondwindow = self.get_screen('second')
        # delayed()
    @mainthread
    def update(self, text):
        mainwindow = self.get_screen('main')
        secondwindow = self.get_screen('second')
        pass

# kv = Builder.load_file("mymain.kv")


class MainApp(App):
    def build(self):
        self.load_kv('main.kv')
        return WindowManager()


if __name__ == "__main__":
    MainApp().run()
