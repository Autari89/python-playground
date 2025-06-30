from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Define your Screen classes in Python
class MainScreen(Screen):
    pass

class SecondaryScreen(Screen):
    pass

class TwoViewsApp(App):
    def build(self):
        # Load the .kv file
        return Builder.load_file("two_views.kv")

if __name__ == "__main__":
    TwoViewsApp().run()
