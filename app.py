from nicegui import ui
from nicegui import Tailwind

with ui.header().classes(replace='flex text-lg min-h-18 bg-gray-800')as header:
    with ui.row().classes('flex'):
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').tailwind('bg-gray-800')
        ui.label('The Labs').classes('text-xl font-bold')
        ui.button('Sign in', 
                on_click=lambda: ui.notify('Your signed in')
                ).classes('''flex justify-end bg-gray-800 text-white px-4 py-2 float-right rounded-md''').props('flat')

    



with ui.footer(value=False).classes('bg-white') as footer:
    with ui.row().classes('center'):
        ui.label('Footer').classes('black')
    ui.label('Label B').tailwind('drop-shadow', 'font-bold', 'text-green-600')

with ui.left_drawer().classes('bg-gray-100') as left_drawer:
    ui.label('Left menu')
    with ui.tabs() as tabs:
        ui.tab('A')
        ui.tab('B')
        ui.tab('C')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support')

    

with ui.tab_panels(tabs, value='A').classes('w-full'):


    with ui.tab_panel('A'):
        ui.label('Content of A')
    with ui.tab_panel('B'):
        ui.label('Content of B')
    with ui.tab_panel('C'):
        ui.label('Content of C')

ui.run()