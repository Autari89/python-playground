from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os


class HistoryView(Screen):
    """Screen for viewing workout history."""

    _kv_loaded = False

    def __init__(self, **kwargs):
        # Load the screen's .kv file only once
        if not HistoryView._kv_loaded:
            kv_file = os.path.join(os.path.dirname(__file__), "history_view.kv")
            Builder.load_file(kv_file)
            HistoryView._kv_loaded = True
        super().__init__(**kwargs)
