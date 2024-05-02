from nicegui import Tailwind, ui 

class index_page:
    def __init__(self):
        self.ui = ui
        self.ui.page_title('Vektir Labs')
        self.isAuthd = False

        # Dialogs ----------------------------------
        # Login form -------------------------------
        with self.ui.dialog() as login_dialog:
            with self.ui.card():
                self.ui.label('Login').tailwind('text-xl','w-48', 'p-2', 'font-bold',)
                email = self.ui.input(label='Email', placeholder='Your email').classes('w-48 p-2')
                password = self.ui.input(label='Password', placeholder='Your password', password=True, ).classes('w-48 p-2')
                fpw = self.ui.link('Forgot Password', '/forgot').classes('block text-center p-2')
                submit = self.ui.button('Login', on_click=lambda: '',
                    ).classes('w-48 bg-green text-white font-bold py-2 px-4 p-2 rounded') #TODO: Sign up process

        # Signup form -----------------------------
        with self.ui.dialog() as signup_dialog:
            with self.ui.card():
                self.ui.label('Sign Up').tailwind('text-xl','w-48', 'p-2', 'font-bold',)
                un = self.ui.input(label='User name', placeholder='Your username').classes('w-48 p-2')
                email = self.ui.input(label='Email', placeholder='Your email').classes('w-48 p-2')
                password = self.ui.input(label='Password', placeholder='Your password', password=True, ).classes('w-48 p-2')
                confirm_password = self.ui.input(label='Confirm Password', placeholder='Your password again', password=True, ).classes('w-48 p-2')
                submit = self.ui.button('Sign up', on_click=lambda: '',
                    ).classes('w-48 bg-blue-500 text-white font-bold py-2 px-4 p-2 rounded') #TODO: signup process
                
       # Header ----------------------------------
        with self.ui.header().classes(replace='flex block font-mono shadow-md bg-white text-md min-h-12') as header:
            with self.ui.grid(columns=4).classes('flex justify-between flat box-shadow-none'):
                     # Menu & Name ----------------------------------
                with self.ui.element():
                    with self.ui.row():
                        # Label ----------------------------------
                        self.ui.label('Vektir Labs').classes('flex p-2 pl-4 font-mono text-slate-600 text-lg font-bold')

                # Tabs ----------------------------------
                with ui.tabs().classes('flex justify-between blue w-100 text-slate-600 ') as tabs:
                    h1 = ui.tab('Home')
                    t1 = ui.tab('Industry')
                    t2 = ui.tab('Projects')
                    t3 = ui.tab('About')
                    t4 = ui.tab('Contact Us')

                # Auth ----------------------------------
                with self.ui.element():
                    # Login button ----------------------------------    
                    self.ui.button('Login', on_click=login_dialog.open,
                    ).tailwind('flex-none','w-100', 'bg-green','bg-gray-600','text-grey-800','capitalize', 'm-2')

                    # Sign up button ----------------------------------    
                    self.ui.button('Sign up', on_click=signup_dialog.open,
                    ).tailwind('flex-none','w-100', 'bg-gray-600','text-grey-800','capitalize', 'm-2')

        # Body ----------------------------------
        with self.ui.tab_panels(tabs, value=h1).classes('w-full capitalize'):
            with self.ui.tab_panel(h1):
                self.ui.markdown('# Welcome to Vektir Labs'
                    ).classes('flex justify-center w-full p-2 pl-4 font-mono text-slate-600 text-lg font-bold')

            with self.ui.tab_panel(t1):
                self.ui.markdown('# Vektir Labs - Industries'
                    ).classes('flex justify-center w-full p-2 pl-4 font-mono text-slate-600 text-lg font-bold')

            with self.ui.tab_panel(t2):
                self.ui.markdown('# Vektir Labs - Projects'
                    ).classes('flex justify-center w-full p-2 pl-4 font-mono text-slate-600 text-lg font-bold')

            with self.ui.tab_panel(t3):
                self.ui.markdown('# Vektir Labs - About'
                    ).classes('flex justify-center w-full p-2 pl-4 font-mono text-slate-600 text-lg font-bold')

            with self.ui.tab_panel(t4):
                self.ui.markdown('# Vektir Labs - Contact Us'
                    ).classes('flex justify-center w-full p-2 pl-4 font-mono text-slate-600 text-lg font-bold')

        