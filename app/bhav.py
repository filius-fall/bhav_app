import io
import os
import json
import requests
import csv
import zipfile

from datetime import date,timedelta

from app.redis_client import RedisClient
from app.settings import conf



class BhavFile:

    def __init__(self):
        self.today = date.today()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux Mint 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        self.r = RedisClient().connect()

    def get_today(self):
        return date.today().strftime('%d-%m-%y')
    
    def validate_url(self,date):
        
        try:
            url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=self.headers)
            url.raise_for_status()
        except requests.HTTPError:
            return False

        return url

    def get_date(self):
        
        date = self.today
        while True:
            if self.validate_url(date):
                return date
            else:
                date = date - timedelta(days=1)

        return date

    def get_url(self):

        k = self.get_date()
        url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(k),headers=self.headers)

        return url


    def get_file_name(self):
        date = self.get_date()
        FILE_NAME = f"{date.strftime('EQ%d%m%y_CSV')}".replace('_','.')

        FILE = os.path.join(os.path.abspath('./media'),FILE_NAME)

        return FILE


    def download_and_extract_csv(self):
        url = self.get_url()
        zip_file = zipfile.ZipFile(io.BytesIO(url.content))
        zip_file.extractall(os.path.abspath('./media'))
        return None

    def push_values_to_redis(self):
        
        self.r.flushall()
        file_name = self.get_file_name()
        data = self.return_only(file_name)
        for i in data:
            key = f"BSE:{i.get('name').strip()}-{i.get('code')}"
            self.r.set(key,json.dumps(i),ex=86400)

    def return_only(self,csv_file):
        
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

            return data_list


    def return_required_data(self,n: int):
        
        k = []
        file_name = self.get_file_name()
        data_list = self.return_only(file_name)
        count = 0
        for i in data_list:
            if count < n:
                k.append(i)
                count = count + 1
            else:
                break

        return k

    def search_values(self,search):

        keys = []
        data = []

        for i in self.r.scan_iter('BSE:' + search + '*'):
            keys.append(i.decode('UTF-8'))

        for j in keys:
            data.append(json.loads(self.r.get(j).decode('UTF-8')))

        return data


    def perform(self):

        date = self.get_date()
        if not self.validate_url(date):
            return

        self.download_and_extract_csv()
        self.push_values_to_redis()