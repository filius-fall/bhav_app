## BhavCopy

-----------------------------------

This app shows data of BhavCopy file published by  BSE on their official site



### Introduction

----------------------------

This application checks for today file report of bhavcopy and if present parses, downloads and extract the csv file in it.

Then the records is csv file are written in to Redis into appropriate data structures

If todays report is not published yet, then it checks for the previous day data and publishes it



### Setup

----------------------------

##### Prerequisites:

- Python version 3
- Virtual environment
- All Packages in requirements.txt
- .env file to load your environment variables
- Redis-server should be running in background.

```
$ redis-server
```

If you are using Ubuntu/Debian

### Configuration

-------------------------

Create a .env file with the following variables:

```
DEBUG = "1 or 0" # 1 for development and 0 for Deployment

REDIS_DB = " "              # Which Redis database you are using
REDIS_HOST = " "            # Address at which server is running
REDIS_PASSWORD = " "        # Your Redis Password 
REDIS_PORT = 6379           # 6379 is Default you can change if you are using another port 
REDIS_USERNAME = " "        # Your Redis Username
```

### Running

---------------------

#### Development

```
$ python3 -u run.py
```



### References

---------------

- [Cherrypy Documentation](https://docs.cherrypy.org/en/latest/)
- [Introduction to Redis Data Structures](https://university.redislabs.com/courses/course-v1:redislabs+RU101+2021_03/course/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis-py Documentation](https://redis-py.readthedocs.io/en/stable/)