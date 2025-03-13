import cherrypy
from app.tools.cors import cors_tool
from app.controllers.google_auth_controller import GoogleAuthController
from app.controllers.google_calendar_controller import GoogleCalendarController

cherrypy.config.update({
    "server.socket_host":"0.0.0.0",
    "server.socket_port": 8080
})

cherrypy.tools.cors = cors_tool

cherrypy.tree.mount(GoogleAuthController(), "/api/auth/google", config={"global": {"tools.cors.on": True}})
cherrypy.tree.mount(GoogleCalendarController(), "/api/google-calendar", config={"global": {"tools.cors.on": True}})

cherrypy.engine.start()
cherrypy.engine.block()