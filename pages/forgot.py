from nicegui import Tailwind, ui 

class forgot_page:
    def __init__(self):
        self.ui = ui

        # Header ----------------------------------
        with self.ui.header().classes(replace='flex block font-mono shadow-md bg-white text-md  items-center min-h-12') as header:
            with self.ui.grid(columns=3).classes('flex flat box-shadow-none'):
                self.ui.label('Vektir Labs').classes('flex-1 font-mono m-2 pl-4 text-slate-600 text-lg font-bold')

                # Sign up button ----------------------------------    
                self.ui.button('Home', on_click=lambda: ui.navigate.to('/', new_tab=False),
                ).tailwind('flex-none','w-100', 'bg-gray-600','text-grey-800','capitalize', 'm-2')

        # Body ----------------------------------
        with ui.row().classes('flex flex-col w-full bg-white items-center py-2'):
            self.ui.markdown('## **Forgot Password**').tailwind('grid', 'grid-flow-col', 'auto-cols-max')
            self.ui.separator().classes('w-60')
        with ui.row().classes('flex flex-col w-full bg-white items-center py-2'):
            email = self.ui.input(label='Email', placeholder='Your email').classes('w-60')
            submit = self.ui.button('Send Password Rest email').classes('w-60 bg-red text-white font-bold py-2 px-4 rounded')