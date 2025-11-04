from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os


class MainScreen(Screen):
    """Main screen of the fitness tracker app."""
    _kv_loaded = False

    def __init__(self, **kwargs):
        # Load the screen's .kv file only once
        if not MainScreen._kv_loaded:
            kv_file = os.path.join(os.path.dirname(__file__), "main_screen.kv")
            Builder.load_file(kv_file)
            MainScreen._kv_loaded = True
        super().__init__(**kwargs)
