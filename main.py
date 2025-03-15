import cherrypy
from app.tools.cors import use_cors
from app.controllers.google_auth_controller import GoogleAuthController
from app.controllers.google_calendar_controller import GoogleCalendarController

use_cors()

cherrypy.config.update({
    "server.socket_host": "0.0.0.0",
    "server.socket_port": 8080,
    "tools.sessions.on": True,
    "tools.sessions.storage_type": "ram",  
    "tools.sessions.storage_class": cherrypy.lib.sessions.RamSession,  
    "tools.sessions.timeout": 60,
})

config={"/": {  "tools.cors.on": True,  "tools.response_headers.on": True }}

cherrypy.tree.mount(GoogleAuthController(), "/api/auth/google", config=config)
cherrypy.tree.mount(GoogleCalendarController(), "/api/google-calendar", config=config)

cherrypy.engine.start()
cherrypy.engine.block()
