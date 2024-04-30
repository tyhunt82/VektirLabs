from nicegui import APIRouter, ui
from components.layout import default_header, default_sidebar

router = APIRouter()

@ui.page('/')
def get_index_view():
    default_header()

    # Body ----------------------------------
    ui.link('landing Page', '/')
    ui.link('Home', '/home')


@ui.page('/home')
def get_home_view():
    default_header()
    default_sidebar()

    # Body ----------------------------------  
    ui.label('Authenticated Home Page')
    ui.link('landing Page', '/')
    ui.link('Home', '/home')
