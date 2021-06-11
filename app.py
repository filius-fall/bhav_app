import cherrypy
from jinja2 import Environment,FileSystemLoader
import os
from get_data import download_and_extract_csv,return_only,return_required_data,search_values,get_today,FILE,push_values_to_redis


current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir),trim_blocks=True)

conf = {
    "/css":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./css")
    },
    "/html" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./templates")
    }
}
class Hello(object):
    # @cherrypy.expose
    # def index(self):
    #     return "Hello world"
    
    @cherrypy.expose
    def home(self,length = 1):
        return length
    
    @cherrypy.expose
    def index(self,length=""):
        try:
            file = open('./media/EQ110621.CSV')
        except FileNotFoundError:
            download_and_extract_csv()
            push_values_to_redis()

        
        template = env.get_template('/templates/index.html')
        
        
        if length == "":
            data = return_required_data(10)
        else:
            length = length.upper()
            data = search_values(length)

        date = get_today()
        return template.render(data = data,title = "Title",length = length,date=date)
    


if __name__ == "__main__":
    cherrypy.quickstart(Hello(),config = conf)