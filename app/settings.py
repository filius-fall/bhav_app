import os

PATH = os.path.abspath(os.path.dirname(__file__))

conf = {    
    "/css":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.join(PATH,'css')
    },
    "/html" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.join(PATH,'templates')
    },
    "/favicon":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("../static/favicon")
    },
    "/favicon.ico" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("../static/favicon/favicon.ico")
    },
    "/templates" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./templates")
    }
}