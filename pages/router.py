from nicegui import APIRouter, ui

# Import pages -------------------------------------------------------
from pages.index import index_page
from pages.home import home_page 
from pages.login import login_page

# Set up NiceGUI router ----------------------------------------------
router = APIRouter()

# Define routes -------------------------------------------------------
@ui.page('/')
def get_index_view():
    index_page()

@ui.page('/home')
def get_home_view():
    home_page()
  
@ui.page('/login')
def get_login_view():
    login_page()