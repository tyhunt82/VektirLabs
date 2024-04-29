from nicegui import ui
from nicegui import Tailwind

with ui.header().classes(replace='text-lg min-h-12 bg-gray-800')as header:
    with ui.grid(columns=3).classes('flex'):
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flex-none w-14 h-12')
        ui.label('The Labs').classes('align-middle text-white text-lg font-bold ')
        
        with ui.tabs().classes('grow text-xl font-bold h-12') as tabs:
            ui.tab('A')
            ui.tab('B')
            ui.tab('C')

        ui.button('Login', 
                on_click=lambda: ui.notify('Your logged in')
                ).classes('''flex-none w-20 h-12 bg-gray-800 text-white px-4 py-2  rounded-md''').props('flat')
        
        ui.label('or').classes('text-sm text-gray-400')

        ui.button('Sign in', 
                on_click=lambda: ui.notify('Your signed in')
                ).classes('''flex-none w-20 h-12 bg-gray-800 text-white px-4 py-2  rounded-md''').props('flat')

with ui.left_drawer().classes('bg-gray-100') as left_drawer:
    ui.label('Left menu')
    ui.separator()
    with ui.expansion('Expand!', icon='work').classes('w-full'):
        ui.label('inside the expansion')
   

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    pass
    

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.label('Content of A')
    with ui.tab_panel('B'):
        ui.label('Content of B')
    with ui.tab_panel('C'):
        ui.label('Content of C')


ui.run()