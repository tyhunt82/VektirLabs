from nicegui import APIRouter, ui

# Import pages -------------------------------------------------------
from pages.index import index_page
from pages.home import home_page 
from pages.forgot import forgot_page 
from pages.template import template_page

# Set up NiceGUI router ----------------------------------------------
router = APIRouter()

# Define routes -------------------------------------------------------
@ui.page('/')
def get_index_view():
    index_page()

@ui.page('/home')
def get_home_view():
    home_page()
  
@ui.page('/temp')
def get_temp_view():
    template_page()

@ui.page('/forgot')
def get_temp_view():
    forgot_page()