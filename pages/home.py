from nicegui import Tailwind, ui 

class home_page:
    def __init__(self):
        self.ui = ui

        # Header ----------------------------------
        with self.ui.header().classes(replace='font-mono shadow-md bg-white text-md min-h-12') as header:
            with self.ui.grid(columns=3).classes('flex flat box-shadow-none'):
                self.ui.button(
                    on_click=lambda: left_drawer.toggle(),
                    icon='menu'
                ).tailwind('flex-none', 'blue-000', 'm-2')

                self.ui.label('Vektir Labs').classes('flex-1 font-mono m-2 text-slate-600 text-lg font-bold')

        # Body ----------------------------------
        with ui.row().classes('w-full'):
            self.ui.label('Home Page')
            self.ui.link('landing Page', '/')
            self.ui.link('Home', '/home')
            self.ui.link('Login', '/login')
            self.ui.separator()

        # Sidebar ----------------------------------
        with self.ui.left_drawer().classes('bg-gray-100') as left_drawer:
            self.ui.label('Left menu')
            self.ui.separator()
            with self.ui.expansion('Projects', icon='house').classes('w-full'):
                self.ui.label('Well 1').tailwind.text_color('bg-blue-500')
                self.ui.label('Well 2')
                self.ui.label('Well 3')
                self.ui.label('Well 4')
                self.ui.label('Well 5')