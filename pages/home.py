from nicegui import Tailwind, ui

class home_page:
    def __init__(self):
        self.ui = ui
        self.un = 'Guest'
        self.ui.page_title('Home')
        self.isAuthd = False

        # Dialogs ----------------------------------
        with self.ui.dialog().classes('bg-white w-48') as settings_dialog:
            with self.ui.card():
                self.ui.label('Settings').tailwind('text-xl','w-48', 'p-2', 'font-bold',)
                ui.separator()
                ui.switch('switch me')
                ui.switch('switch me')
                ui.switch('switch me')

        with self.ui.dialog().classes('bg-white w-48') as create_new_dialog:
            with self.ui.card():
                self.ui.label('Create new Project').tailwind('text-xl','w-96', 'p-2', 'font-bold')
                self.ui.separator()
                well_name = self.ui.input(label='Well Name', placeholder='Your Wells Name').classes('w-48')
                self.ui.switch('Add Comments')
                self.ui.switch('Add Attachments').props('enabled')
                self.ui.switch('Add Tags')

                self.ui.button('Create new Project', on_click=lambda: '',).classes('w-full capitalize bg-blue-500 text-white font-bold py-2 px-4 p-2 rounded')


        # Header ----------------------------------
        with self.ui.header().classes(replace='font-mono shadow-md bg-white text-md min-h-12') as header:
            with self.ui.grid(columns=3).classes('flex justify-between flat box-shadow-none'):
                
                self.ui.button(on_click=lambda: left_drawer.toggle(), icon='menu'
                ).tailwind('flex-none', 'bg-slate-500', 'm-2')

                self.ui.label('Vektir Labs').classes('flex-1 p-2 font-mono text-slate-600 text-lg font-bold')

                # Settings button ----------------------------------    
                self.ui.button(icon='settings', on_click=lambda: settings_dialog.open(),
                ).tailwind('flex-none','w-100', 'bg-gray-600','text-grey-800','capitalize', 'm-2')

        # Body ----------------------------------
        with self.ui.row().classes('flex w-full bordered'):
            with self.ui.column().classes('flex flex-col w-full bg-white h-screen items-center py-2'):
                self.ui.link('landing Page', '/')
                self.ui.link('Home', '/home')
                self.ui.link('Login', '/login')
                self.ui.link('Temp', '/temp')
           
        # Left Sidebar ----------------------------------
        with self.ui.left_drawer().classes('bg-gray-100 font-mono shadow-md') as left_drawer:
            self.ui.label(f'Welcome, {self.un}!').tailwind('w-full', 'text-lg', 'blue-500', 'text-center')
            ui.separator()

            self.ui.button('Create',icon='add', on_click=lambda: create_new_dialog.open()
                ).tailwind('flex', 'flex-col','block','capitalize','rounded-full', 'text-center','w-full', 'bg-blue-500', 'text-white', 'font-bold',)

            with self.ui.expansion('Projects').classes('w-full'):
                self.ui.label('Well 1').tailwind.text_color('bg-blue-500')
                self.ui.label('Well 2')
                self.ui.label('Well 3')
                self.ui.label('Well 4')
                self.ui.label('Well 5')

            # self.ui.space()
            # with ui.element('q-fab').props('icon=navigation color=blue-5'):
            #     self.ui.element('q-fab-action').props('icon=train color=blue-5') 
               