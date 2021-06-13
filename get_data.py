from datetime import date,timedelta
import os
import io,zipfile
from urllib.request import Request, urlopen
import csv
import redis,json,requests

r = redis.StrictRedis()

today = date.today()

headers = {'User-Agent': 'Mozilla/5.0 (Linux Mint 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


def validate_url(date):
    
    try:
        url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=headers)
        url.raise_for_status()
    except requests.HTTPError:
        return False

    return url



def get_date():

    date = today
    while True:
        if validate_url(date):
            return date
        else:
            date = date - timedelta(days=1)  
    return date

def get_file_name():
    date = get_date()
    FILE_NAME = f"{date.strftime('EQ%d%m%y_CSV')}".replace('_','.')

    FILE = os.path.join('./media',FILE_NAME)

    return FILE

def get_url():

    k = get_date()
    url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(k),headers=headers)

    return url


def get_today():
    return date.today().strftime('%d-%m-%y')

def download_and_extract_csv():
    url = get_url()
    zip_file = zipfile.ZipFile(io.BytesIO(url.content))
    zip_file.extractall(os.path.abspath('./media'))
    return None



def return_only(csv_file):
    field = ['code', 'name', 'group','type','open', 'high', 'low', 'close']
    data_list = []
    with open(csv_file,'r') as r:

        data = csv.DictReader(r,fieldnames=field)

        for i in data:
            data_list.append(i)

        data_list.pop(0)
        for i in data_list:
            del i[None]
            i['name'] = i['name'].strip()

        # print(data_list[0])
        return data_list

def return_required_data(n: int):
    k = []
    file_name = get_file_name()
    data_list = return_only(file_name)
    count = 0
    for i in data_list:
        if count < n:
            k.append(i)
            count = count + 1
        else:
            break

    # print(k)
    return k

def push_values_to_redis():
    r.flushall()
    file_name = get_file_name()
    data = return_only(file_name)
    for i in data:
        key = f"BSE:{i.get('name').strip()}-{i.get('code')}"
        r.set(key,json.dumps(i),ex=86400)
        print('EXPIRY SETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')

def search_values(search):

    keys = []
    data = []

    for i in r.scan_iter('BSE:' + search + '*'):
        keys.append(i.decode('UTF-8'))

    for j in keys:
        data.append(json.loads(r.get(j).decode('UTF-8')))

    return data

def validate_file():
        try:
            file = open(get_file_name())
        except FileNotFoundError:
            download_and_extract_csv()
            push_values_to_redis()

if __name__ == "__main__":
    download_and_extract_csv()
    # copy_required_to_another()
    return_required_data(5)
    push_values_to_redis()
