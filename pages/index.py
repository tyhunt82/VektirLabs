from nicegui import Tailwind, ui 

class index_page:
    def __init__(self):
        self.ui = ui
        username = 'Guest' # This will be replaced with the actual username and annonimous user
        self.ui.page_title('Vektir Labs')

        # Header ----------------------------------
        with self.ui.header().classes(replace='font-mono shadow-md bg-white text-md') as header:
            with self.ui.grid().classes('flex block text-center flat box-shadow-none'):
                self.ui.label('Vektir Labs').classes('flex-1 p-2 font-mono text-slate-600 text-lg font-bold')         

        # Body ----------------------------------

