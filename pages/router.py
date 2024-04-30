from nicegui import APIRouter, ui
from components.headers import default_header
from components.sidebars import default_sidebar

# Set up NiceGUI router ----------------------------------------------
router = APIRouter()

# Define routes -------------------------------------------------------
@ui.page('/')
def get_index_view():
    # Page Setup ----------------------------------
    default_header()

    # Body ----------------------------------
    ui.link('landing Page', '/')
    ui.link('Home', '/home')
    ui.link('Login', '/login')

@ui.page('/home')
def get_home_view():
    # Page Setup ----------------------------------
    default_header()
    default_sidebar()

    # Body ----------------------------------  
    ui.label('Authenticated Home Page')
    ui.link('landing Page', '/')
    ui.link('Home', '/home')
    ui.link('Login', '/login')

@ui.page('/login')
def get_login_view():
    # Page Setup ----------------------------------
    default_header()

    # Body ----------------------------------------
    ui.label('Login Page')
    ui.link('landing Page', '/')
    ui.link('Home', '/home')
    ui.link('Login', '/login')
