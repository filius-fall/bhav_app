import os
import requests

import cherrypy
from jinja2 import Environment,FileSystemLoader

from .bhav import get_values_from_redis,get_url,download_extract_url,HEADERS,get_date,r,push_to_redis,file_name,get_date,TODAY,search_values
from .settings import conf


current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir),trim_blocks=True)

class Bhav(object):

    @cherrypy.expose
    def index(self,length = ""):
        
        template = env.get_template('/templates/index.html')

        if len(os.listdir(os.path.abspath('./media'))) == 0:
            date = get_date()
            url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=HEADERS)
            download_extract_url(url)
 
        if r.dbsize() == 0:
            
            csv_file = file_name(get_date())
            push_to_redis(csv_file)
        
        if length == "":
            data = get_values_from_redis()
        else:
            data = search_values(length)

        count = 1

        return template.render(data = data,title = "Title",length = length,count = count, date = get_date(),today = TODAY)



