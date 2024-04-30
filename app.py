from nicegui import ui, app
from pages.router import get_index_view, get_home_view

# Landing Page ------------------------------------------------------
async def index():
    app.include_router(get_index_view)

# Run app -----------------------------------------------------------
ui.run()