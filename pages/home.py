from nicegui import Tailwind, ui 

class home_page:
    def __init__(self):
        self.ui = ui
        self.un = 'Guest'
        self.ui.page_title('Home')
        self.isAuthd = False

        # Header ----------------------------------
        with self.ui.header().classes(replace='font-mono shadow-md bg-white text-md min-h-12') as header:
            with self.ui.grid(columns=3).classes('flex justify-between flat box-shadow-none'):
                
                self.ui.button(on_click=lambda: left_drawer.toggle(), icon='menu'
                ).tailwind('flex-none', 'bg-slate-500', 'm-2')

                self.ui.label('Vektir Labs').classes('flex-1 p-2 font-mono text-slate-600 text-lg font-bold')

                # Login form ----------------------------------
                with self.ui.dialog() as login_dialog:
                    with self.ui.card():
                        self.ui.label('Login').tailwind('text-xl','w-48', 'p-2', 'font-bold',)
                        email = self.ui.input(label='Email', placeholder='Your email').classes('w-48 p-2')
                        password = self.ui.input(label='Password', placeholder='Your password', password=True, ).classes('w-48 p-2')
                        fpw = self.ui.link('Forgot Password', '/forgot').classes('block text-center p-2')
                        submit = self.ui.button('Login', on_click=self.ui.notify('Logged in'),
                            ).classes('w-48 bg-green text-white font-bold py-2 px-4 p-2 rounded') #TODO: Sign up process
                
                # Signup form ----------------------------------
                with self.ui.dialog() as signup_dialog:
                    with self.ui.card():
                        self.ui.label('Sign Up').tailwind('text-xl','w-48', 'p-2', 'font-bold',)
                        un = self.ui.input(label='User name', placeholder='Your username').classes('w-48 p-2')
                        email = self.ui.input(label='Email', placeholder='Your email').classes('w-48 p-2')
                        password = self.ui.input(label='Password', placeholder='Your password', password=True, ).classes('w-48 p-2')
                        confirm_password = self.ui.input(label='Confirm Password', placeholder='Your password again', password=True, ).classes('w-48 p-2')
                        submit = self.ui.button('Sign up', on_click=self.ui.notify('Logged in'),
                            ).classes('w-48 bg-blue-500 text-white font-bold py-2 px-4 p-2 rounded') #TODO: signup process
                        
                # Login button ----------------------------------    
                self.ui.button('Login', on_click=login_dialog.open,
                ).tailwind('flex-none','w-100', 'bg-green','bg-gray-600','text-grey-800','capitalize', 'm-2')

                # Sign up button ----------------------------------    
                self.ui.button('Sign up', on_click=signup_dialog.open,
                ).tailwind('flex-none','w-100', 'bg-gray-600','text-grey-800','capitalize', 'm-2')

      


        # Body ----------------------------------
        with self.ui.row().classes('flex w-full bordered'):
            with self.ui.column().classes('flex flex-col w-full bg-white h-screen items-center py-2'):
                self.ui.link('landing Page', '/')
                self.ui.link('Home', '/home')
                self.ui.link('Login', '/login')
                self.ui.link('Temp', '/temp')
           
        # Left Sidebar ----------------------------------
        with self.ui.left_drawer().classes('bg-gray-100') as left_drawer:
            self.ui.label(f'Welcome, {self.un}!').tailwind('block', 'w-full', 'text-lg', 'blue-500', 'm-2', 'text-center')
            self.ui.separator()
            with self.ui.expansion('Projects', icon='house').classes('w-full'):
                self.ui.label('Well 1').tailwind.text_color('bg-blue-500')
                self.ui.label('Well 2')
                self.ui.label('Well 3')
                self.ui.label('Well 4')
                self.ui.label('Well 5')
            self.ui.space()
            with ui.element('q-fab').props('icon=navigation color=blue-5'):
                self.ui.element('q-fab-action').props('icon=train color=blue-5') \
                    .on('click', lambda: ui.notify('train'))
                self.ui.element('q-fab-action').props('icon=sailing color=blue-5') \
                    .on('click', lambda: ui.notify('boat'))
                self.ui.element('q-fab-action').props('icon=rocket color=blue-5') \
                    .on('click', lambda: ui.notify('rocket'))

        # Right Sidebar ----------------------------------
        with self.ui.right_drawer().classes('bg-gray-100 w-200') as right_drawer:
            with self.ui.expansion('Get Started', icon='lock').classes('w-full'):
                self.ui.label('Login').props('borderless')
                self.ui.label('Sign up')
                self.ui.label('Anonymous')
                self.ui.label('Forgot Passwrord')