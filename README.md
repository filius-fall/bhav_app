## BhavCopy

-----------------------------------

This app shows data of BhavCopy file published by  BSE on their official site



### Introduction

----------------------------

This application checks for today file report of bhavcopy and if present parses, downloads and extract the csv file in it.

Then the records in csv file are written in to Redis into appropriate data structures

If todays report is not published yet, then it checks for the previous day data and publishes it



## Setup

---------------------------

### Prerequisites:



- Python version 3

- Virtual environment

  [virtualenv](https://packaging.python.org/key_projects/#virtualenv) is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

  ##### Installing virtualenv

  If you are using macOS or Linux

  ```
  $ python3 -m pip install --user virtualenv
  ```

  #### Creating virtualenv

  ```
  python3 -m venv env
  ```

  #### Activating virtalenv

  ```
  source env/bin/activate
  ```

  

- All Packages in requirements.txt

  ```
  $ pip install -r requirements.txt
  ```

  

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



###  Testing

--------------

You can test the code and can check the execution time of the code using pytest

#### Steps:

1. Install Pytest

   ```
   $ pip install -U pytest
   ```

2. Run multiple tests:

   `pytest` will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows [standard test discovery rules](https://docs.pytest.org/en/6.2.x/goodpractices.html#test-discovery).

   ```
   $ pytest
   ```

   Run test on single file

   ```
   pytest -q /path/to/test_file
   ```

   -q/--quiet keeps ouput brief



### References

---------------

- [Cherrypy Documentation](https://docs.cherrypy.org/en/latest/)
- [Introduction to Redis Data Structures](https://university.redislabs.com/courses/course-v1:redislabs+RU101+2021_03/course/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis-py Documentation](https://redis-py.readthedocs.io/en/stable/)