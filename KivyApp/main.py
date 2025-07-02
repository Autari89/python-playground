from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp

from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText

# Define your Screen classes in Python
class MainScreen(Screen):
    pass

class WorkoutLogView(Screen):
    def on_ok(self, instance_date_picker):
        instance_date_picker.dismiss()
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The selected day is {instance_date_picker.get_date()[0]}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive"
        ).open()
    
    def on_cancel(self, instance_date_picker):
        instance_date_picker.dismiss()
        
    def show_date_picker(self):
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.open()

class HistoryView(Screen):
    pass

class FitnessTrackerApp(MDApp):
    def build(self):
        # Load the .kv file
        return Builder.load_file("fitness_tracker.kv")

if __name__ == "__main__":
    FitnessTrackerApp().run()
