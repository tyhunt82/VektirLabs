from nicegui import Tailwind, ui 

class template_page:
    def __init__(self):
        self.ui = ui
        username = 'Guest' 

        self.ui.page_title('Templates')

        # Header -----------------------------------
        with self.ui.header().classes(replace='font-mono shadow-lg bg-white text-md min-h-8') as header:
            with self.ui.grid(columns=3).classes('flex flat box-shadow-none'):
                self.ui.label('Vektir Labs').classes('flex-1 p-1 font-mono m-2 text-slate-600 min-h-8 h-8 text-lg font-bold')
                
                with self.ui.row():
                    self.ui.markdown(f'Welcome, {username}').classes('flex-none font-mono h-8 m-2 text-slate-600 text-sm')

                self.ui.button('Get Started',
                    on_click=lambda: right_login_drawer.toggle(),
                ).tailwind('flex-none', 'blue-100','capitalize', 'm-2','w-22 h-8')

    
         # Sidebars --------------------------------------
        
        # Right drawer ----------------------------------
        with self.ui.right_drawer().classes('bg-gray-100 w-96 bordered overlay') as right_login_drawer:
            self.ui.markdown('##### Login')
            self.ui.separator()

            # Login form ----------------------------------
            with ui.column().classes('flex justify-center '):
                email = self.ui.input(label='Email', placeholder='Your email').classes('w-48')
                password = self.ui.input(label='Password', placeholder='Your password', password=True, ).classes('w-48')
                
                submit = self.ui.button('Login', on_click= ui.notify('You are logged in!')
                                        ).classes('w-48 bg-blue-500 text-white font-bold py-2 px-4 rounded')



        # Body -------------------------------------------
        with self.ui.row().classes('flex w-full reveal bordered border-solid border-2 border-gray-300'):
            with self.ui.column().classes('flex flex-col w-full bg-white h-screen items-center py-2'):
                with ui.card().tight():
                    ui.image('https://picsum.photos/id/684/640/360')
                    with ui.card_section():
                        ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')
                #self.ui.link('landing Page', '/')
                #self.ui.link('Home', '/home')
                #self.ui.link('Login', '/login')
                #self.ui.link('Temp', '/temp')
                
