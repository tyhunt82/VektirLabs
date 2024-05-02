from nicegui import APIRouter, ui

# Import pages -------------------------------------------------------
from pages.index import index_page
from pages.home import home_page 
from pages.forgot import forgot_page 
from pages.temp1 import temp1_page
from pages.temp2 import temp2_page

# Set up NiceGUI router ----------------------------------------------
router = APIRouter()

# Define routes -------------------------------------------------------
@ui.page('/')
def get_index_view():
    index_page()

@ui.page('/home')
def get_home_view():
    home_page()

@ui.page('/forgot')
def get_forgotpw_view():
    forgot_page()

# Testing and Temp pages ------------------------------------------------
@ui.page('/temp1')
def get_temp1_view():
    temp1_page()

@ui.page('/temp2')
def get_temp2_view():
    temp2_page()