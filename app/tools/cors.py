import cherrypy

def cors_tool():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*";
    cherrypy.response.headers['Access-Control-Allow-Methods'] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
    cherrypy.response.headers['Access-Control-Allow-Headers'] = "Content-Type, Authorization"

cherrypy.tools.cors = cherrypy.Tool( "before_handler", cors_tool)    