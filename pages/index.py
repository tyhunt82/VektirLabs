from nicegui import Tailwind, ui 

class index_page:
    def __init__(self):
        self.ui = ui
        self.ui.page_title('Vektir Labs')
        self.isAuthd = False
        username = 'Guest' # This will be replaced with the actual username and annonimous user
        
       # Header ----------------------------------
        with self.ui.header().classes(replace='flex block font-mono shadow-md bg-white text-md min-h-12') as header:
            with self.ui.grid(columns=3).classes('flex justify-between flat box-shadow-none'):
                self.ui.label('Vektir Labs').classes('flex-1 p-2 pl-4 font-mono text-slate-600 text-lg font-bold')

                # Login form ----------------------------------
                with self.ui.dialog() as login_dialog:
                    with self.ui.card():
                        self.ui.label('Login').tailwind('text-xl','w-48', 'p-2', 'font-bold',)
                        email = self.ui.input(label='Email', placeholder='Your email').classes('w-48 p-2')
                        password = self.ui.input(label='Password', placeholder='Your password', password=True, ).classes('w-48 p-2')
                        fpw = self.ui.link('Forgot Password', '/forgot').classes('block text-center p-2')
                        submit = self.ui.button('Login', on_click=lambda: '',
                            ).classes('w-48 bg-green text-white font-bold py-2 px-4 p-2 rounded') #TODO: Sign up process

                # Signup form ----------------------------------
                with self.ui.dialog() as signup_dialog:
                    with self.ui.card():
                        self.ui.label('Sign Up').tailwind('text-xl','w-48', 'p-2', 'font-bold',)
                        un = self.ui.input(label='User name', placeholder='Your username').classes('w-48 p-2')
                        email = self.ui.input(label='Email', placeholder='Your email').classes('w-48 p-2')
                        password = self.ui.input(label='Password', placeholder='Your password', password=True, ).classes('w-48 p-2')
                        confirm_password = self.ui.input(label='Confirm Password', placeholder='Your password again', password=True, ).classes('w-48 p-2')
                        submit = self.ui.button('Sign up', on_click=lambda: '',
                            ).classes('w-48 bg-blue-500 text-white font-bold py-2 px-4 p-2 rounded') #TODO: signup process
                        
                # Login button ----------------------------------    
                self.ui.button('Login', on_click=login_dialog.open,
                ).tailwind('flex-none','w-100', 'bg-green','bg-gray-600','text-grey-800','capitalize', 'm-2')

                # Sign up button ----------------------------------    
                self.ui.button('Sign up', on_click=signup_dialog.open,
                ).tailwind('flex-none','w-100', 'bg-gray-600','text-grey-800','capitalize', 'm-2')


        # Body ----------------------------------
        self.ui.markdown('# Welcome to Vektir Labs').classes('flex justify-center w-full p-2 pl-4 font-mono text-slate-600 text-lg font-bold')
