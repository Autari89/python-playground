from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText
from kivy.lang import Builder
import os
from widgets import ExerciseRow


class WorkoutLogView(Screen):
    """Screen for logging workout exercises."""
    
    # Class variable to track if KV file has been loaded
    _kv_loaded = False
    
    def __init__(self, **kwargs):
        # Load the screen's .kv file only once
        if not WorkoutLogView._kv_loaded:
            kv_file = os.path.join(os.path.dirname(__file__), 'workout_log_view.kv')
            Builder.load_file(kv_file)
            WorkoutLogView._kv_loaded = True
        super().__init__(**kwargs)
    
    def add_exercise_row(self):
        """Add a new exercise entry row to the workout."""
        exercise_row = ExerciseRow(parent_view=self)
        self.ids.workout_entry_box.add_widget(exercise_row, index=1)

    def on_ok(self, instance_date_picker):
        """Handle date picker OK button."""
        instance_date_picker.dismiss()
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The selected day is {instance_date_picker.get_date()[0]}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive",
        ).open()

        self.date_label.text = f"Chosen date: {instance_date_picker.get_date()[0]}"
        self.add_exercise_row()

    def on_cancel(self, instance_date_picker):
        """Handle date picker cancel button."""
        instance_date_picker.dismiss()

    def show_date_picker(self):
        """Show the date picker modal."""
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.open()
    
    def get_all_exercise_data(self):
        """Get data from all exercise rows."""
        exercises = []
        for child in self.ids.workout_entry_box.children:
            if isinstance(child, ExerciseRow):
                exercises.append(child.get_exercise_data())
        return exercises
    
    def clear_all_exercises(self):
        """Remove all exercise rows."""
        children_to_remove = [child for child in self.ids.workout_entry_box.children 
                             if isinstance(child, ExerciseRow)]
        for child in children_to_remove:
            self.ids.workout_entry_box.remove_widget(child)
            