from nicegui import Tailwind, ui 

class default_sidebar():
    def __init__(self):
        self.ui = ui
        with self.ui.left_drawer().classes('bg-gray-100') as left_drawer:
            self.ui.label('Left menu')
            self.ui.separator()
            with self.ui.expansion('Projects', icon='house').classes('w-full'):
                self.ui.label('Well 1').tailwind.text_color('bg-blue-500')
                self.ui.label('Well 2')
                self.ui.label('Well 3')
                self.ui.label('Well 4')
                self.ui.label('Well 5')