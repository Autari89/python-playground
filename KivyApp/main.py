from kivymd.app import MDApp
from kivy.lang import Builder

# Import screens
from screens import MainScreen, WorkoutLogView, HistoryView


class FitnessTrackerApp(MDApp):
    def build(self):
        # Load the main .kv file
        return Builder.load_file("fitness_tracker.kv")


if __name__ == "__main__":
    FitnessTrackerApp().run()
