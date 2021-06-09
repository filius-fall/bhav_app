import cherrypy
from jinja2 import Environment,FileSystemLoader
import os
from get_data import download_and_extract_csv,return_only,return_required_data


current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir),trim_blocks=True)


class Hello(object):
    @cherrypy.expose
    def index(self):
        return "Hello world"
    
    @cherrypy.expose
    def home(self,length = 1):
        return length
    
    @cherrypy.expose
    def html_page(self):
        template = env.get_template('index.html')
        data = return_required_data(5)
        return template.render(data = data,title = "Title")

if __name__ == "__main__":
    cherrypy.quickstart(Hello())