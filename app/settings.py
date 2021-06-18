import os

conf = {
    "/css":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./app/static/css")
    },
    "/html" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./app/templates")
    },
    "/favicon":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./app/static/favicon")
    },
    "/favicon.ico" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./app/static/favicon/favicon.ico")
    },
    "/js":{
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : os.path.abspath("./app/static/js")
    }
}