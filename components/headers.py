from nicegui import Tailwind, ui 

class default_header:
    def __init__(self):
        self.ui = ui
        with self.ui.header().classes(replace='font-mono shadow-md bg-white text-md min-h-12') as header:
            with self.ui.grid(columns=3).classes('flex flat box-shadow-none'):
                self.ui.button(
                    on_click=lambda: self.left_drawer.toggle(),
                    icon='menu'
                ).tailwind('flex-none', 'blue-000', 'm-2')

                self.ui.label('Vektir Labs').classes('flex-1 font-mono m-2 text-slate-600 text-lg font-bold')

