from app.views import Hello
from app.settings import conf
import cherrypy



if __name__ == "__main__":
    print('STARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT_________________________YYYYYYYYYYYYYYYYYyy')
    cherrypy.quickstart(Hello(),config = conf)