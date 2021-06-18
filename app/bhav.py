import io
import os
import json
import requests
import csv
import zipfile

from datetime import date,timedelta

from app.redis_client import RedisClient


FIELDS = ['code', 'name', 'group','type','open', 'high', 'low', 'close']
HEADERS = {'User-Agent': 'Mozilla/5.0 (Linux Mint 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
TODAY = date.today()
r = RedisClient().connect()



def formatted_date(date):
    """
    Arguments    :  Date
    Returns      :  String (Contains formatted date)
    Descryption  :
                    This function returns formated version of given data 
                    example: formatted_date(date(10,6,21)) will return '10621'
    """ 
    return date.today().strftime('%d-%m-%y')

def file_name(date):
    """
    Arguments    :  Date
    Returns      :  Path
    Descryption  :
                    This Function returns file path of given csv file   
    """
    file_name = f"{date.strftime('EQ%d%m%y_CSV')}".replace('_','.')
    file = os.path.join(os.path.abspath('./media'),file_name)

    return file

def get_url(date):
    """
    Arguments    :  Date
    Returns      :  URL
    Descryption  :
                    This file checks if the url for the current date exists or not and return the url if exists
                    If not it raises HTTPError and returns false
    """
    try:
        url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=HEADERS)
        url.raise_for_status()
    except requests.HTTPError:
        return False

    return url

def get_date():
    """
    Arguments    :  URL
    Returns      :  Path
    Descryption  :
                    This function gets the last valid date for which the url exists.
                    It Loops back until the valid date for url exists
    """
    date = TODAY
    while True:
        if get_url(date):
            return date
        else:
            date = date - timedelta(days=1)

    return date

def download_extract_url(url):
    """
    Arguments    :  URL
    Returns      :  Path
    Descryption  :
                    This Function reads the contents of zip file of the url
                    Then downloads the extracted file to given directory
    """
    if not url:
        return None

    zip_file = zipfile.ZipFile(io.BytesIO(url.content))
    path_to_file = os.path.abspath('./media')
    zip_file.extractall(os.path.abspath(path_to_file))

    return os.path.join(path_to_file,os.listdir(path_to_file)[-1])

def read_data_csv(file):
    """
    Arguments    :  Expects path to a csv file
    Returns      :  List
    Descryption  :
                    This Function reads the data from the csv file given as argument
                    Then Returns the data as a list

    """
    directory = file
    d_list = []

    with open(directory,'r') as r:
        data = csv.DictReader(r,fieldnames=FIELDS)

        for i in data:
            d_list.append(i)
        
        d_list.pop(0)
        for i in d_list:
            del i[None]
            i['name'] = i['name'].strip()
    
    return d_list

def push_to_redis(csv_file):
    """
    Arguments    :  Expects path to a csv file
    Returns      :  No values
    Descryption  :
                    This Function reads the values from csv file given as an argument
                    Then push all the values to redis database

    """

    if r.dbsize() != 0:
        if r.get("BSE:DATE") == formatted_date(TODAY):
            return
    if get_url(TODAY):
        date = TODAY
    else:
        date = get_date()

    csv_file_dir = file_name(date)
    data_values = read_data_csv(csv_file_dir)

    r.set("DATE",formatted_date(TODAY))
    for i in data_values:
        key = f"BSE:{i.get('name').strip()}-{i.get('code')}"
        r.set(key,json.dumps(i))
    

def get_values_from_redis():
    """
    Arguments    :  No Args
    Returns      :  A List 
    Descryption  :
                    This Function reads the values from csv file given as an argument
                    Then push all the values to redis database

    """
    redis_keys = []
    redis_values = []
    
    for i in r.scan_iter("BSE:" + "*"):
        redis_keys.append(i)
    for j in redis_keys:
        redis_values.append(json.loads(r.get(j)))


    return redis_values

def search_values(n):
    """
    Arguments    :  String
    Returns      :  List
    Descryption  :
                    This Function returns the search values from Redis database as List

    """
    keys = []
    values = []
    
    for i in r.scan_iter("BSE:" + n.upper() + "*"):
        keys.append(i)
    for j in keys:
        values.append(json.loads(r.get(j)))
    
    return values


def get_scan_values(index):

    k = []
    m = []
    l = r.scan(cursor=0)
    k.append(l[1])

    for i in range(r.dbsize()):
        l = r.scan(cursor=l[0],count=10)
        k.append(l[1])

    print(len(k))
    for j in k[index]:
        m.append(json.loads(r.get(j)))

    return m

def get_scan_search_values(search,index):

    k = []
    m = []
    s = "BSE:" + search + "*"
    l = r.scan(cursor=0,match=s)
    k.append(l[1])

    for i in range(r.dbsize()):
        l = r.scan(l[0],s,10)
        k.append(l[1])

    # print(k)

    # print(len(k))
    for j in k[index]:
        m.append(json.loads(r.get(j)))

    return m
