import os

import cherrypy
from jinja2 import Environment,FileSystemLoader
from .bhav import BhavFile
from .settings import conf


current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir),trim_blocks=True)


class Hello(object):
    
    @cherrypy.expose
    def index(self,length=""):
        try:
            file = open(BhavFile().get_file_name())
        except FileNotFoundError:
            BhavFile().perform()

        
        template = env.get_template('/templates/index.html')
        
        
        if length == "":
            data = BhavFile().return_required_data(10)
        else:
            length = length.upper()
            data = BhavFile().search_values(length)

        date = BhavFile().get_date().strftime('%d-%m-%y')
        return template.render(data = data,title = "Title",length = length,date = date, today = BhavFile().get_today())
