from nicegui import ui, app
from pages.router import router

# App configuration -------------------------------------------------
app.add_static_files('/static', 'static')
 
    # TODO: Add app configuration here
        # State management
        # Check user auth
        # Set up firebase

# NOTE: On Windows reload must be disabled to make asyncio.create_subprocess_exec 
# work (see https://github.com/zauberzeug/nicegui/issues/486)
# ui.run(reload=platform.system() != 'Windows')


# Run app -----------------------------------------------------------
ui.run()