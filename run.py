from app.views import Bhav
from app.settings import conf
import cherrypy



if __name__ == "__main__":
    cherrypy.quickstart(Bhav(),config = conf)