from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
import os


class ExerciseRow(MDBoxLayout):
    """Custom widget for exercise entry row with 5 fields and delete button."""
    
    # Class variable to track if KV file has been loaded
    _kv_loaded = False
    
    def __init__(self, parent_view=None, **kwargs):
        # Load the widget's .kv file only once
        if not ExerciseRow._kv_loaded:
            kv_file = os.path.join(os.path.dirname(__file__), 'exercise_row.kv')
            Builder.load_file(kv_file)
            ExerciseRow._kv_loaded = True
        
        super().__init__(**kwargs)
        self.parent_view = parent_view
    
    def remove_self(self):
        """Remove this exercise row from the parent view."""
        if self.parent_view and hasattr(self.parent_view, 'ids'):
            if hasattr(self.parent_view.ids, 'workout_entry_box'):
                self.parent_view.ids.workout_entry_box.remove_widget(self)
    
    def get_exercise_data(self):
        """Get the current data from all fields."""
        return {
            'exercise_name': self.ids.exercise_name.text,
            'sets': self.ids.sets_field.text,
            'reps': self.ids.reps_field.text,
            'weight': self.ids.weight_field.text,
            'notes': self.ids.notes_field.text
        }
    
    def set_exercise_data(self, data):
        """Set data to all fields."""
        self.ids.exercise_name.text = data.get('exercise_name', '')
        self.ids.sets_field.text = str(data.get('sets', ''))
        self.ids.reps_field.text = str(data.get('reps', ''))
        self.ids.weight_field.text = str(data.get('weight', ''))
        self.ids.notes_field.text = data.get('notes', '')
    
    def clear_fields(self):
        """Clear all input fields."""
        for field_id in ['exercise_name', 'sets_field', 'reps_field', 'weight_field', 'notes_field']:
            self.ids[field_id].text = ''
            