from nicegui import Tailwind, ui 

class login_page:
    def __init__(self):
        self.ui = ui

        # Header ----------------------------------
        with self.ui.header().classes(replace='font-mono shadow-md bg-white text-md min-h-12') as header:
            with self.ui.grid(columns=3).classes('flex flat box-shadow-none'):
                self.ui.label('Vektir Labs').classes('flex-1 font-mono m-2 text-slate-600 text-lg font-bold')

        # Body ----------------------------------
        with ui.row().classes('w-full align-center'):
            self.ui.markdown('### Login Page').tailwind('grid', 'grid-flow-col', 'auto-cols-max')

        with ui.column().classes('flex justify-center'):
            email = self.ui.input(label='Email', placeholder='Your email').classes('w-60')
            password = self.ui.input(label='Password', placeholder='Your password', 
                                password=True, password_toggle_button=True).classes('w-60')
            submit = self.ui.button('Login').classes('w-60 bg-blue-500 text-white font-bold py-2 px-4 rounded')