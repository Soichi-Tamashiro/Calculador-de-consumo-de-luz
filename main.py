from kivy.app import App
from kivy.clock import mainthread
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget


class MainWindow(Screen):
    cargo_fijo = ObjectProperty()

    def btn(self, instance):
        # Interaction between Kivy widgets in Python
        # Use a dictionary to pass values between Classes
        b = App.get_running_app()
        # Populate dictionary keys
        b.big_dict = self.ids.keys
        # b.big_dict['botonazo']="Cotizar"
        # print(self.ids.keys())
        print(self.get_id(instance),instance.text)
        # print(b.big_dict)
    pass

    def get_id(self,  instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id


class SecondWindow(Screen, Widget):
    @mainthread
    def update(self):
        # Populate dictionary keys
        c = App.get_running_app()
        c.big_dict = self.ids.keys()
        print(c.big_dict)

    pass


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @mainthread
    def update(self):
        mainwindow = self.get_screen('main')
        secondwindow = self.get_screen('second')
        self.cargo_fijo_2.text = "hqy"
        # cargofijo=self.ids.WindowManager.MainWindow.cargo_fijo.text
        # self.cargo_fijo_2.text = cargofijo
        # print(cargofijo)
        pass

# kv = Builder.load_file("mymain.kv")


class MainApp(App):
    # Interaction between Kivy widgets in Python
    # Use a dictionary to pass values between Classes
    big_dict = {'hi': 'hi there!'}

    def build(self):
        # self.load_kv('main.kv')
        return WindowManager()


if __name__ == "__main__":
    MainApp().run()
