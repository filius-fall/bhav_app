import cherrypy
from jinja2 import Environment,FileSystemLoader
import os
from get_data import download_and_extract_csv,return_only,return_required_data,search_values,get_file_name,push_values_to_redis,get_date,get_today


current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir),trim_blocks=True)

conf = {
    "/static/css":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./static/css")
    },
    "/html" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./templates")
    },
    "/static/favicon/favicon.ico":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./static/favicon")
    },
    "/favicon.ico" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./static/favicon/favicon.ico")
    }
}
class Hello(object):
    
    @cherrypy.expose
    def home(self,length = 1):
        return length
    
    @cherrypy.expose
    def index(self,length=""):
        try:
            file = open(get_file_name())
        except FileNotFoundError:
            download_and_extract_csv()
            push_values_to_redis()

        
        template = env.get_template('/templates/index.html')
        
        
        if length == "":
            data = return_required_data(10)
        else:
            length = length.upper()
            data = search_values(length)

        date = get_date().strftime('%d-%m-%y')
        return template.render(data = data,title = "Title",length = length,date = date, today = get_today())
    


if __name__ == "__main__":
    cherrypy.quickstart(Hello(),config = conf)