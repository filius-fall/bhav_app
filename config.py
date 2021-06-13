import os

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


REDIS_NAME = "Sreeram"
REDIS_SITE = "LOCAL HOST"